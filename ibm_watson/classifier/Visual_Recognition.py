
import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3 as VisualRecognition

# 현재 version, api-key 입력
visual_recognition = VisualRecognition('2016-05-20',
    api_key = '71f9767fb017656f628449b301fcfc81562265e4')   # 버전은 무조건 2016-05-20, api키는 대괄호 없이!

# json 형태로 분류 정보 출력
print(json.dumps(visual_recognition.classify(
    images_url='http://trumanlawfirm.com/wp-content/uploads/2013/07/Front-Crash.jpg'), indent=2))

'''
with open(join(dirname(__file__), './Dog/Dog10.jpg'), 'rb') as image_file:
    print(json.dumps(visual_recognition.classify(images_file=image_file, threshold=0,
    classifier_ids='Dog_Cat_1875776851'), indent=2))
'''

# 왜인지 image_url은 잘 인식하는데, image_file은 에러 뜸..
"""from PIL import Image
os.chdir('C:/Users/User/Downloads')
image = Image.open('ginni_bio_780x981_v4_03162016.jpg')
print(image)

print(json.dumps(visual_recognition.classify(images_file='C:/Users/User/Downloads/ginni_bio_780x981_v4_03162016.jpg'), indent=2))
"""
    