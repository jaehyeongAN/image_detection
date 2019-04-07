# -*- coding: utf-8 -*- 
'''
Created on 2017. 8. 29.

@author: jaehyeong
'''
# OpenCV - 도형 외각 추출하기 2
import numpy as np
import cv2 
import matplotlib.pyplot as plt

def contour():
    imgfile = '../images/contour2.png'
    img = cv2.imread(imgfile)
    img2 = img.copy()
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    
    edge = cv2.Canny(imgray, 50, 200)  
    contours, hierarchy = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)    
    
    cnt = contours[0]
    cv2.drawContours(img, [cnt], 0, (0, 255, 0), 2)
        
    # 근사정확도(오차),    arcLength : Contour 둘레를 계산  , True:폐곡선(닫혀있는 외곡선)
    epsilon = 0.1 * cv2.arcLength(cnt, True)    # 오차를 10%로 
    # approxPolyDP : 다각형을 중심으로 꼭지점을 줄여나감
    approx = cv2.approxPolyDP(cnt, epsilon, True)   # approxPolyDP(contour, 오차(epsilon), 폐곡선/개곡선)
    cv2.drawContours(img2, [approx], 0, (0, 255, 0), 3)
    
    cv2.imshow('Contour', img)
    cv2.imshow('Approx', img2)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    
if __name__ == '__main__':
    contour()