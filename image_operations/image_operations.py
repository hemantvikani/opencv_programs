# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:47:23 2020

@author: heman
"""

import cv2
import numpy as np

img = cv2.imread('vivo.jpg',cv2.IMREAD_COLOR)

px = img[55,55]
img[55,55] = [255,255,255]

px = img[55,55]
print(px)

px = img[300:500,500:750]
print(px)

img[300:500,500:750] = [255,255,255]

px = img[300:500,500:750]
print(px)

print(img.shape)
print(img.size)
print(img.dtype)

vivo_face = img[200:311,210:494]
img[0:111,0:284] = vivo_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()