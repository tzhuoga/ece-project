import numpy as np
import cv2.aruco as aruco
import cv2


aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters_create()


def jpeg_to_mat(jpeg_data):
    return cv2.imdecode(np.fromstring(jpeg_data, dtype='uint8'), 1)

def detect_markers(gray):
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    # For demonstration purposes...
    aruco.drawDetectedMarkers(gray, corners, ids)
    cv2.imwrite('detection_test.jpg', gray)
    return ids
