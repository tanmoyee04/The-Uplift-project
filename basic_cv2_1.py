# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 17:01:55 2021

@author: USER
"""

import cv2

img = cv2.imread('eagle.png')
print(img.dtype)
print(img.shape)
print(img.size)