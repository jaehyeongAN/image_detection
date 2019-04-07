import requests
from lxml.html import parse
from io import StringIO
import os

keyword = 'Overturned vehicle'

urls = ['https://www.google.co.kr/search?q=Overturned+vehicle&hl=ko&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiP9fq-x6PVAhULx7wKHdtUBgUQ_AUIBigB&biw=936&bih=930&dpr=1',
        'https://www.google.co.kr/search?q=Overturned+vehicle&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwigl7qDyKPVAhVChrwKHf2SDbAQ_AUIBigB&biw=1920&bih=950#q=Overturned+vehicle&hl=ko&tbm=isch&tbs=rimg:CR7C2Irp5fFTIjjVX8HWONeV7SQatP-I_1vIjU_12_12XLOycSYfzGXlnprKNKryljG0Yw9EFKElmlaxmzwwNprNXZOzSoSCdVfwdY415XtEbnnl0I4jgQZKhIJJBq0_14j-8iMR-nxbZti3OrwqEglT_1b_1Zcs7JxBGfMqbU9GpXKyoSCZh_1MZeWemsoEbnnl0I4jgQZKhIJ0qvKWMbRjD0RPL5gwk0PcpIqEgkQUoSWaVrGbBHa8znM02gtwCoSCfDA2ms1dk7NESeXFQ5GYo7F',
        'https://www.google.co.kr/search?q=Overturned+vehicle&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwigl7qDyKPVAhVChrwKHf2SDbAQ_AUIBigB&biw=1920&bih=950#q=Overturned+vehicle&hl=ko&tbm=isch&tbs=rimg:CT5AhZRoIrapIjh4NrhWHReJv41O-76GFAYOlYZsbpWhHTEakQm9NAtfw28UwISg20SgxFP1QEIltp-x9A4qeTpbZyoSCXg2uFYdF4m_1EXlrtS04b-YgKhIJjU77voYUBg4RLBnJWxde92sqEgmVhmxulaEdMRE3UYZzBRoGGSoSCRqRCb00C1_1DEcXjrMtEmjEkKhIJbxTAhKDbRKARFHeYf9iCFi4qEgnEU_1VAQiW2nxHrXsQIF316gyoSCbH0Dip5OltnEYtsQNgy8FfT',
        'https://www.google.co.kr/search?q=Overturned+vehicle&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwigl7qDyKPVAhVChrwKHf2SDbAQ_AUIBigB&biw=1920&bih=950#q=Overturned+vehicle&hl=ko&tbm=isch&tbs=rimg:CRBShJZpWsZsIjji608b_11L1t2p46S16ulgtIQJaWbdkKo3kb7YQ07gCs1ojgHbnf6pl2z8N-jOAARv-OQ82qaqooCoSCeLrTxv_1UvW3EUvCEwNw1vEiKhIJanjpLXq6WC0RrcGbEhqQAKgqEgkhAlpZt2QqjRGGP79CGz_14nioSCeRvthDTuAKzEVqiSWDOaZh1KhIJWiOAdud_1qmURsra99RFK5VAqEgnbPw36M4ABGxE1ON-QKeSIryoSCf45DzapqqigEXnINsEIFV7H',
        'https://www.google.co.kr/search?q=Overturned+vehicle&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwigl7qDyKPVAhVChrwKHf2SDbAQ_AUIBigB&biw=1920&bih=950#q=Overturned+vehicle&hl=ko&tbm=isch&tbs=rimg:CSXfpUwcpSxXIjg8O0p7CmVl4Veu-Ib5viQaXK8erz6MEBPEU_1VAQiW2n1vMbNIg6sMHeiVDE_1OPyvJwDScSgeGfSSoSCTw7SnsKZWXhEbPGzGS6-_1_1xKhIJV674hvm-JBoRwfAoUea7km8qEglcrx6vPowQExEY67vI3lCTGyoSCcRT9UBCJbafEetexAgXfXqDKhIJW8xs0iDqwwcRQZLtcQi-yZAqEgl6JUMT84_1K8hG555dCOI4EGSoSCXANJxKB4Z9JEaUmqw_1r8p78',
        'https://www.google.co.kr/search?q=Overturned+vehicle&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwigl7qDyKPVAhVChrwKHf2SDbAQ_AUIBigB&biw=1920&bih=950#q=Overturned+vehicle&hl=ko&tbm=isch&tbs=rimg:CUPKAZYKA97JIjjj3f8JLRAbaNVfwdY415Xt0FYKe6bBXOzVJNHAss-hZ-76iPo3WKUpU_12_12XLOycSs17YWrbBslyoSCePd_1wktEBtoERb7hUnk5JGRKhIJ1V_1B1jjXle0RueeXQjiOBBkqEgnQVgp7psFc7BGI7eTnwyIdryoSCdUk0cCyz6FnESmZT6kGLNJ1KhIJ7vqI-jdYpSkRMl58WdZH66sqEglT_1b_1Zcs7JxBGfMqbU9GpXKyoSCazXthatsGyXEVEDtzA6n7ze',
        'https://www.google.co.kr/search?q=Overturned+vehicle&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwigl7qDyKPVAhVChrwKHf2SDbAQ_AUIBigB&biw=1920&bih=950#q=Overturned+vehicle&hl=ko&tbm=isch&tbs=rimg:Cfv5xIoA9v4fIjgUnNKLjN9kcuLrTxv_1UvW3d4hcmRmF1y47P8SZ2qeuOMmuwgKsCCiBfGElcXdAPAyYfzGXlnprKCoSCRSc0ouM32RyEaEndAIA408DKhIJ4utPG_19S9bcRS8ITA3DW8SIqEgl3iFyZGYXXLhFenxSC8nH64ioSCTs_1xJnap644EZCeK9meAERFKhIJya7CAqwIKIERnIW7NZMC0HMqEgl8YSVxd0A8DBG555dCOI4EGSoSCZh_1MZeWemsoEbnnl0I4jgQZ',
        'https://www.google.co.kr/search?q=Overturned+vehicle&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwigl7qDyKPVAhVChrwKHf2SDbAQ_AUIBigB&biw=1920&bih=950#q=Overturned+vehicle&hl=ko&tbm=isch&tbs=rimg:CcYNAuf847Q2IjhI0VCfunlrlobg5J2SvnPQDaB3ApAtFyeT_11LNcqmcAdVfwdY415XtYtUPH-PdQHCwMCgXiNaSZSoSCUjRUJ-6eWuWEXwKZgv0UfqTKhIJhuDknZK-c9AR2jv7jS32BvUqEgkNoHcCkC0XJxGuIiqoaKAscioSCZP_1Us1yqZwBEbtEhD_1iG533KhIJ1V_1B1jjXle0RueeXQjiOBBkqEgli1Q8f491AcBFbvBhAc9nvGioSCbAwKBeI1pJlEejhPyM2UwQr',
        'https://www.google.co.kr/search?q=Overturned+vehicle&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwigl7qDyKPVAhVChrwKHf2SDbAQ_AUIBigB&biw=1920&bih=950#q=Overturned+vehicle&hl=ko&tbm=isch&tbs=rimg:CVyvHq8-jBATIjihhJhDCrRsalvMbNIg6sMHPkCFlGgitqkl36VMHKUsV1CYzG05Z5g61Y9LOLcH9frGDQLn_1OO0NioSCaGEmEMKtGxqEd8nBSZMswXQKhIJW8xs0iDqwwcRQZLtcQi-yZAqEgk-QIWUaCK2qREKeSCpyj3dVyoSCSXfpUwcpSxXEQW54WD2WGW2KhIJUJjMbTlnmDoRn4Pp537MCgsqEgnVj0s4twf1-hG3RrW76E3XByoSCcYNAuf847Q2Efs6NXuENb-D',
        'https://www.google.co.kr/search?q=Overturned+vehicle&hl=ko&site=webhp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwigl7qDyKPVAhVChrwKHf2SDbAQ_AUIBigB&biw=1920&bih=950#q=Overturned+vehicle&hl=ko&tbm=isch&tbs=rimg:Ce855K9YdbIfIjgjQ3UOSFcwC7gdtbqLj4C85_1be0gJxxY4IMJthjRZ0EpmmhrQBjXxSddzwvrQ1OaOVhmxulaEdMSoSCSNDdQ5IVzALEWqxJhWf4tnpKhIJuB21uouPgLwRfjxgVIwwLgQqEgnn9t7SAnHFjhHAMIjK4qLN9ioSCQgwm2GNFnQSEZDOb6zxefAUKhIJmaaGtAGNfFIR_1kfMakrR0FgqEgl13PC-tDU5oxG555dCOI4EGSoSCZWGbG6VoR0xETdRhnMFGgYZ'
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










