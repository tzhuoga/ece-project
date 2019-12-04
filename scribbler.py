import serial


'''Byte Codes'''
GET_JPEG_COLOR_SCAN = 138
GET_JPEG_COLOR_HEADER = 137
GET_JPEG_GRAY_SCAN = 136
GET_JPEG_GRAY_HEADER = 135
GET_LINE_ALL = 76
GET_WINDOW = 84
GET_BATTERY = 89
SET_WINDOW = 127
SET_SPEAKER = 113
SET_MOTORS = 109
SET_ECHO_MODE = 98

ECHO_LENGTH = 9

JPEG_FAST = 0
JPEG_REG = 1

'''Frame width and height'''
FRAME_WIDTH = 256  # 427
FRAME_HEIGHT = 192 # 266


class Scribbler:
    jpeg_header = None

    def __init__(self, dev_str):
        self.s = serial.Serial(dev_str, 57600)

    def _write_command(self, name, data):
        self.s.write(bytearray([name] + data))

    def capture_jpeg_data(self, is_gray, mode):
        header_byte_code = GET_JPEG_GRAY_HEADER if is_gray else GET_JPEG_COLOR_HEADER
        scan_byte_code = GET_JPEG_GRAY_SCAN if is_gray else GET_JPEG_COLOR_SCAN
        if Scribbler.jpeg_header == None:
            self._write_command(header_byte_code, [0] * 8)
            Scribbler.jpeg_header = self._read_jpeg_header()
        self._write_command(scan_byte_code, [mode] + [0] * 7)
        self.s.write(1)
        jpeg = Scribbler.jpeg_header + self._read_jpeg_scan()
        return jpeg

    def grab_gray_array(self):
        width = int(FRAME_WIDTH / 2)
        height = int(FRAME_HEIGHT / 2)
        size = width * height
        gray_conf_window(s, 0, 1, 0, FRAME_WIDTH - 1, FRAME_HEIGHT - 1, 2, 2)
        write_command(GET_WINDOW, [0] * 8)
        self.s.write(0)
        image = self.s.read(size)
        return image

    def gray_conf_window(self, window, x_low, y_low, x_high, y_high, x_step, y_step):
        self.s.write(bytearray([SET_WINDOW, window, x_low, y_low, x_high, y_high, x_step, y_step, 0]))

    def _read_jpeg_header(self):
        buf = self.s.read(2)
        length = buf[0] + buf[1] * 256
        return self.s.read(length)

    def _read_jpeg_scan(self):
          buf = b''
          last_byte = 0
          while True:
                  by = self.s.read(1)
                  buf += by

                  # End-Of-Image marker
                  if last_byte == b'\xFF' and by == b'\xD9':
                          break
                  last_byte = by

          self.s.read(4 * 3) # start, read, compress

          return buf

    def play_tone(self, duration, frequency):
        self._write_command(SET_SPEAKER, [duration >> 8, duration % 256, \
            frequency >> 8, frequency % 256, 0, 0, 0, 0])
        self.s.read(20)

    def play_song(self, notes):
        for note in notes:
            self.play_tone(note[0], note[1])

    def set_motors(self, left, right):
        self._write_command(SET_MOTORS, [int((right + 1) * 100), int((left + 1) * 100), 0, 0, 0, 0, 0, 0])
        self.s.read(20)

    def read_line_sensors(self):
        if s.in_waiting == 0:
            write_command(GET_LINE_ALL, [0] * 8)
            s.read(ECHO_LENGTH) # ignore echo here
            ret = s.read(2)
            return [ret[0], ret[1]]
        return [None, None]

    def get_battery(self):
        self._write_command(GET_BATTERY, [0] * 8)
        b = s.read(2)
        raw = (b[0] >> 8) + b[1]
        return round(raw / 20.9813, 2)
