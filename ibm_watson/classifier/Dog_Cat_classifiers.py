'''
A new custom classifier can be trained by several compressed (.zip) files, 
including files containing positive or negative images (.jpg, or .png). 

You must supply at least two compressed files, 
either two positive example files or one positive and one negative example file.
'''

import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3 as VisualRecognition 

# 현재 version, api-key 입력
visual_recognition = VisualRecognition('2016-05-20',
    api_key = '71f9767fb017656f628449b301fcfc81562265e4')   # 버전은 무조건 2016-05-20, api키는 대괄호 없이!

'''
# Dog & Cat Classifier 생성
with open(join(dirname(__file__), './images/Dog/Dog.zip'), 'rb') as dog, \
      open(join(dirname(__file__), './images/Cat/Cat.zip'), 'rb') as cat:
   print(json.dumps(visual_recognition.create_classifier('Dog/Cat', dog_positive_examples=dog, negative_examples=cat), indent=2))
'''
'''
# 생성한 classifier 적용
with open(join(dirname(__file__), 'dog/dog45.jpg'), 'rb') as image_file:
    print(json.dumps(visual_recognition.classify(images_file=image_file, threshold=0,
    classifier_ids='DogxCat'), indent=2))
'''

# 현재 생성되있는 classifier 목록보기
print(json.dumps(visual_recognition.list_classifiers(), indent=2)) 

# 선택한 classifier 정보 보기
#print(json.dumps(visual_recognition.get_classifier('DogxCat_645197722'), indent=2))

# 선택한 classifier 삭제하기
print(json.dumps(visual_recognition.delete_classifier(classifier_id='DogxCat_1490224558'), indent=2))






