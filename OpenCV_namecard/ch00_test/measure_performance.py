# -*- coding: utf-8 -*- 
'''
Created on 2017. 12. 29.

@author: jaehyeong
'''
import cv2

img1 = cv2.imread('./images/sample.png')

e1 = cv2.getTickCount()
for i in xrange(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print t
