import time
import scribbler as s
from detect import *


DEVICE = '/dev/rfcomm0'

notes = { 'c': 261, 
          'd': 294,
          'e': 329, 
          'f': 349, 
          'g': 391, 
          'g#': 415,
          'a': 440,
          'b': 494,
          'bb': 466,
          'cH': 523,
          'dH': 587,
          'dH#':622,
          'eH': 659,
          'fH': 698,
          'fH#': 740,
          'gH': 784,
          'gH#': 831,
          'aH': 880,
          'bH': 988,
          'bHb':932,
          'cHH':1046,
          'rest': 0}

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
        [500, notes['g#']],
        [350, notes['f']],
        [150, notes['cH']],
        [650, notes['a']]]

Mario1 = [[150, notes['eH']],
        [150, notes['eH']],
        [150, notes['rest']],
        [150, notes['eH']],
        [150, notes['rest']],
        [150, notes['cH']],
        [150, notes['eH']],
        [150, notes['rest']],
        [300, notes['gH']],
        [300, notes['rest']],
        [300, notes['g']]
        [300, notes['rest']]]

Mario2 = [[300, notes['cH']],
        [150, notes['rest']],
        [150, notes['g']],
        [300, notes['rest']],
        [300, notes['e']],
        [150, notes['rest']],
        [150, notes['a']],
        [150, notes['rest']],
        [150, notes['b']],
        [150, notes['rest']],
        [150, notes['bb']],
        [300, notes['a']],
        
        [100, notes['g']],
        [100, notes['e']],
        [100, notes['gH']],
        [300, notes['aH']],
        [150, notes['fH']],
        [150, notes['gH']],
        [150, notes['rest']],
        [150, notes['eH']],
        [150, notes['rest']],
        [150, notes['cH']],
        [150, notes['dH']],
        [150, notes['b']],
        [150, notes['rest']]]

Mario3 = [[300, notes['rest']],
        [150, notes['gH']],
        [150, notes['fH#']],
        [150, notes['fH']],
        [150, notes['dH#']],
        [150, notes['rest']],
        [150, notes['eH']],
        [150, notes['rest']],
        [150, notes['g#']],
        [150, notes['a']],
        [150, notes['cH']],
        [150, notes['rest']],
        [150, notes['a']],
        [150, notes['cH']],
        [150, notes['dH']],
        
        [150, notes['rest']],
        [150, notes['gH']],
        [150, notes['fH#']],
        [150, notes['fH']],
        [150, notes['dH#']],
        [150, notes['rest']],
        [150, notes['eH']],
        [150, notes['rest']],
        [150, notes['cHH']],
        [150, notes['rest']],
        [150, notes['cHH']],
        [150, notes['cHH']]]
        [600, notes['rest']]]
        [150, notes['gH']],
        [150, notes['fH#']],
        [150, notes['fH']],
        [150, notes['dH#']],
        [150, notes['rest']],
        [150, notes['eH']],
        
        [150, notes['rest']],
        [150, notes['g#']],
        [150, notes['a']],
        [150, notes['b']],
        [150, notes['rest']],
        [150, notes['a']],
        [300, notes['cH']],
        [150, notes['dH']],
        [150, notes['cH']],
        [150, notes['dH#']],
        [150, notes['rest']],
        [150, notes['dH']],
        [300, notes['rest']],
        
        [300, notes['cH']]]

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

#add qr function for Mario song 
    if second_marker == 0:
        sc.play_song(Mario1)
        sc.play_song(Mario2)
        sc.play_song(Mario2)
        sc.play_song(Mario3)
        sc.play_song(Mario3)
