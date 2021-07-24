# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 16:39:01 2021

@author: USER
"""

import cv2

image = cv2.imread('eagle.png')

greyimg = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow('Eagle Bird',image)
cv2.imwrite('abc.png', image)

cv2.imshow('Grey Scale Image',greyimg)
cv2.imwrite('def.png',greyimg)

cv2.waitKey(0)
cv2.destroyAllWindows()