import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3 as VisualRecognition
from PIL import Image
import cv2

# 현재 version, api-key 입력
visual_recognition = VisualRecognition('2016-05-20',
    api_key = '71f9767fb017656f628449b301fcfc81562265e4')   # 버전은 무조건 2016-05-20, api키는 대괄호 없이!


#print(json.dumps(visual_recognition.detect_faces(images_url='http://pds.joins.com/news/component/ilgan_isplus/201705/27/2017052714361078300.jpeg'), indent=2))

info = json.dumps(visual_recognition.detect_faces(images_url='http://img.insight.co.kr/static/2017/12/31/700/it5m1l5fua35kv04050p.jpg'), indent=2)
print(info)
data = json.loads(info)

# 얼굴 위치 x,y,w,h
face_location = data['images'][0]['faces'][0]['face_location']

# 얼굴 부분만 자르기
def im_trim(img):
    x = face_location['left']
    y = face_location['top']
    w = face_location['width']
    h = face_location['height']
    
    crop_img = img[y:y+h,x:x+w]
    cv2.imshow('img',crop_img)
    cv2.waitKey(0)
    #cv2.imwrite('../images/crop_img.jpg',crop_img)
    
    return crop_img

from PIL import Image
img = cv2.imread('./images/test111.jpg')

im_trim(img)


