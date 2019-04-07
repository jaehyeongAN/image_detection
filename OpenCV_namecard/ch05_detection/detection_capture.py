# -*- coding: utf-8 -*- 
'''
Created on 2017. 8. 29.

@author: jaehyeong
'''
# 명함인식 구현하기 - 캡처된 이미지

import numpy as np
import cv2

def order_points(pts):
    # initialzie a list of coordinates that will be ordered
    # such that the first entry in the list is the top-left,
    # the second entry is the top-right, the third is the
    # bottom-right, and the fourth is the bottom-left
    rect = np.zeros((4, 2), dtype = "float32")

    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    # now, compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference\
    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    # return the ordered coordinates
    return rect

def auto_scan_image():
    # load the image and compute the ratio of the old height
    # to the new height, clone it, and resize it
    # document.jpg ~ docuemnt7.jpg
    image = cv2.imread('../images/carnumber.jpg')
    orig = image.copy()
    r = 800.0 / image.shape[0]
    dim = (int(image.shape[1] * r), 800)
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

    # convert the image to grayscale, blur it, and find edges in the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    edged = cv2.Canny(gray, 75, 200)

    # show the original image and the edge detected image
    print "STEP 1: Edge Detection"
    cv2.imshow("Image", image)
    cv2.imshow("Edged", edged)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    # find the contours in the edged image, keeping only the
    # largest ones, and initialize the screen contour
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]  # 외각이 그린 contour를  외각이 큰 순서대로 받아옴

    # loop over the contours
    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        # if our approximated contour has four points, then we
        # can assume that we have found our screen
        if len(approx) == 4:
            screenCnt = approx
            break
        # 즉. 찾아낸 외각 중 가장 큰 외각 순서대로 꼭지점이 4개를 찾아 냈을 때 그것을 외각으로 판단

    # show the contour (outline) of the piece of paper
    print "STEP 2: Find contours of paper"
    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
    cv2.imshow("Outline", image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    # apply the four point transform to obtain a top-down
    # view of the original image
    rect = order_points(screenCnt.reshape(4, 2) / r)
    (topLeft, topRight, bottomRight, bottomLeft) = rect
    
    w1 = abs(bottomRight[0] - bottomLeft[0])
    w2 = abs(topRight[0] - topLeft[0])
    h1 = abs(topRight[1] - bottomRight[1])
    h2 = abs(topLeft[1] - bottomLeft[1])
    maxWidth = max([w1, w2])
    maxHeight = max([h1, h2])
    
    dst = np.float32([[0,0], [maxWidth-1,0], 
                      [maxWidth-1,maxHeight-1], [0,maxHeight-1]])
    
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(orig, M, (maxWidth, maxHeight))

    # show the original and scanned images
    print "STEP 3: Apply perspective transform"
    cv2.imshow("Warped", warped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    # convert the warped image to grayscale, then threshold it
    # to give it that 'black and white' paper effect
    warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    warped = cv2.adaptiveThreshold(warped, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 10)
    
    # 이미지 크기 조정
    r = 150.0 / warped.shape[0]
    dim = (int(warped.shape[1] * r), 150)
    warped = cv2.resize(warped, dim, interpolation = cv2.INTER_AREA)
    
    # 번호판 부분만 자르기
    crop_img = warped[0:150, 50:700]
    
    # show the original and scanned images
    print "STEP 4: Apply Adaptive Threshold"
    cv2.imshow("Original", orig)
    cv2.imshow("Scanned", warped)
    cv2.imshow("crop img",crop_img)
    cv2.imwrite('scannedImage.png', crop_img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    
if __name__ == '__main__':
    auto_scan_image()
    