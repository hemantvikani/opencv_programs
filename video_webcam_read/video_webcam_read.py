# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:32:58 2020

@author: heman
"""

import numpy as np
import cv2

cap = cv2.VideoCapture('sunanda.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))


while(True):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(frame)
    
    cv2.imshow('frame',gray)
    
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()