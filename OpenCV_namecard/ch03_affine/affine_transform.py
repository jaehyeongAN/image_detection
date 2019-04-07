# -*- coding: utf-8 -*- 
'''
Created on 2017. 8. 29.

@author: jaehyeong
'''
import numpy as np
import cv2

def warpAffine():
    img = cv2.imread('../images/transform.png')
    
    pts1 = np.float32([[50,50],[200,50],[20,200]])    # 이동당할 대상 픽셀 위치
    pts2 = np.float32([[70,100],[220,50],[150,250]])  # 이동할 픽셀 위치
    
    M = cv2.getAffineTransform(pts1, pts2)  # 좌표이동 matrix
    
    result = cv2.warpAffine(img, M, (350, 300)) # 변환시킴,  (img, matrix, 변환될 이미지 크기)
    
    cv2.imshow('original', img)
    cv2.imshow('Affine Transform', result)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    
if __name__ == '__main__':
    warpAffine()
