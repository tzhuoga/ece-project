import time
import scribbler as s
from detect import *


DEVICE = '/dev/rfcomm0'

notes = { 'c': 261, 
          'd': 294,
          'e': 329, 
          'f': 349, 
          'g': 391, 
          'gS': 415,
          'a': 440,
          'cH': 523,
          'eH': 659,
          'fH': 698 }

part1 = [[500, notes['a']],
        [500, notes['a']],
        [500, notes['a']],
        [350, notes['f']],
        [150, notes['cH']],
        [500, notes['a']],
        [350, notes['f']],
        [150, notes['cH']],
        [650, notes['a']]]


part2 = [[500, notes['eH']],
        [500, notes['eH']],
        [500, notes['eH']],
        [350, notes['fH']],
        [150, notes['cH']],
        [500, notes['gS']],
        [350, notes['f']],
        [150, notes['cH']],
        [650, notes['a']]]


if __name__ == '__main__':
    sc = s.Scribbler(DEVICE)
    ids = None

    # drive slowly forward
    sc.set_motors(-0.1, -0.1)

    # loop until a marker is detected
    while ids == None:
        jpeg = sc.capture_jpeg_data(True, s.JPEG_FAST)
        ids = detect_markers(jpeg_to_mat(jpeg))
    first_marker = ids.flat[0]
    print('I found marker #%d' % first_marker)

    # stop the robot
    sc.set_motors(0, 0)

    # if marker #0 was detected
    if first_marker == 0:
        sc.play_song(part1)
        time.sleep(0.150)
        sc.play_song(part2)
