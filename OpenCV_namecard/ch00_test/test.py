# -*- coding: utf-8 -*- 
'''
Created on 2017. 8. 28.

@author: jaehyeong
'''
#
import sys
import cv2
import pytesseract
from PIL import Image

# tesseact 경로지정
tesseract_path = 'C:/Program Files (x86)/Tesseract-OCR'
pytesseract.pytesseract.tesseract_cmd = tesseract_path + '/tesseract.exe'

print('python : ',sys.version)
print('opencv : ',cv2)
print('pytesseract : ',pytesseract.image_to_string(Image.open('../images/test.png')))

