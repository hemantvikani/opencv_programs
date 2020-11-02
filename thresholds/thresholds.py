# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:22:08 2020

@author: heman
"""

#using color image

import cv2
import numpy as np

img  = cv2.imread('bookpage.jpg')

retval , threshold = cv2.threshold(img,12,255,cv2.THRESH_BINARY)

cv2.imshow('original',img)
cv2.imshow('threshold',threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()



#use gray scale image

import cv2
import numpy as np
img  = cv2.imread('bookpage.jpg')
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

#adaptive thresholding

import cv2
import numpy as np
img  = cv2.imread('bookpage.jpg')
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('original',img)
cv2.imshow('Adaptive threshold',th)
cv2.waitKey(0)
cv2.destroyAllWindows()