# -*- coding: utf-8 -*- 
'''
Created on 2017. 8. 28.

@author: jaehyeong
'''
# OpenCV - 도형 외각 추출하기
import numpy as np
import cv2 
import matplotlib.pyplot as plt

def contour():
    imgfile = '../images/contour.jpg'
    img = cv2.imread(imgfile)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # cvtColor : 이미지의 색공간을 변환, BGR2GRAY : RGB를 gray로 바꿈
    
    edge = cv2.Canny(imgray, 100, 200)  #  Canny(img, min, max) : 이미지의 엣지를 판단, 100보다 낮으면 엣지X, 200보다 높으면 엣지로 판단 
    contours, hierarchy = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)    # findContours : 외각을 검출
    
    cv2.imshow('edge', edge)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 1)  # 검출한 외각을 원본이미지 위에 그림, index, (BGR색상값), 선 두께  
    cv2.imshow('Contour', img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    
if __name__ == '__main__':
    contour()