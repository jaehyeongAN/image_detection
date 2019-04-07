# -*- coding: utf-8 -*- 
'''
Created on 2017. 8. 29.

@author: jaehyeong
'''
# http://projectoxford.ai에서 가입 후 free key 받기
# OCR - Project Oxford by MS

from PIL import Image
import httplib, urllib, base64, json

def print_text(json_data):
    result = json.loads(json_data)
    for l in result['regions']:
        for w in l['lines']:
            line = []
            for r in w['words']:
                line.append(r['text'])
            print ' '.join(line)
    return

def ocr_project_oxford(headers, params, data):
    conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v1.0/ocr?%s" % params, data, headers=headers)
    response = conn.getresponse()
    data = response.read()
    print data + "\n"
    print_text(data)
    conn.close()
    return
    
if __name__ == '__main__':
    headers = {
        # Request headers
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': '133a842327f1420cbae21067b5060a6f',    # project oxford 인증키 입력(1분에 20번, 한달에 5000번 제한)
    }
    params = urllib.urlencode({
        # Request parameters
        'language': 'ko',   # 'unk' : 알아서 언어를 인식
        'detectOrientation ': 'True',   # 글자의 각도까지 감지
    })
    data = open('../ch05_detection/scannedImage.png', 'rb').read()
    
    try:
        image_file = '../ch05_detection/scannedImage.png'
        im = Image.open(image_file)
        im.show()
        ocr_project_oxford(headers, params, data)
    except Exception as e:
        print(e)
