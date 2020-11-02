# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:31:17 2020

@author: heman
"""

import cv2
import numpy as np

#read the original color image

img_rgb  =cv2.imread('opencv-template-matching-python-tutorial.jpg')

img_gray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)

template = cv2.imread('opencv-template-for-matching.jpg',0)

w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

threshold  = 0.7

#check by changing the threshold,we can get false positives if we set 0.7 as threshold

loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)
    
cv2.imshow('Detected',img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()