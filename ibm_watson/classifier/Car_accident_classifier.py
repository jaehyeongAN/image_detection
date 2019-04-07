'''
Created on 2017. 7. 20.

@author: jaehyeong
'''

import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3 as VisualRecognition 

# 버전과 api키 입력
visual_recognition = VisualRecognition('2016-05-20',
    api_key = '71f9767fb017656f628449b301fcfc81562265e4')

# Car accident classifier 생성(총 7개의 클래스)
with open(join(dirname(__file__), './images/Car front crash/Car front crash.zip'), 'rb') as Front_crash, \
        open(join(dirname(__file__), './images/Rear end crash/Rear end crash.zip'), 'rb') as Rear_end_crash, \
        open(join(dirname(__file__), './images/Car side crash/Car side crash.zip'), 'rb') as Side_crash, \
        open(join(dirname(__file__), './images/Car broken windshield/Car broken windshield.zip'), 'rb') as Broken_windshield, \
        open(join(dirname(__file__), './images/Car scratch/Car scratch.zip'), 'rb') as Scratch, \
        open(join(dirname(__file__), './images/Flat tire/Flat tire.zip'), 'rb') as Flat_tire, \
        open(join(dirname(__file__), './images/Overturned vehicle/Overturned vehicle.zip'), 'rb') as Overturned, \
      open(join(dirname(__file__), './images/Car/Car.zip'), 'rb') as Car:
    
    print(json.dumps(visual_recognition.create_classifier('Broken_Unbroken',    # 사용할 classifier
                                                          Front_crash_positive_examples=Front_crash,
                                                          Rear_end_crash_positive_examples=Rear_end_crash,
                                                          Side_crash_positive_examples=Side_crash,
                                                          Broken_windshield_positive_examples=Broken_windshield,
                                                          Scratch_positive_examples=Scratch,
                                                          Flat_tire_positive_examples=Flat_tire,
                                                          Overturned_positive_examples=Overturned,

                                                          negative_examples=Car), indent=2))

# 이미지 적용
with open(join(dirname(__file__), './rearend.jpg'), 'rb') as image_file:    # 적용할 이미지 파일 
    print(json.dumps(visual_recognition.classify(images_file=image_file, threshold=0,
    classifier_ids='Broken_Unbroken'), indent=2))       # 생성한 클래스 이름 지정 

 
# 현재 생성되있는 classifier 목록보기
print(json.dumps(visual_recognition.list_classifiers(), indent=2)) 

# 선택한 classifier 삭제하기
print(json.dumps(visual_recognition.delete_classifier(classifier_id='Broken_Unbroken_175697702'), indent=2))

