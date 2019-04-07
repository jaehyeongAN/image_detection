import requests
from lxml.html import parse
from io import StringIO
import os

keyword = 'Flat tire'

urls = ['https://www.google.co.kr/search?q=flat+tire&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwihk5nJr6PVAhXHrJQKHR7bD7QQ_AUIBigB&biw=958&bih=930',
        'https://www.google.co.kr/search?q=flat+tire&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwihk5nJr6PVAhXHrJQKHR7bD7QQ_AUIBigB&biw=958&bih=930#q=flat+tire&hl=ko&tbm=isch&tbs=rimg:CfS27T3Odj57IjizqpC6uNfvo4TIc_1NlzbL9Ff275n1CnEo_1e6QRtsF1TmZSxikCNuiPs3yMZYZQJqZl0WOYiG7UHCoSCbOqkLq41--jEU9DIq-RjakaKhIJhMhz82XNsv0Rg2qY6yUa64sqEgkV_1bvmfUKcShEQAdB2ElzGdyoSCT97pBG2wXVOEXoG7lSbislQKhIJZlLGKQI26I8RP7tLC8JLfAcqEgmzfIxlhlAmphF9Mp6pccVJjCoSCWXRY5iIbtQcEYmIUuZ2sjDK',
        'https://www.google.co.kr/search?q=flat+tire&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwihk5nJr6PVAhXHrJQKHR7bD7QQ_AUIBigB&biw=958&bih=930#q=flat+tire&hl=ko&tbm=isch&tbs=rimg:CSsQCQqKFi1YIjgUoY-u8t1gRE-uIsm0_1USJ9geriyGhPLQG0AiCkj3maVUG7iT4TdF7GcBQDjHY3I3T8Mq5bnrN6SoSCRShj67y3WBEEazSJmen49unKhIJT64iybT9RIkR5q6PuczSZ4IqEgn2B6uLIaE8tBFf8lzdWfXuLioSCQbQCIKSPeZpEarSDaTPQq8yKhIJVQbuJPhN0XsRoZEkhEzRjvwqEgkZwFAOMdjcjRGCWCbtV8i1hioSCdPwyrlues3pESaKSw-3RsBJ',
        'https://www.google.co.kr/search?q=flat+tire&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwihk5nJr6PVAhXHrJQKHR7bD7QQ_AUIBigB&biw=958&bih=930#q=flat+tire&hl=ko&tbm=isch&tbs=rimg:CWEZOTi1uK7TIjhAsj0-QhQtAaGMtm6vrcpeJwug7vph6ALA4V4YBDq3JX8U8EFypk3OcUD9PsMX3tF-U-cEiQgUfioSCUCyPT5CFC0BEQuEAgv_1mbQXKhIJoYy2bq-tyl4RVqACDaoA2Y8qEgknC6Du-mHoAhEmJDQxC9fZKyoSCcDhXhgEOrclEW5xDiWqvgXFKhIJfxTwQXKmTc4R-KjnsPRBP5wqEglxQP0-wxfe0REkv7P3rHpityoSCX5T5wSJCBR-EVeYXjfFoWOK',
        'https://www.google.co.kr/search?q=flat+tire&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwihk5nJr6PVAhXHrJQKHR7bD7QQ_AUIBigB&biw=958&bih=930#q=flat+tire&hl=ko&tbm=isch&tbs=rimg:CTL5OeLOIYfFIjj89PMGjVqPl8luxfdcgmGnXOf3DjMP1ZbrQfVUccOYZ-KXdsi71uHN8CBI6DsQO4bk1tFd6-jTzCoSCfz08waNWo-XEeoeCRE5PoDCKhIJyW7F91yCYacRMNoOSYYUV-YqEglc5_1cOMw_1VlhG4LpnsNZWCPCoSCetB9VRxw5hnES4oqD8nETtqKhIJ4pd2yLvW4c0RgCD6me12g5YqEgnwIEjoOxA7hhGKWOJ231ViIioSCeTW0V3r6NPMEZwY5F4chQCK',
        'https://www.google.co.kr/search?q=flat+tire&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwihk5nJr6PVAhXHrJQKHR7bD7QQ_AUIBigB&biw=958&bih=930#q=flat+tire&hl=ko&tbm=isch&tbs=rimg:CWvkbqfOdkWgIjgdOdmECwnenWRGG-Uqcf0HroClusf8hvtjT3YSn2ErWPe1e7sHtfNuspVJlWJ1nySSyduXwbQN5ioSCR052YQLCd6dEc-n6OZ8LKMQKhIJZEYb5Spx_1QcRO0n7DD8rT0MqEgmugKW6x_1yG-xHBlvIae1A92CoSCWNPdhKfYStYEcSNWmdfblyiKhIJ97V7uwe1824R3sf0wFD7JbgqEgmylUmVYnWfJBHYZzYEe522MioSCZLJ25fBtA3mEcOvxiwO6fKy',
        'https://www.google.co.kr/search?q=flat+tire&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwihk5nJr6PVAhXHrJQKHR7bD7QQ_AUIBigB&biw=958&bih=930#q=flat+tire&hl=ko&tbm=isch&tbs=rimg:CRg-uFgMqKtVIjgqn1m_1M5RVVSFvRKUyQYbyqLHvSLgC3gVhsoeziLf5bip6LSe-OKIy5_16pyqbXNZsueZNxAhXmuCoSCSqfWb8zlFVVEbdGP_17FrKpRKhIJIW9EpTJBhvIRSG4l0ccY8Z4qEgmose9IuALeBREAhwyTVQblZioSCWGyh7OIt_1luEYl21tnEwC2HKhIJKnotJ744ojIRzKwO8IVyXVIqEgnn_1qnKptc1mxG6a-M8TSQvcCoSCS55k3ECFea4EaKlQoCuZoNY',
        'https://www.google.co.kr/search?q=flat+tire&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwihk5nJr6PVAhXHrJQKHR7bD7QQ_AUIBigB&biw=958&bih=930#q=flat+tire&hl=ko&tbm=isch&tbs=rimg:Cd0IeBL8m2bSIjjj9CFSvQhGXII8gIMOJjSCl-IBI0IDZxGZQly_1WvswNdcAJdatVCW2HFalmZDBMMofn9GNpX-lVCoSCeP0IVK9CEZcEXKXrTvhi_1BpKhIJgjyAgw4mNIIRxKQ-UbJMhbwqEgmX4gEjQgNnERGD_134drlVHYyoSCZlCXL9a-zA1EfnWAEs4PxSrKhIJ1wAl1q1UJbYRU1h8Iz9UxkUqEgkcVqWZkMEwyhFVRHeBdakTdioSCR-f0Y2lf6VUEVxnbB0nnQdY',
        'https://www.google.co.kr/search?q=flat+tire&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwihk5nJr6PVAhXHrJQKHR7bD7QQ_AUIBigB&biw=958&bih=930#q=flat+tire&hl=ko&tbm=isch&tbs=rimg:CdDgWXXd2xOhIjiNmwUbdqYE6MgWyBeoiB4ZyzbvYkP6_1r69327r31MQSLqw6ZjcQ3rHO5_1bk7HLcdNojst7Go-sMyoSCY2bBRt2pgToEVlnXpS47jq4KhIJyBbIF6iIHhkRjsEmYpAy2HUqEgnLNu9iQ_1r-vhFmS5tYaY3loSoSCb3fbuvfUxBIESMxaipI4wC1KhIJurDpmNxDescREssg_1r_18p-IqEgk7n9uTsctx0xEH0Ti99PerFCoSCWiOy3saj6wzEdxWbN0DbaRW',
        'https://www.google.co.kr/search?q=flat+tire&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwihk5nJr6PVAhXHrJQKHR7bD7QQ_AUIBigB&biw=958&bih=930#q=flat+tire&hl=ko&tbm=isch&tbs=rimg:CQ8SGZJwGp0eIjgAaAsvkZ4eZR-CLJHFzOdpvZO4zIGKAxCp7W4w6rK6FN0ALui64TEbs2Ox0dnYKsp-uGbf7M93PioSCQBoCy-Rnh5lEUkBBgFuyOUnKhIJH4IskcXM52kRiJGTKiZVmxQqEgm9k7jMgYoDEBEKvMVn3rFRhioSCantbjDqsroUEUdaUGUObdlUKhIJ3QAu6LrhMRsRFC_1AvOxIlV8qEgmzY7HR2dgqyhFMuiFtFonYXyoSCX64Zt_1sz3c-EekYuGn2j8Y9'
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










