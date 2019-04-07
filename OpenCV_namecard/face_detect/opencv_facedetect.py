# -*- coding: utf-8 -*- 
import cv2
import sys
from PIL import Image

# 이미지 읽어 들이기
image = cv2.imread("./img/a5.jpg")
# 그레이스케일로 변환하기
image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 얼굴 인식 특징 파일 읽어 들이기 
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# 얼굴 인식 실행하기
face_list = cascade.detectMultiScale(image_gs,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(100, 100), maxSize=(1000,1000))

if len(face_list) > 0:
    # 인식한 부분 표시하기 
    print(face_list)
    color = (0, 0, 255)
    for face in face_list:
        x,y,w,h = face
        cv2.rectangle(image, (x,y), (x+w, y+h), color, thickness=8)
        face_location = cv2.rectangle(image, (x,y), (x+w, y+h), color, thickness=8)
        break
    
    # 파일로 출력하기
    #cv2.imwrite("output.PNG", image)
    cv2.imshow('image',image)
    cv2.waitKey(0)
    
    crop_img = image[y:y+h,x:x+w]
    cv2.imshow('crop_img',crop_img)
    cv2.waitKey(0)
    
    cv2.imwrite('face_output.png',crop_img)
    
else:
    print("no face")
