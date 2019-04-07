import requests
from lxml.html import parse
from io import StringIO
import os

keyword = 'Car front crash'

urls = ['https://www.google.co.kr/search?q=car+front+crash&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj_8O6ivKHVAhUNPrwKHa-XBHgQ_AUIBigB&biw=1920&bih=950',
       'https://www.google.co.kr/search?q=car+front+crash&hl=ko&site=webhp&source=lnms&tbm=isch#q=car+front+crash&hl=ko&tbm=isch&tbs=rimg:CQBnsn85DNKDIjjdAKupNNRpjTon7fejvvZuBnCTENCJ1sanq2kVKFA64Zs_16Bg-uRHRXjxEj2tGNRu1wQK2RvsW_1SoSCd0Aq6k01GmNEY0DnDWcJQRcKhIJOift96O-9m4RblPS1FD3RGkqEgkGcJMQ0InWxhEuboAV2DQCsSoSCaeraRUoUDrhEad6jBBYDfdvKhIJmz_1oGD65EdERCj61OAmg82cqEglePESPa0Y1GxHNBQ2O5cZK7ioSCbXBArZG-xb9EZsx3VyehtVj',
       'https://www.google.co.kr/search?q=car+front+crash&hl=ko&site=webhp&source=lnms&tbm=isch#q=car+front+crash&hl=ko&tbm=isch&tbs=rimg:CSoxb-JB4bKwIjgkyTSJxAPs4wpQY8zR914LcY0OApZVU4Q0gfsZNL_1P1jYBwOtPSHAWIgeLLtBO-CRrTcbbPcFT9SoSCSTJNInEA-zjEQqA7oDqGxiEKhIJClBjzNH3XgsRj5t-i6WoLfEqEglxjQ4CllVThBEKuMVwyjtd8SoSCTSB-xk0v8_1WESKT26gMoNzEKhIJNgHA609IcBYRMS25DXpXMoQqEgkiB4su0E74JBErGL_112zY9aCoSCWtNxts9wVP1EUvGxOKwT6kC',
       'https://www.google.co.kr/search?q=car+front+crash&hl=ko&site=webhp&source=lnms&tbm=isch#q=car+front+crash&hl=ko&tbm=isch&tbs=rimg:CTI_15g9KlS89IjgyaDWCkpTmFNJCeSdk0ZS053GV9KNuZ32MRNAdwmGBw9TgGHSm8XzEvQtJlVF1bRkaPIR9wa7U_1CoSCTJoNYKSlOYUEfqKgyDX_1yjoKhIJ0kJ5J2TRlLQR32YekUtKP74qEgnncZX0o25nfRHTq5sNiXig_1CoSCYxE0B3CYYHDEY1cZWgg4418KhIJ1OAYdKbxfMQROKVQbn55y_1QqEgm9C0mVUXVtGREjnmcPeFRy8yoSCRo8hH3BrtT8Ef-to066k9XN',
       'https://www.google.co.kr/search?q=car+front+crash&hl=ko&site=webhp&source=lnms&tbm=isch#q=car+front+crash&hl=ko&tbm=isch&tbs=rimg:CRbdNLWaEG1eIji2dggB0zAWgajYnU9_1YYwhDWvPkxHK7QynWJ5SnXhkbEvKHi_1SsQrDse6-PhNteIVmY2mmyegjrioSCbZ2CAHTMBaBEf5GlwNPZf-mKhIJqNidT39hjCERa4DymixUWuYqEgkNa8-TEcrtDBH71BATqTfVXSoSCadYnlKdeGRsEYhHDPuu05jgKhIJS8oeL9KxCsMREsuwBu9_1G64qEgmx7r4-E214hRGOeKbmsPC1ESoSCWZjaabJ6COuEUyl3qWKdaK7',
       'https://www.google.co.kr/search?q=car+front+crash&hl=ko&site=webhp&source=lnms&tbm=isch#q=car+front+crash&hl=ko&tbm=isch&tbs=rimg:CUKaS_1HcxtiRIjjdW4Q1RaHbuFA3SkhZxWDGaq3iHGZN396pIlPBklAS1wbFiJ2sOkjPgO8Mhv282uPBM44nkWVqMCoSCd1bhDVFodu4Ebtaag3rxubhKhIJUDdKSFnFYMYRMoHzsAgmDnwqEglqreIcZk3f3hGTVVDwV8nzYSoSCakiU8GSUBLXEfpP7oNQBoZGKhIJBsWInaw6SM8ROMbX42l4h6sqEgmA7wyG_1bza4xG50Ad0jNv64ioSCcEzjieRZWowEWUET_1SnPxf8',
       'https://www.google.co.kr/search?q=car+front+crash&source=lnms&tbm=isch&sa=X&ved=0ahUKEwirwLaHq6PVAhUDybwKHSs0Dh8Q_AUIBigB&biw=958&bih=930#q=car+front+crash&tbm=isch&tbs=rimg:CcHH9G2FBZwLIjhbYZbj7wsku420b43wvQ2AiZbzBogf9D3tZ0ZDiFrJ0LlEHFs3lKE3rLqxk_1veWjOYfeF2lLpQ2yoSCVthluPvCyS7Efc3j_1-A1TbRKhIJjbRvjfC9DYARiriR_1Gu3tBsqEgmJlvMGiB_10PREjfJarC_1XkFCoSCe1nRkOIWsnQEU0O0fmw-Z-OKhIJuUQcWzeUoTcRreP_1q3nahtsqEgmsurGT-95aMxEPif4uCE_1o8ioSCZh94XaUulDbEbf6zsr4K0LF',
       'https://www.google.co.kr/search?q=car+front+crash&source=lnms&tbm=isch&sa=X&ved=0ahUKEwirwLaHq6PVAhUDybwKHSs0Dh8Q_AUIBigB&biw=958&bih=930&dpr=1#q=car+front+crash&tbm=isch&tbs=rimg:CUsT6XXIN1ECIjiTVT-ZVOH39RxwcthJCK61Mj_1mD0qVLz1T2PFXM0gPrpSHAuIQGQ98P0Z6Gih1ogjtphqNL24tUioSCZNVP5lU4ff1EVIK687eYv2UKhIJHHBy2EkIrrURhAOP3pvroCUqEgkyP-YPSpUvPRESalx6QPrCryoSCVPY8VczSA-uEdiXlNNNWhfKKhIJlIcC4hAZD3wR6Z1rwKo9I4MqEgk_1RnoaKHWiCBEqnKRMZ8YpUyoSCe2mGo0vbi1SEY_1jr7lvh5v8',
       'https://www.google.co.kr/search?q=car+front+crash&source=lnms&tbm=isch&sa=X&ved=0ahUKEwirwLaHq6PVAhUDybwKHSs0Dh8Q_AUIBigB&biw=958&bih=930&dpr=1#q=car+front+crash&tbm=isch&tbs=rimg:CZSHAuIQGQ98IjjST1PbWvOgzJD82DIIW9tRAHtaare3JAaecPJfPHLf9-i-nKfnOjxHlU-b3X_1CnoV03IdRU_1CI3CoSCdJPU9ta86DMEYh8oxYxvgXiKhIJkPzYMghb21ERHzh_1BDjkqToqEgkAe1pqt7ckBhEGQd-ZaaFhKSoSCZ5w8l88ct_13EQH4sJj5IXoHKhIJ6L6cp-c6PEcRtAmJdCSd4iQqEgmVT5vdf8KehRHkJl2qbnBoVyoSCXTch1FT8IjcEZ8rm-a6IQp_1',
       'https://www.google.co.kr/search?q=car+front+crash&source=lnms&tbm=isch&sa=X&ved=0ahUKEwirwLaHq6PVAhUDybwKHSs0Dh8Q_AUIBigB&biw=958&bih=930&dpr=1#q=car+front+crash&tbm=isch&tbs=rimg:CeG4m98D_1K11IjjpHBAYIMhQzSeZyQlkoS9oAFvaR-q-h_1ocaNOGEAPstSlNRI6VkOjRdFVgTf0GrbpgKs0cuWVo9ioSCekcEBggyFDNERIXz4a-Ee-iKhIJJ5nJCWShL2gR3O3DaNAIiDEqEgkAW9pH6r6H-hFceOsyfaCutyoSCRxo04YQA-y1EaPNdnk5uKwVKhIJKU1EjpWQ6NERHDabS5HuRogqEgl0VWBN_1QatuhGmyEgJl_1g6oyoSCWAqzRy5ZWj2EWR254yaDc3C'
       ]

