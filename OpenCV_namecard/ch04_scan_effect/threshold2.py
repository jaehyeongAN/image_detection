# -*- coding: utf-8 -*- 
'''
Created on 2017. 8. 29.

@author: jaehyeong
'''
# threshold를 자동으로, 조명의 영향을 더 줄이기 -> Adaptive Threshold(이미지를 잘게 쪼개서 threshold를 각각 구함)
import numpy as np
import cv2

def adaptive_threshold():
    imgfile = '../images/document.jpg'
    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)
    
    # Resize image
    r = 600.0 / img.shape[0]
    dim = (int(img.shape[1] * r), 600)
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    # Blur image and apply adaptive threshold
    # GaussianBlur(적용할 img, (주변픽셀크기), 0)
    blur = cv2.GaussianBlur(img, (5, 5), 0) # 주변 픽셀의 평균값을 대입하여 블러효과, 주변픽셀크기가 크면 클수록 이미지가 뭉개짐
    
    # adaptiveThreshold(img ,threshold 최대값, algo, algo, 쪼개는 블럭정도, 주변밝기를 빼는 상수값)
    result_without_blur = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 10) # 보통 21,10을 사용
    #result_with_blur = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH, cv2.THRESH_BINARY, 21, 10)
    result_with_blur = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 10)
    
    cv2.imshow('Without Blur', result_without_blur)
    cv2.imshow('With Blur', result_with_blur)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    
if __name__ == '__main__':
    adaptive_threshold() 
    
    