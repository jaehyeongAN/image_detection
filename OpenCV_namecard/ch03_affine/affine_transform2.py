# -*- coding: utf-8 -*- 
'''
Created on 2017. 8. 29.

@author: jaehyeong
'''
# 포인트를 지정하지 않고 자동으로 반듯하게 
import numpy as np
import cv2

def warpPerspective():
    img = cv2.imread('../images/transform.jpg')
    
    topLeft = [127, 157]
    topRight = [448, 152]
    bottomRight = [579, 526]
    bottomLeft = [54, 549]

    pts1 = np.float32((topLeft, topRight, bottomRight, bottomLeft))
    
    w1 = abs(bottomRight[0] - bottomLeft[0])
    w2 = abs(topRight[0] - topLeft[0])
    h1 = abs(topRight[1] - bottomRight[1])
    h2 = abs(topLeft[1] - bottomLeft[1])
    minWidth = min([w1, w2])
    minHeight = min([h1, h2])
    
    pts2 = np.float32([[0, 0], [minWidth-1, 0], [minWidth-1, minHeight-1], [0, minHeight-1]])
    
    M = cv2.getPerspectiveTransform(pts1, pts2) # (변환당할 위치, 변환될 위치)
    '''
    AffineTransform : 원근 보정x, 
    PerspectiveTransform : 원근 보정o
    '''
    result = cv2.warpPerspective(img, M, (int(minWidth), int(minHeight)))
    
    cv2.imshow('original', img)
    cv2.imshow('Warp Transform', result)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    
if __name__ == '__main__':
    warpPerspective()

