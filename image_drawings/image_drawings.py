# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:29:20 2020

@author: heman
"""

import numpy as np
import cv2

img= cv2.imread('vivo.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(200,300),(255,255,255),50)

cv2.rectangle(img,(0,0),(400,450),(0,255,255),15)

cv2.circle(img,(100,63), 55, (0,255,0), -1)

pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
pts = pts.reshape((-1,1,2))


cv2.polylines(img, [pts], True, (0,100,255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'VIVO',(10,500),font,1,(0,0,0),2,cv2.LINE_AA)
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

