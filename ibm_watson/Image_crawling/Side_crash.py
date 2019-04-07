import requests
from lxml.html import parse
from io import StringIO
import os

keyword = 'Car side crash'

urls = ['https://www.google.co.kr/search?q=Car+side+crash&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiRyteHu6HVAhUDtpQKHUUFCTYQ_AUIBigB&biw=1920&bih=950',
        'https://www.google.co.kr/search?q=Car+side+crash&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiRyteHu6HVAhUDtpQKHUUFCTYQ_AUIBigB&biw=1920&bih=950#q=Car+side+crash&hl=ko&tbm=isch&tbs=rimg:CZy9QT0Yei4uIjgLTgSARWQm3rvhtByQTcSpCNWBinAYtcbr39C3hbNuADqflJUfMVAS5wG2jw5SksGYYyydSfJiQioSCQtOBIBFZCbeEX8ARKnDV8GYKhIJu-G0HJBNxKkRRHWPkK2OvE4qEgkI1YGKcBi1xhGI6MlmcGqk0yoSCevf0LeFs24AEba_1tio8qSaPKhIJOp-UlR8xUBIR-X73Hbb1mPgqEgnnAbaPDlKSwRFJsP4iZPcFqyoSCZhjLJ1J8mJCEdvh4IosdWF6',
        'https://www.google.co.kr/search?q=Car+side+crash&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiRyteHu6HVAhUDtpQKHUUFCTYQ_AUIBigB&biw=1920&bih=950#q=Car+side+crash&hl=ko&tbm=isch&tbs=rimg:CU0SDdNQBiAbIjhDXB16gc3tsPtv1bDWywVqQTCEmYY5TGyuAXYOR5U_1D3coMFqVR1DoNveX6mJ9bUda_1q8cMClC_1CoSCUNcHXqBze2wEXfcSQVU9DJYKhIJ-2_1VsNbLBWoRKQ2na05_15rwqEglBMISZhjlMbBH6lZ2l5Yx_1GioSCa4Bdg5HlT8PEUip_1s2ZTCgtKhIJdygwWpVHUOgR10Q6eRwEmHYqEgk295fqYn1tRxFxwy0D3HlkECoSCVr-rxwwKUL8EQaF8dmW6N4Z',
        'https://www.google.co.kr/search?q=Car+side+crash&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiRyteHu6HVAhUDtpQKHUUFCTYQ_AUIBigB&biw=1920&bih=950#q=Car+side+crash&hl=ko&tbm=isch&tbs=rimg:CbiD86fKS7oQIjja_1QWCFUTRHXvMx_1t4ShBBZ9OjUsQWRVspjJ1w4hYv5p-nf2y7G9mv3oX5FRVc4_1tdD8ZFwHBDTSoSCdr9BYIVRNEdEUQKK2pI0OWAKhIJe8zH-3hKEEERL2eDUhKhXHYqEgln06NSxBZFWxGldM7gEasTjCoSCSmMnXDiFi_1mEQY4eZXm8b88KhIJn6d_1bLsb2a8RHRUmf3NAfEwqEgnehfkVFVzj-xGz_1yIPY5oxVSoSCV0PxkXAcENNEUQs8ucelKRo',
        'https://www.google.co.kr/search?q=car+side+crash&hl=ko&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjujKHwu6HVAhUJhrwKHRppBdwQ_AUIBigB&biw=1920&bih=950&dpr=1#q=car+side+crash&hl=ko&tbm=isch&tbs=rimg:CX6o67XbihtWIjiFX2Di7BShRO7C4rW9VGc_1FAT2fBwadFFSGk6Y03FT5tqMbpTdD9kVdQKkfJMgnrJaQ_16bMLlG2CoSCYVfYOLsFKFEEVCJVKIrqztVKhIJ7sLitb1UZz8RYt0Cba3wRmwqEgkUBPZ8HBp0URGG1bDyx_1VpPioSCVIaTpjTcVPmEaPovGO7LhyPKhIJ2oxulN0P2RURdWTFZHN0Dz8qEgl1AqR8kyCeshFKcrfY1muzwioSCVpD_1pswuUbYEYQK0seJxcsW',
        'https://www.google.co.kr/search?q=car+side+crash&hl=ko&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjujKHwu6HVAhUJhrwKHRppBdwQ_AUIBigB&biw=1920&bih=950&dpr=1#q=car+side+crash&hl=ko&tbm=isch&tbs=rimg:CTtdKplqC4ENIjiiAhqDl2Mv4eeCRquttaNJG5d--6eD9SRqWjBKW1S8HP5yMSO7sA_1hy4CUeYvvEstK6KK96Hju4ioSCaICGoOXYy_1hETcervcshIn1KhIJ54JGq621o0kR4uHn2xAwXI8qEgkbl377p4P1JBEOwLRMMtx8tCoSCWpaMEpbVLwcERd520O35y1KKhIJ_1nIxI7uwD-ERev--dQVgN64qEgnLgJR5i-8SyxFZLCSCh2P1ISoSCUroor3oeO7iEbgHlQoxnjI_1',
        'https://www.google.co.kr/search?q=Car+rear-end+crash&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjz66mZraPVAhVHUrwKHQ5TBB8Q_AUIBigB&biw=958&bih=930#q=Car+side+crash&hl=ko&tbm=isch&tbs=rimg:CU0SDdNQBiAbIjhDXB16gc3tsPtv1bDWywVqQTCEmYY5TGyuAXYOR5U_1D3coMFqVR1DoNveX6mJ9bUda_1q8cMClC_1CoSCUNcHXqBze2wEXfcSQVU9DJYKhIJ-2_1VsNbLBWoRKQ2na05_15rwqEglBMISZhjlMbBH6lZ2l5Yx_1GioSCa4Bdg5HlT8PEUip_1s2ZTCgtKhIJdygwWpVHUOgR10Q6eRwEmHYqEgk295fqYn1tRxFxwy0D3HlkECoSCVr-rxwwKUL8EQaF8dmW6N4Z',
        'https://www.google.co.kr/search?q=Car+rear-end+crash&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjz66mZraPVAhVHUrwKHQ5TBB8Q_AUIBigB&biw=958&bih=930#q=Car+side+crash&hl=ko&tbm=isch&tbs=rimg:CaJvyG0PUsW-IjhUAxIFnWsr36ZAAg4-a8ZwzBkYdKpw-0JvLSMOYa4OBIiJ-movs5ZcYlgp1235gYZY4GiP6ilHoioSCVQDEgWdayvfEXeJmxkyiV1YKhIJpkACDj5rxnARD_1v_1loTXsDYqEgnMGRh0qnD7QhEzC3BijvT1OioSCW8tIw5hrg4EEYhD-jux_1k6ZKhIJiIn6ai-zllwRgPBWz54XI3EqEgliWCnXbfmBhhECWs6FhABcXSoSCVjgaI_1qKUeiEU0bm4E4Gfz0',
        'https://www.google.co.kr/search?q=Car+side+crash&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiDrP72raPVAhUCXrwKHdsoApoQ_AUIBigB&biw=958&bih=930#q=Car+side+crash&hl=ko&tbm=isch&tbs=rimg:CQt5CaE1C4E_1IjjnYWw9Y6izU4deOctcx119xCM6NLxLbufEjT18e_10w3BqY3eftLPuoc_1_19z1snANeSb43C-TIklCoSCedhbD1jqLNTER8yORMKLtlAKhIJh145y1zHXX0R-fvc83_1B3yYqEgnEIzo0vEtu5xE0hRwDkh_1fXCoSCcSNPXx7_1TDcEbS0CMpsJDoeKhIJGpjd5-0s-6gRmS-LvVpbEg8qEglz_1_13PWycA1xEoWu8QPEBuoSoSCZJvjcL5MiSUET60tbtVX7cP',
        'https://www.google.co.kr/search?q=Car+side+crash&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiDrP72raPVAhUCXrwKHdsoApoQ_AUIBigB&biw=958&bih=930#q=Car+side+crash&hl=ko&tbm=isch&tbs=rimg:CX_1IeIHNL-ZNIjhY4GiP6ilHouT5JxLpeuX4wd-KeX2esFbq3lnsZmfb7RqBSm8CP8_1lCNWBinAYtcaLdWBUD10XOioSCVjgaI_1qKUeiEU0bm4E4Gfz0KhIJ5PknEul65fgRaZ3ZaOczy8QqEgnB34p5fZ6wVhGcqHgpihWqwyoSCereWexmZ9vtETEenFd2CHGrKhIJGoFKbwI_1z-URzke6bdhFiHsqEgkI1YGKcBi1xhGI6MlmcGqk0yoSCYt1YFQPXRc6EVWu8JkKYMHj'
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










