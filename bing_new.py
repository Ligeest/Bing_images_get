import os
import urllib
import time
import requests
import re

now_path = os.getcwd()
if os.path.exists(now_path+'\\image') == True:
    dir_path = now_path+'\\image\\'
    print(dir_path)
else:
    os.mkdir(now_path+'\\image')
    dir_path = now_path+'\\image\\'
    print("创建目录成功")

def list_exchange(will_list):
    return {}.fromkeys(will_list).keys()

head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.3282.204 Safari/537.36'}
pat1 = re.compile('url='+'(.*?)'+'&amp;a',re.S)
pat2 = re.compile('ve="'+'(.*?)'+'.jpg">',re.S)
for page_number in range(1,74):
    page_url = 'https://bing.ioliu.cn/?p='
    page_url += str(page_number)
    #print(page_url)
    time.sleep(3)
    page_data = requests.get(page_url,headers=head)
    page_data = page_data.text
    #page_data = page_data.replace('\n','')
    time.sleep(3)
    d_url = pat1.findall(page_data)
    os.mkdir(dir_path+str(page_number))
    with open(dir_path+str(page_number)+'\\'+str(page_number)+'.txt','w+',encoding='utf-8')as f:
        f.write(str(page_data))
    d_number = 0
    for d1 in range(0,12):
        d_data = requests.get(d_url[d1],headers=head)
        d_data = d_data.text
        for d in range(0,12):
            img_url_list = pat2.findall(d_data)
            img_url =img_url_list[0]
            #print('index:'+str(d))
            img_url += '.jpg'
            print(img_url)
            #urllib.request.urlretrieve(img_url,dir_path+str(page_number)+'\\'+str(d)+'.jpg',headers=head)
            img = requests.get(img_url,headers=head)
            time.sleep(2)
            d_number += 1
            with open(dir_path+str(page_number)+'\\'+str(d_number)+'.jpg', 'wb') as f_obj:
                f_obj.write(img.content)
            break






