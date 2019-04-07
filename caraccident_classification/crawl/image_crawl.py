import requests
from lxml.html import parse
from io import StringIO
import os, sys
from PIL import Image


# 검색할 이미지의 키워드 입력
keyword = input("검색할 이미지를 입력하세요 : ")
url = 'https://www.google.co.kr/search?q='+keyword+'&source=lnms&tbm=isch&sa=X&ved=0ahUKEwic-taB9IXVAhWDHpQKHXOjC14Q_AUIBigB&biw=1842&bih=990'

 # html 소스 가져오기
text = requests.get(url, headers={'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}).text

# html 문서로 파싱
text_source = StringIO(text)
parsed = parse(text_source)

# root node 
doc = parsed.getroot()

# img 경로는 img 태그안에 src에 있음(20개만 크롤링 됨.. 이유 찾아봐야 됨)
imgs = doc.findall('.//img')

img_list = []   # 이미지 경로가 담길 list
for a in imgs:
    if a.get('data-src') == None:
            continue
    img_list.append(a.get('data-src'))
    #print(a.get('src'))

## 크롤링한 이미지 jpg파일로 저장 ##
import urllib.request

# 이미지 저장 경로지정
os.mkdir('D:/wise/dev/MachineLearning/CNN/'+keyword)   # 새 폴더 생성
os.chdir('D:/wise/dev/MachineLearning/CNN/'+keyword)   # 경로 설정

print("이미지 저장을 시작합니다~~~~~~~~~~~~~~~~~~~~~~~~~~")

cnt = 1
for urls in img_list:   
    print(urls)
    name = keyword
    full_name  = str(name) + str(cnt) + '.jpg'
    urllib.request.urlretrieve(str(urls), full_name)
    
    print(cnt,'번째 이미지 저장 성공')
    cnt += 1









