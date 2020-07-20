# -*- coding: utf-8 -*-
import cv2
def videoCapture():
    camera = cv2.VideoCapture(1)
    while True:
        ret, window=camera.read()
        cv2.imshow("Camera Window" , window)           
        if cv2.waitKey(1) & 0Xff == ord('q'):
            break    
    camera.relase()
    cv2.destroyAllWindows()
videoCapture()


