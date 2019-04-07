# -*- coding: utf-8 -*- 
'''
Created on 2017. 8. 28.

@author: jaehyeong
'''
# OpenCV - 이미지 읽기, 쓰기 및 표시하기
import numpy as np
import cv2

def handle_image():
    imgfile = '../images/sample.png'
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR) # 컬러이미지로 불러오기
    
    cv2.imshow('image',img) # 반환된 객체를 화면에 표시
    cv2.waitKey(0)          # 사용자가 키를 누를때까지 무한정(0) 기다림 
    cv2.destroyAllWindows() # 표시했던 모든 윈도우를 닫음
    #cv2.waitKey(1)
    
if __name__ == '__main__':
    handle_image()