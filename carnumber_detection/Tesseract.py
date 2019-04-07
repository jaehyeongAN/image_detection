# -*- coding: utf-8 -*- 
'''
Created on 2017. 8. 29.

@author: jaehyeong
'''
'''
# pytesseract 한글 사용
http://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-4.00.00dev.exe
다운받아서 설치할때, 추가 언어팩 체크
'''
from PIL import Image
import pytesseract

# tesseact 경로지정
tesseract_path = 'C:/Program Files (x86)/Tesseract-OCR'
pytesseract.pytesseract.tesseract_cmd = tesseract_path + '/tesseract.exe'

def ocr_tesseract():
    image_file = '../ch05_detection/scannedImage.png'
    im = Image.open(image_file)
    text = pytesseract.image_to_string(im,lang='kor')
    im.show()
    
    print(text)
    if text == '':
        print('null')
    
if __name__ == '__main__':
    ocr_tesseract()
    