img_list = []   # 이미지 경로가 담길 list
for url in urls:
    
    # html 소스 가져오기
    text = requests.get(url, headers={'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}).text
    
    # html 문서로 파싱
    text_source = StringIO(text)
    parsed = parse(text_source)
    
    # root node 
    doc = parsed.getroot()
    
    # img 경로는 img 태그안에 src에 있음
    imgs = doc.findall('.//img')
    
    
    for a in imgs:
        if a.get('data-src') == None:
            continue
        img_list.append(a.get('data-src'))
    
'''
for li in img_list:
    print(li)
'''

## 크롤링한 이미지 jpg파일로 저장 ##
import urllib.request

# 이미지 저장 경로지정
os.mkdir('C:/dev/Python/workspace(pydev)/IBM_Watson/VR/'+keyword)   
os.chdir('C:/dev/Python/workspace(pydev)/IBM_Watson/VR/'+keyword)

print("######## 이미지 저장을 시작합니다 ########")
print("### 총 ",len(img_list),'개의 이미지 ###')

cnt = 1
for urls in img_list: 
    print(urls)
    name = keyword
    full_name  = str(name) + str(cnt) + '.jpg'
    urllib.request.urlretrieve(str(urls), full_name)
    
    print('## ',cnt,'번째 이미지 저장 성공')
    cnt += 1










