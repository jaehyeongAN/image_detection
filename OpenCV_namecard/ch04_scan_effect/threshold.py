# -*- coding: utf-8 -*- 
'''
Created on 2017. 8. 29.

@author: jaehyeong
'''
# 스캔한 듯한 효과 주기
import numpy as np
import cv2

# Callback Function for Trackbar (but do not any work)
def nothing(x):
    pass

def global_threshold():
    imgfile = '../images/document.jpg'
    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)
    
    # Resize image
    r = 600.0 / img.shape[0]    # 가로 픽셀을 600으로 고정
    dim = (int(img.shape[1] * r), 600)
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    WindowName = "Window"
    TrackbarName = "Threshold"
    
    # Make Window and Trackbar
    cv2.namedWindow(WindowName)
    cv2.createTrackbar(TrackbarName, WindowName, 200, 255, nothing) # (TrackbarName, WindowName, 초기값, 최대값, 이동했을때 함수)
    
    # Allocate destination image
    Threshold = np.zeros(img.shape, np.uint8)   # 이미지의 가로,세로 픽셀을 0으로 초기화
    
    # Loop for get trackbar pos and process it
    while True:
        # Get position in trackbar
        TrackbarPos = cv2.getTrackbarPos(TrackbarName, WindowName)  # 트랙바의 위치를 반환
        # Apply threshold(이미지 이진화 함수)
        cv2.threshold(img, TrackbarPos, 255, cv2.THRESH_BINARY, Threshold)
        # Show in window
        cv2.imshow(WindowName, Threshold)
        
        # wait for ESC key to exit
        k = cv2.waitKey(0)
        if k == 27:
            cv2.destroyAllWindows()
            cv2.waitKey(1)
            break
    return
 
if __name__ == '__main__':
    global_threshold() 
    
    