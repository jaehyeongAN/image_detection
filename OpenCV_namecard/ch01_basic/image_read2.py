# -*- coding: utf-8 -*- 
'''
Created on 2017. 8. 28.

@author: jaehyeong
'''
import numpy as np 
import cv2

def handle_image():
    imgfile = '../images/sample.png'
    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE) # 흑백이미지로 불러오기
    
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)  # 윈도우 사이즈 지정, autosize : 원본, normal : 크기조정가능
    cv2.imshow('image',img)
    k = cv2.waitKey(0)
    
    # wait for ESC key to exit
    if k == 27:
        cv2.destroyAllWindows()
        cv2.waitKey(1)
    # wait for 's' key to save and exit
    elif k == ord('s'):
        cv2.imwrite('grayImage.png', img)   
        cv2.destroyAllWindows()
        cv2.waitKey(1)

if __name__ == '__main__':
    handle_image()