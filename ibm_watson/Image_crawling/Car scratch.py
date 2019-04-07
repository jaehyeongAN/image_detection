import requests
from lxml.html import parse
from io import StringIO
import os

keyword = 'Car scratch'

urls = ['https://www.google.co.kr/search?q=Car+scratch&source=lnms&tbm=isch&sa=X&ved=0ahUKEwijlOv8xKPVAhWKnZQKHbEYBEQQ_AUIBigB&biw=958&bih=930',
        'https://www.google.co.kr/search?q=Car+scratch&source=lnms&tbm=isch&sa=X&ved=0ahUKEwijlOv8xKPVAhWKnZQKHbEYBEQQ_AUIBigB&biw=958&bih=930#q=Car+scratch&tbm=isch&tbs=rimg:Ce4gZywCKZrpIjhb6JooMRUcbw8wqr7n-rV_1s_1cjnioddVM-MNuuFJj4zyQFSWzJr0xcMKd2l57Sei33ow3vSA5lICoSCVvomigxFRxvESDAyzuMepVgKhIJDzCqvuf6tX8RirrORYvRx04qEgmz9yOeKh11UxFO3PcnkNaEEioSCT4w264UmPjPEZuuXhyCn_1yXKhIJJAVJbMmvTFwRsWbnLDjEbx4qEgkwp3aXntJ6LRFc42NWIKpDvyoSCfejDe9IDmUgEa5QRU2GdefK',
        'https://www.google.co.kr/search?q=Car+scratch&source=lnms&tbm=isch&sa=X&ved=0ahUKEwijlOv8xKPVAhWKnZQKHbEYBEQQ_AUIBigB&biw=958&bih=930#q=Car+scratch&tbm=isch&tbs=rimg:CYdjm6clZoeeIjjzcbomm7frqrUD0DU4xtmVr8PDetcUrBDVTNb-oX_18klJ7izxTuWwo7BUupHXYI3wMKn6Kw1Q9xSoSCfNxuiabt-uqES2XuJ7HYmtCKhIJtQPQNTjG2ZURD2cHi_1B4U9oqEgmvw8N61xSsEBHMNb9IobCS1yoSCdVM1v6hf_1ySEcl0-SlSx7POKhIJUnuLPFO5bCgRwtXPDbJQI40qEgnsFS6kddgjfBE-pcIJLhYLfyoSCQwqforDVD3FETX3OG_1Ci-oJ',
        'https://www.google.co.kr/search?q=Car+scratch&source=lnms&tbm=isch&sa=X&ved=0ahUKEwijlOv8xKPVAhWKnZQKHbEYBEQQ_AUIBigB&biw=958&bih=930#q=Car+scratch&tbm=isch&tbs=rimg:CTATzewHllGOIjiJH5FR4SdFOD62dkN9-miC2TLbSou3NHoq2xE5MeMeTeIxd9ecMv9_1MKJWuJVZLTvHDnXUT9FWkyoSCYkfkVHhJ0U4EaCcQuzq3AnnKhIJPrZ2Q336aIIRO_1OpkNPF_1-YqEgnZMttKi7c0ehGd3CEIkRMnQCoSCSrbETkx4x5NEQkYkNQXhZQ1KhIJ4jF315wy_138R6Rwg5DjwiHkqEgkwola4lVktOxHU6f6Hg3jpiCoSCccOddRP0VaTEaaqFyxsRiCq',
        'https://www.google.co.kr/search?q=Car+scratch&source=lnms&tbm=isch&sa=X&ved=0ahUKEwijlOv8xKPVAhWKnZQKHbEYBEQQ_AUIBigB&biw=958&bih=930#q=Car+scratch&tbm=isch&tbs=rimg:CfJf722dMinJIji6hT4QtHNrRXXvZ9_1MDUI9EWW3ekq0vEasH9iTd8N9f4LOMKA0CuArxVtWG_1h78dJHcyhmd2Wl3CoSCbqFPhC0c2tFEcSO_1-TjxIrzKhIJde9n38wNQj0RDQsssWDh8rAqEgkRZbd6SrS8RhFKYdCMoGsRUSoSCawf2JN3w31_1Ecx-UXKs7V_14KhIJgs4woDQK4CsRNeTZWor6P-EqEgnFW1Yb-Hvx0hH-1qx9rIINKioSCUdzKGZ3ZaXcESpplb_1ZHQ7P',
        'https://www.google.co.kr/search?q=Car+scratch&source=lnms&tbm=isch&sa=X&ved=0ahUKEwijlOv8xKPVAhWKnZQKHbEYBEQQ_AUIBigB&biw=958&bih=930#q=Car+scratch&tbm=isch&tbs=rimg:CX85p4szpj8AIjhvjcx8beTdhMKJ27sEJ09qlrLf1HegoclAL0ABSCbwXBKCMbVXieY2JX2I2vbm5cNhSVhsuZc8xSoSCW-NzHxt5N2EEVWH5SLK64a1KhIJwonbuwQnT2oRITFCs6KCDV8qEgmWst_1Ud6ChyRHfVjkN59Va3ioSCUAvQAFIJvBcEb_1R8XeFBaKVKhIJEoIxtVeJ5jYREtzCSrpNVbgqEgklfYja9ublwxEW3TNV6ChSWyoSCWFJWGy5lzzFERLcwkq6TVW4',
        'https://www.google.co.kr/search?q=Car+scratch&source=lnms&tbm=isch&sa=X&ved=0ahUKEwijlOv8xKPVAhWKnZQKHbEYBEQQ_AUIBigB&biw=958&bih=930#q=Car+scratch&tbm=isch&tbs=rimg:CcD4my6KIegkIjh9_1T8mowZpkzW-AP7NpwnM3uOGXskdSpDgoHdNvUZMaWUBVZo8kz0z8l_1vbZ0yKclNSeugSOPbVCoSCX39PyajBmmTEd_1UE2mdGYQVKhIJNb4A_1s2nCcwRdlQ0CT2vFx4qEgne44ZeyR1KkBEC8e1sU6RAKioSCeCgd029RkxpEfOPEwXF-qzpKhIJZQFVmjyTPTMRK1Jqntmd_1C8qEgnyX-9tnTIpyRE8ZFEWXEulWioSCU1J66BI49tUEdBd9_1oH84Qt',
        'https://www.google.co.kr/search?q=Car+scratch&source=lnms&tbm=isch&sa=X&ved=0ahUKEwijlOv8xKPVAhWKnZQKHbEYBEQQ_AUIBigB&biw=958&bih=930#q=Car+scratch&tbm=isch&tbs=rimg:Cbs5_1sr85xi3IjiQdZrpRPTLZe0cmeHKTOW_12qK7G6UbQVUUdobWfpWVvQzhrl4CuryC7d3hPbB5oMGOZZYTUBZkrioSCZB1mulE9MtlEV8l97F-NNa4KhIJ7RyZ4cpM5b8RbBjUJbxXm44qEgnaorsbpRtBVRFsJpTNKo_18HioSCRR2htZ-lZW9EWRaGKamFyYyKhIJDOGuXgK6vIIRsPLckpXvRwIqEgnt3eE9sHmgwREqT7Mq4kdgmSoSCY5llhNQFmSuETjk2IbzdJlo',
        'https://www.google.co.kr/search?q=Car+scratch&source=lnms&tbm=isch&sa=X&ved=0ahUKEwijlOv8xKPVAhWKnZQKHbEYBEQQ_AUIBigB&biw=958&bih=930#q=Car+scratch&tbm=isch&tbs=rimg:CSWzGExE7H6AIjiWZXS6wyEBsjSRHyZ-SdJ18Ni0HwMBHi2Tq4EnmmvATmr6UPYrZqcU30T-ZQPT41iFbksZfZI1QSoSCZZldLrDIQGyEUaBs_1Y0lQAFKhIJNJEfJn5J0nUR0slDrrDLyOwqEgnw2LQfAwEeLRFpCYSgyvX0BSoSCZOrgSeaa8BOEXmsuWaUWFNUKhIJavpQ9itmpxQRDVmo4AoBEqEqEgnfRP5lA9PjWBFplWG1shASFCoSCYVuSxl9kjVBEbc47eBIVydG',
        'https://www.google.co.kr/search?q=Car+scratch&source=lnms&tbm=isch&sa=X&ved=0ahUKEwijlOv8xKPVAhWKnZQKHbEYBEQQ_AUIBigB&biw=958&bih=930#q=Car+scratch&tbm=isch&tbs=rimg:CYVcN1pmT6xnIjh3HLZJyV-QmvFLOQCrtLQ8z_135Ua_1b-SoLk9EvUvO8iBTeL4QOcXKgv7c--i3s3UdyuMAzl1GRcyoSCXcctknJX5CaEal4tRGcE2BlKhIJ8Us5AKu0tDwReTRrHDuWgYoqEgnP_1flRr9v5KhGQe4ZG63Vd3SoSCQuT0S9S87yIETVm6E2z2dOhKhIJFN4vhA5xcqARWZcur_1iiwiYqEgm_1tz76LezdRxGpeLURnBNgZSoSCXK4wDOXUZFzEUlUiEL76OkE'
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


