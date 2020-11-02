# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:57:58 2020

@author: heman
"""

import numpy as np
import cv2

# Load two images
img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainlogo.png')
r1,c1,channels1 = img1.shape
r,c,channels = img2.shape
# I want to put logo on top-left corner, So I create a ROI
roi = img1[0:r,0:c]

#now create a mask of logo and create its inverse mask
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#add a threshold

ret,mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)
# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

dst = cv2.add(img1_bg,img2_fg)
img1[0:r, 0:c ] = dst


cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()