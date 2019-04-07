import requests
from lxml.html import parse
from io import StringIO
import os

keyword = 'Car broken windshield'

urls = ['https://www.google.co.kr/search?q=Car+broken+windshield&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj38frRmaPVAhWDnZQKHYI0AZUQ_AUIBigB&biw=1920&bih=950',
        'https://www.google.co.kr/search?q=Car+broken+windshield&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj38frRmaPVAhWDnZQKHYI0AZUQ_AUIBigB&biw=1920&bih=950#q=Car+broken+windshield&hl=ko&tbm=isch&tbs=rimg:CZhVCAFSDtROIjjavn20plng9Hiqyw3KVKAIfpmeXRtCkl2wbT3mWe6VBaXhpBg99dIBW_1vY6u9JsRxpql8dExzNNioSCdq-fbSmWeD0EbccpMCweYbpKhIJeKrLDcpUoAgR6CXTduguXsgqEgl-mZ5dG0KSXRGB_1CT4jNJ5SCoSCbBtPeZZ7pUFEeMiQMegugBHKhIJpeGkGD310gER7wTtzrokwjkqEglb-9jq70mxHBFBeH2tFlqL-CoSCWmqXx0THM02ETMcIci7-TSE',
        'https://www.google.co.kr/search?q=Car+broken+windshield&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj38frRmaPVAhWDnZQKHYI0AZUQ_AUIBigB&biw=1920&bih=950#q=Car+broken+windshield&hl=ko&tbm=isch&tbs=rimg:CZTZcap3Cc-gIjgwO8jrDLZh0txwqbwGZBK_1JM_1ncBBiKXJh54G1gvVBHbzc5j6Zd6DckoLLKy1JV5wJvTy-sTOkpioSCTA7yOsMtmHSEY_1mepoJzFt3KhIJ3HCpvAZkEr8RExen9RYM7TMqEgkkz-dwEGIpchGbH70i2eJIYSoSCWHngbWC9UEdEYagvRgzQXUwKhIJvNzmPpl3oNwRyiedvIRC-uYqEgmSgssrLUlXnBFGQ_1pIymGexSoSCQm9PL6xM6SmEcaIp9qH-1Ag',
        'https://www.google.co.kr/search?q=Car+broken+windshield&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj38frRmaPVAhWDnZQKHYI0AZUQ_AUIBigB&biw=1920&bih=950#q=Car+broken+windshield&hl=ko&tbm=isch&tbs=rimg:Cf_1ArGtZ2BsoIjilqdkgDXau0D_1afnsKiiqZk37i5fVWVNsMZmNqOMVye1EMc7dl_12Wg8bFUzgKNVG_11gF4-dsKIFyoSCaWp2SANdq7QEWU96LLIYnUDKhIJP9p-ewqKKpkRLC20QoDTXBQqEgmTfuLl9VZU2xEX500FRv1tCSoSCQxmY2o4xXJ7ER1kfcVpsp05KhIJUQxzt2X_1ZaARoSRo0faNoYcqEgnxsVTOAo1UbxHlSYvjV6n5dioSCfWAXj52wogXEfQgckji5A4x',
        'https://www.google.co.kr/search?q=Car+broken+windshield&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj38frRmaPVAhWDnZQKHYI0AZUQ_AUIBigB&biw=1920&bih=950#q=Car+broken+windshield&hl=ko&tbm=isch&tbs=rimg:CRXGKZcZuLl_1IjiOI4WuopOoW_1vtSuz1XR9hd6gKJ2s82hioAIMy7UuHla7XO3lj11g3nVezKNfG-PHe6sbbg9-wjyoSCY4jha6ik6hbEQpCOqOK5Zf7KhIJ--1K7PVdH2ERb0I63N6FosQqEgl3qAonazzaGBFllj6cLfiZTyoSCagAgzLtS4eVEdzT4MY4HBUMKhIJrtc7eWPXWDcRTL2RYYL_1zh0qEgmdV7Mo18b48REedwfQ8Y7Q5SoSCd7qxtuD37CPEYLPa6dNon7T',
        'https://www.google.co.kr/search?q=Car+broken+windshield&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj38frRmaPVAhWDnZQKHYI0AZUQ_AUIBigB&biw=1920&bih=950#q=Car+broken+windshield&hl=ko&tbm=isch&tbs=rimg:CTRQTOOH_1VkdIjge3RO_12_1c3fyEmrhztNRwI2QHAWVDlRrBecl_1_1tsOY6lgYXCb_12R5KS0unmLbtHvMFJuvjuRHNsioSCR7dE7_1b9zd_1EfUEBiXl4WNSKhIJISauHO01HAgROXXLOJWrF0IqEgnZAcBZUOVGsBEaFNO3VPFMXSoSCV5yX_1-2w5jqEQfliqqbZqARKhIJWBhcJv_1ZHkoR1QsuOmlZFH0qEglLS6eYtu0e8xGtN_1TuKJNM0ioSCQUm6-O5Ec2yEdsH9K_1JE75P',
        'https://www.google.co.kr/search?q=car+front+crash&source=lnms&tbm=isch&sa=X&ved=0ahUKEwirwLaHq6PVAhUDybwKHSs0Dh8Q_AUIBigB&biw=958&bih=930&dpr=1#q=Car+broken+windshield&tbm=isch&tbs=rimg:CfZO16Dnrj6OIjg9DQ8DC2OH_10ZCQKHw5ge-PwtDusiUjNXSWVHLsgWTdghsO1_1wFla-Cc9kfBIU2u0w9gvewIA2pCoSCT0NDwMLY4f_1EXyIu1MM7bHvKhIJRkJAofDmB74RGalGcBq646MqEgk_1C0O6yJSM1RHGdUH554qoTSoSCdJZUcuyBZN2ETG4JAkiRoCQKhIJCGw7X_1AWVr4RZ_1GfLj6dFK0qEgkJz2R8EhTa7RHDME8UzpoF4yoSCTD2C97AgDakEXWjhQ60Iso8',
        'https://www.google.co.kr/search?q=car+front+crash&source=lnms&tbm=isch&sa=X&ved=0ahUKEwirwLaHq6PVAhUDybwKHSs0Dh8Q_AUIBigB&biw=958&bih=930&dpr=1#q=Car+broken+windshield&tbm=isch&tbs=rimg:CWg1HIMHAtX4Ijiryv4zs0QACwcgk1p5eP7vtclw_1A4iFum--crj8sAs0r9HU-uP74OV_1s8z0OwmRCcpeAI8ny6lZSoSCavK_1jOzRAALEYntw0_1sklmJKhIJByCTWnl4_1u8Ra2LIBT4wMcAqEgm1yXD8DiIW6RH1HoEA9bA5aioSCb75yuPywCzSEXoVnGC6YgzwKhIJv0dT64_1vg5URCVsVKvPtCAkqEgn-zzPQ7CZEJxEFNKV026OE_1SoSCSl4AjyfLqVlEUm2p1edhotE',
        'https://www.google.co.kr/search?q=Car+broken+windshield&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjD89vjrKPVAhXEHJQKHcaTCAMQ_AUIBigB&biw=958&bih=930#q=Car+broken+windshield&hl=ko&tbm=isch&tbs=rimg:CZJsLFl6f6MNIjgK5zvM2CUVLuZhZaUUoGb9oe3lSbwBCc6EqJZ1MR5Vc8WT1pUy99ASNqRldq-QrcT0lAIqHMMLYioSCQrnO8zYJRUuEZmMGDQL0kU7KhIJ5mFlpRSgZv0RRBIwhf78rM8qEgmh7eVJvAEJzhHVHUmQ70HGCioSCYSolnUxHlVzESbV5DcY1VSaKhIJxZPWlTL30BIRW_1unPOqLggoqEgk2pGV2r5CtxBEM3CxejwtK1CoSCfSUAiocwwtiEdm4zHjvHzQb',
        'https://www.google.co.kr/search?q=Car+broken+windshield&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjD89vjrKPVAhXEHJQKHcaTCAMQ_AUIBigB&biw=958&bih=930#q=Car+broken+windshield&hl=ko&tbm=isch&tbs=rimg:Ce4Ukkyr0NIRIjiKbPxO2C9X4SQfb3UUgwFY8iANwHfXoot6xlpuErmycandDAZ_1oTFi1oGyk8SBIiybrs6LPjuTaioSCYps_1E7YL1fhESs5Q4KtYsU4KhIJJB9vdRSDAVgRMNOHwEm-9nQqEgnyIA3Ad9eiixEb7RQF4x0PUCoSCXrGWm4SubJxEb1R9O7Sn74rKhIJqd0MBn-hMWIR_1eLC0cBziGcqEgnWgbKTxIEiLBFB51Wh8Zvh6SoSCZuuzos-O5NqEVoo8SXXUtpR'
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










