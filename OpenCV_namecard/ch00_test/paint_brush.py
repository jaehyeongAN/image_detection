# -*- coding: utf-8 -*- 
'''
Created on 2017. 12. 29.

@author: jaehyeong
'''
import cv2
import numpy as np

cv2.useOptimized()

drawing = False
eraser = False
mode = False
ix, iy = -1, -1

# mouse callback function
def draw_circle(event, x, y, flags, param):
    global ix, iy, eraser, drawing, mode
    
    e1 = cv2.getTickCount()
    
    # drawing
    if event == cv2.EVENT_LBUTTONDOWN:  # left button
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(255,255,255),-1)
            else:
                cv2.circle(img,(x,y),5,(255,255,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(255,255,255),-1)
        else:
            cv2.circle(img,(x,y),5,(255,255,255),-1)
    
    # erasing
    if event == cv2.EVENT_RBUTTONDOWN:  # right button
        eraser = True
        ix, iy = x,y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if eraser == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,0,0),-1)
            else:
                cv2.circle(img,(x,y),10,(0,0,0),-1)
                
    elif event == cv2.EVENT_RBUTTONUP:
        eraser = False
        if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,0,0),-1)
        else:
            cv2.circle(img,(x,y),10,(0,0,0),-1)        
            
    e2 = cv2.getTickCount()
    t = (e2 - e1)/cv2.getTickFrequency()
    print 'performance: ',t

img = np.zeros((850,1020,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()