import requests
from lxml.html import parse
from io import StringIO
import os

keyword = 'Rear end crash'

urls = ['https://www.google.co.kr/search?q=Rear+end+crash&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjV0v2AuqHVAhWFjZQKHb90AtgQ_AUIBigB&biw=1920&bih=950',
        'https://www.google.co.kr/search?q=Rear+end+crash&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjV0v2AuqHVAhWFjZQKHb90AtgQ_AUIBigB&biw=1920&bih=950#q=Rear+end+crash&tbm=isch&tbs=rimg:CS-hDoQ-sKB7IjipzE5YZkJEn2coraQ3T2xzquCPEMzbXeCCTU_1Tw282Z8cOurixuc3z-EY34wiSHghTRPVP0sea4CoSCanMTlhmQkSfEZS5deH0Ni_1EKhIJZyitpDdPbHMRYqmZK3vz2qoqEgmq4I8QzNtd4BEEAsfhst1DdCoSCYJNT9PDbzZnEbN6X0yUubzvKhIJxw66uLG5zfMR36E-7uaQR34qEgn4RjfjCJIeCBGulqS8Vn0PqCoSCVNE9U_1Sx5rgEaqd4ivwjy1P',
        'https://www.google.co.kr/search?q=Rear+end+crash&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjV0v2AuqHVAhWFjZQKHb90AtgQ_AUIBigB&biw=1920&bih=950#q=Rear+end+crash&tbm=isch&tbs=rimg:CRbjjbiWEs7LIjhJlzgCtORvT6altuqt4rqN4Hz5Y9LUhD9Hi6XMXcc7SNHIax2F3Yt9zrULnUYY6NpWm_1lVjVp0fCoSCUmXOAK05G9PEZ3ntCHSRjzPKhIJpqW26q3iuo0ROyKL_1AO0P90qEgngfPlj0tSEPxGA2EPMaeMxYyoSCUeLpcxdxztIEcHUBOr4tOALKhIJ0chrHYXdi30RGiKhCZhHdLAqEgnOtQudRhjo2hGXXoB007JYoyoSCVab-VWNWnR8EQGBjyCs5jEu',
        'https://www.google.co.kr/search?q=Rear+end+crash&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjV0v2AuqHVAhWFjZQKHb90AtgQ_AUIBigB&biw=1920&bih=950#q=Rear+end+crash&tbm=isch&tbs=rimg:CYJNT9PDbzZnIjg4v5LM3Fp7RbnhEhFu9taPiatsmOTwkQyiGvnXeu175argjxDM213gPtQWQHqMKkDEXW2kVvQj6CoSCTi_1kszcWntFEYAgoezT_1veGKhIJueESEW721o8Rjqxk_1xownb4qEgmJq2yY5PCRDBFNiIffDKGcFSoSCaIa-dd67XvlEbLNfeDR95vqKhIJquCPEMzbXeARBALH4bLdQ3QqEgk-1BZAeowqQBGZcbB0pyLH_1yoSCcRdbaRW9CPoEXcvqHAbdR5F',
        'https://www.google.co.kr/search?q=Rear+end+crash&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjV0v2AuqHVAhWFjZQKHb90AtgQ_AUIBigB&biw=1920&bih=950#q=Rear+end+crash&tbm=isch&tbs=rimg:CZJR9d5LpJhIIjgSE55yJ9rnc8wZGHSqcPtCqqKTPw4_1y3mWM0M0d3T_1iCG6kwW9IFuIytEpVxkPOHVnqJdTPZ54TyoSCRITnnIn2udzEVA9dhMYNiKmKhIJzBkYdKpw-0IRMwtwYo709ToqEgmqopM_1Dj_1LeRGkcvxXU1VrQioSCZYzQzR3dP-IEfAL0zriRzuVKhIJIbqTBb0gW4gRmbuF1D5Z9YwqEgnK0SlXGQ84dRFswjofOjzoaioSCWeol1M9nnhPEZd2Suty-uyZ',
        'https://www.google.co.kr/search?q=Rear+end+crash&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjV0v2AuqHVAhWFjZQKHb90AtgQ_AUIBigB&biw=1920&bih=950#q=Rear+end+crash&tbm=isch&tbs=rimg:CcxBHC1xqdatIjhHs26AEosU-I6yXs28dzvkTy9RiuJ9vAxDhKz-UyjnjyODpc4SouJt3EQMnWtBGv2Q0zDKzvRTiCoSCUezboASixT4EcaEQnm4blemKhIJjrJezbx3O-QR8FsaoYTaXWkqEglPL1GK4n28DBGJxL4KzQtjaSoSCUOErP5TKOePEd9LIUGE2Cp0KhIJI4OlzhKi4m0RCbNQncoxPYEqEgncRAyda0Ea_1RF-_19gQbnKj0yoSCZDTMMrO9FOIEVvkvdD-aR6i',
        'https://www.google.co.kr/search?q=Car+rear-end+crash&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjz66mZraPVAhVHUrwKHQ5TBB8Q_AUIBigB&biw=958&bih=930#q=Car+rear-end+crash&hl=ko&tbm=isch&tbs=rimg:CamMHI5HuaivIjjxy1btOOdXUWF5gl6DOODfHCarzqvTtuKD5tneEigIhFP1nFYoq37WIoVkxPb4yfSU70OAKHP6TSoSCfHLVu0451dRET6uh5gDHoDpKhIJYXmCXoM44N8ROhJUHyYpOtsqEgkcJqvOq9O24hEcdjrerKhkWSoSCYPm2d4SKAiEEUqL8Fk2NrFiKhIJU_1WcViirftYRPM_1aTJaMMMIqEgkihWTE9vjJ9BFMMKEJ1nt12SoSCZTvQ4Aoc_1pNEUh7oXOruYcT',
        'https://www.google.co.kr/search?q=Car+rear-end+crash&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjz66mZraPVAhVHUrwKHQ5TBB8Q_AUIBigB&biw=958&bih=930#q=Car+rear-end+crash&hl=ko&tbm=isch&tbs=rimg:CcOUuVbXLqMbIjgNDdJeWlnqFtHIax2F3Yt9SHo1sBpLblYgAyU0D9d-Yy2kYpdRXpHNxH0ZjFp1A4M-1BZAeowqQCoSCQ0N0l5aWeoWET4IKwJFko5HKhIJ0chrHYXdi30RGiKhCZhHdLAqEglIejWwGktuVhGlLTW2ExZNoyoSCSADJTQP135jEfns1cMQT8kHKhIJLaRil1Fekc0Rj6eCs4KsSWkqEgnEfRmMWnUDgxF_1nOjbgWQ9syoSCT7UFkB6jCpAEZlxsHSnIsf_1',
        'https://www.google.co.kr/search?q=Car+rear-end+crash&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjz66mZraPVAhVHUrwKHQ5TBB8Q_AUIBigB&biw=958&bih=930#q=Car+rear-end+crash&hl=ko&tbm=isch&tbs=rimg:Cc_15HWO0aAZ_1Ijiid0Wc5ht5lOthm6Fbz7JOSH1DdeM8R1Pouem7bekOLpT6cGL1uRe0tzqq5uCw6ktLglTBDbi4-ioSCaJ3RZzmG3mUEdENLLFwlJ05KhIJ62GboVvPsk4R--fiuhq0lsIqEglIfUN14zxHUxFZGPtX3dhdWyoSCei56btt6Q4uEe-E4nZmjinFKhIJlPpwYvW5F7QRpxIoDfLhU2EqEgm3Oqrm4LDqSxHgveJfV1hQYSoSCUuCVMENuLj6EdENLLFwlJ05',
        'https://www.google.co.kr/search?q=Car+rear-end+crash&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjz66mZraPVAhVHUrwKHQ5TBB8Q_AUIBigB&biw=958&bih=930#q=Car+rear-end+crash&hl=ko&tbm=isch&tbs=rimg:CUDxnhc2mm9vIjgZlQZm2s8AaWxx3qfYAEhxSHo1sBpLblYwJV7UBY9r6ScrMmpvNH5h6FyQOKFKMy8AC8GXGjZKNyoSCRmVBmbazwBpERlfX-mLFvENKhIJbHHep9gASHERI-LkOPEU_1LgqEglIejWwGktuVhGlLTW2ExZNoyoSCTAlXtQFj2vpEY9xy11xy-btKhIJJysyam80fmERnHahEHDWYZkqEgnoXJA4oUozLxEmxCusgaAloSoSCQALwZcaNko3ESL3FWV7_116u'
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










