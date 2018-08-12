import os
import time
import requests
import re

#获取当前目录
now_path = os.getcwd()
#判断当前目录下image文件夹是否存在
if os.path.exists(now_path+'/image') == True:
    dir_path = now_path+'/image//'
    print(dir_path)
else:
    os.mkdir(now_path+'/image')
    dir_path = now_path+'/image/'
    print("创建目录成功")

head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.3282.204 Safari/537.36'}
#正则表达式
pat1 = re.compile('url='+'(.*?)'+'&amp;a',re.S)
pat2 = re.compile('ve="'+'(.*?)'+'.jpg">',re.S)
#从第一页到第七十四页
for page_number in range(1,74):
    page_url = 'https://bing.ioliu.cn/?p='
    page_url += str(page_number)
    #得到每一页网址
    time.sleep(2)
    #获取每一页的源码
    page_data = requests.get(page_url,headers=head)
    page_data = page_data.text
    time.sleep(2)
    #匹配正则，将每一页12个图片网址提取出来放进url列表
    d_url = pat1.findall(page_data)
    #创建以页数为名字的文件夹
    os.mkdir(dir_path+str(page_number))
    #在以页数为名字的文件夹写入以页数为名字的每一页网页源码
    with open(dir_path+str(page_number)+'/'+str(page_number)+'.txt','w+',encoding='utf-8')as f:
        f.write(str(page_data))
    #作为每一页图片从1到12的文件名
    d_number = 0
    #分别访问每一页源码提取出12个图片链接
    for d1 in range(0,12):
        d_data = requests.get(d_url[d1],headers=head)
        d_data = d_data.text
        #分别在每一页12个图片网址的源码里提取出12个图片地址
        for d in range(0,12):
            #匹配正则，将每一页12个图片网址的源码里提取出12个图片地址放进url列表
            img_url_list = pat2.findall(d_data)
            #获取图片链接
            img_url =img_url_list[0]
            #由于正则匹配时少了.jpg，所以现在加上
            img_url += '.jpg'
            print(img_url)
            #访问图片链接并保存
            img = requests.get(img_url,headers=head)
            time.sleep(2)
            with open(dir_path+str(page_number)+'/'+str(d_number)+'.jpg', 'wb') as f_obj:
                f_obj.write(img.content)
            d_number += 1
            #跳出此循环，匹配此页下一个图片
            break
