# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:09:53 2020

@author: heman
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('vivo.jpg',0)

#method to show image using opencv
cv2.imshow('image',img)


cv2.waitKey(0)
cv2.destroyAllWindows()

#another method to show image using matplotlib
plt.imshow(img,cmap='gray',interpolation = 'bicubic')
plt.xticks([]),plt.yticks([]) # to hide tick values on X and Y axis

plt.plot([200,300,400],[100,200,300],'c',linewidth=5)
plt.show() 
