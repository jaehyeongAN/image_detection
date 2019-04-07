import requests
from lxml.html import parse
from io import StringIO
import os

keyword = 'Car'

urls = ['https://www.google.co.kr/search?q=Car&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj599Lw0aPVAhUFtpQKHZnxCqsQ_AUIBigB&biw=933&bih=930',
        'https://www.google.co.kr/search?q=Car&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj599Lw0aPVAhUFtpQKHZnxCqsQ_AUIBigB&biw=933&bih=930#q=Car&hl=ko&tbm=isch&tbs=rimg:CaBcwahqLgJiIji9j8TSDa2-IEngOXLVYos-X9xXCrwDuArAyluESF-b9AiHfEPsy7Quk0WA4ZrxYiPhoWErTcMrdioSCb2PxNINrb4gEZJ56CJajj72KhIJSeA5ctViiz4RIoNNPjE0uTkqEglf3FcKvAO4ChF4SNz5WztSpSoSCcDKW4RIX5v0EQvV3ObGO8ZWKhIJCId8Q-zLtC4R1xQmFEGCf18qEgmTRYDhmvFiIxEDNYr_1OEFR9ioSCeGhYStNwyt2EbLQ1ds8ZAPx',
        'https://www.google.co.kr/search?q=Car&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj599Lw0aPVAhUFtpQKHZnxCqsQ_AUIBigB&biw=933&bih=930#q=Car&hl=ko&tbm=isch&tbs=rimg:CcDKW4RIX5v0IjhdODfWo4hhx1Kigf3Q63QtE6xmxA_1J2KsT2RLdfH0DhDf6yZhaZFBIc2pNTNSJ2bLT2VYkqFeolioSCV04N9ajiGHHEZqIdAq3NoRLKhIJUqKB_1dDrdC0RJs7GnP-rWzAqEgkTrGbED8nYqxF5yH1NEiwkpyoSCRPZEt18fQOEEaeEZhL_14ZfBKhIJN_1rJmFpkUEgRJqsgJkjryk4qEglzak1M1InZshEK8KSfQ436NioSCdPZViSoV6iWESp3spdFpNi_1',
        'https://www.google.co.kr/search?q=Car&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj599Lw0aPVAhUFtpQKHZnxCqsQ_AUIBigB&biw=933&bih=930#q=Car&hl=ko&tbm=isch&tbs=rimg:CY7mpNgO9242IjiJkLVDq02u8SzJXUXu5cme9OvXtUcw0u8x3yDO8lTN0-qKpuhrQ4T-wgQg_1iIsQ90D23pudDmexioSCYmQtUOrTa7xEXsmAoTeyZB4KhIJLMldRe7lyZ4R8BohcGTWgwsqEgn069e1RzDS7xEW1-F0sfombioSCTHfIM7yVM3TEW2eW6yvjdHVKhIJ6oqm6GtDhP4Rl7eW6DAk3nIqEgnCBCD-IixD3RHXU0YE4ls5VioSCQPbem50OZ7GETjdj3vvh9dl',
        'https://www.google.co.kr/search?q=Car&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj599Lw0aPVAhUFtpQKHZnxCqsQ_AUIBigB&biw=933&bih=930#q=Car&hl=ko&tbm=isch&tbs=rimg:CYUxzdTwTpkdIjgfe4caduGEW7W2-y-FpRf3htTiD7yJOU_1w5UL1Pra6hPOPU3_1uX4WdxiZBdXNg4cOfX-sTRwTpaioSCR97hxp24YRbERwHYEv0q-jRKhIJtbb7L4WlF_1cR2CCB715aDtcqEgmG1OIPvIk5TxGgwxNsMsztFCoSCfDlQvU-trqEEflY7q2F8aqiKhIJ849Tf-5fhZ0R_17J4eDVDFjgqEgnGJkF1c2DhwxGrWKiwvZLKVioSCZ9f6xNHBOlqERL1-Qx3FA9P',
        'https://www.google.co.kr/search?q=Car&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj599Lw0aPVAhUFtpQKHZnxCqsQ_AUIBigB&biw=933&bih=930#q=Car&hl=ko&tbm=isch&tbs=rimg:CY_1SMKwy7Yf2IjjXK5I9Ibg9fuaDxunB0zTbXagYl_1_1zFGuWT3dzrrk-LvSKLuCT46qykBVaO6JWA17rieg79qU-DCoSCdcrkj0huD1-Ee5sAUfjk_1c7KhIJ5oPG6cHTNNsRQK_1gnCtuQWUqEgldqBiX_1_1MUaxFE2Pc-LwCQjSoSCZZPd3OuuT4uEXiZOjNGQfpmKhIJ9Iou4JPjqrIRzNN-wXGf164qEgmQFVo7olYDXhHdyfTJJKsjVCoSCeuJ6Dv2pT4MESIKFcFc73ol',
        'https://www.google.co.kr/search?q=Car&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj599Lw0aPVAhUFtpQKHZnxCqsQ_AUIBigB&biw=933&bih=930#q=Car&hl=ko&tbm=isch&tbs=rimg:CV4uTYIoOe3EIjjdAWjz18Nh5NR1G8KEjdEPSD9AnciVMCdElamxdIPeH6ESnKq7QueqsU4s7AteSY59c9l1Kf76MyoSCd0BaPPXw2HkEb5SP2FyOaopKhIJ1HUbwoSN0Q8RwBDJP-gK8h0qEglIP0CdyJUwJxHcxsiTRlmZ0CoSCUSVqbF0g94fEUOqIG8RdlZVKhIJoRKcqrtC56oRnR3OFZTlXTsqEgmxTizsC15JjhHyJ4Yqw5o27SoSCX1z2XUp_1vozEcsuqGiUi89e',
        'https://www.google.co.kr/search?q=Car&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj599Lw0aPVAhUFtpQKHZnxCqsQ_AUIBigB&biw=933&bih=930#q=Car&hl=ko&tbm=isch&tbs=rimg:CfcUIlUUbkR_1Ijjd6ndhLOUKFWldyz9jlPKr5bHJv2-caD42WPyuq5UjUwasciiG9HwlrEsizceQuwOoIasEST5fFyoSCd3qd2Es5QoVEWYQ2V8D4YGgKhIJaV3LP2OU8qsRzHf0p58jk6kqEgnlscm_1b5xoPhFsB2DAg8w0PioSCTZY_1K6rlSNTEWr8zTnLF-b_1KhIJBqxyKIb0fCURy1BZYB_1LCsMqEgmsSyLNx5C7AxFAIVz_18c2eXioSCaghqwRJPl8XEUQD40TNwvSW',
        'https://www.google.co.kr/search?q=Car&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj599Lw0aPVAhUFtpQKHZnxCqsQ_AUIBigB&biw=933&bih=930#q=Car&hl=ko&tbm=isch&tbs=rimg:CYEj3y0Gj8asIjixHaMhm9uIcixpvqQc31Togptab0ky6wAV4IETw4I_1J3upogpI-xaNqzuBDdaqrc21eMIDNSGNZyoSCbEdoyGb24hyEQl3x4oEFyMSKhIJLGm-pBzfVOgRSERlBWQVubYqEgmCm1pvSTLrABHdmTZAhozQqyoSCRXggRPDgj8nEXp1YE4f5jeWKhIJe6miCkj7Fo0REd-8TD8bamYqEgmrO4EN1qqtzRFUGmTzsZ_1heCoSCbV4wgM1IY1nES8V71I9Qouq',
        'https://www.google.co.kr/search?q=Car&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj599Lw0aPVAhUFtpQKHZnxCqsQ_AUIBigB&biw=933&bih=930#q=Car&hl=ko&tbm=isch&tbs=rimg:CUPpHdPEWx84IjhOo3RM6UD-Ae5vr97_12QbGGUESvAY-D8P5JRBWhNVz5pSl_16Ww4anaHxAAJ4YSkrnL0CiHp5_1AnSoSCU6jdEzpQP4BEWUueBk6GVi1KhIJ7m-v3v_1ZBsYRPZ2Uy17XixMqEgkZQRK8Bj4PwxFQEsfeZN3pVSoSCfklEFaE1XPmEaFiYGQvS7g0KhIJlKX_1pbDhqdoRWOQbg1MoknoqEgkfEAAnhhKSuRHageyCm0OD7SoSCcvQKIenn8CdEaTlxwc8ivdu']

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










