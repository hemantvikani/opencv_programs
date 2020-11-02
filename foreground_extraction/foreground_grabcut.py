# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:34:10 2020

@author: heman
"""

import numpy as np
import matplotlib.pyplot as plt

import cv2

img  = cv2.imread('opencv-python-foreground-extraction-tutorial.jpg')

mask = np.zeros(img.shape[:2],np.uint8)

bgdmodel = np.zeros((1,65),np.float64)
fgdmodel = np.zeros((1,65),np.float64)

rect = (161,79,150,150)

cv2.grabCut(img,mask,rect,bgdmodel,fgdmodel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 0) | (mask == 1),0,1).astype('uint8')

img =img* mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()