import os
import http.client
import time
import requests
import json
import re
import urllib

#获取时间
conn = http.client.HTTPConnection('www.baidu.com')
conn.request("GET", "/")
r = conn.getresponse()
#r.getheaders() #获取所有的http头
ts =  r.getheader('date') #获取http头date部分
#将GMT时间转换成北京时间
ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
ttime = time.localtime(time.mktime(ltime)+8*60*60)
time = "%u-%02u-%02u"%(ttime.tm_year,ttime.tm_mon,ttime.tm_mday)

now_path = os.getcwd()
if os.path.exists(now_path+'\\images') == True:
    dir_path = now_path+'\\images\\'+time+'\\'
else:
    os.mkdir(now_path+'\\images')
    os.mkdir(now_path+'\\images\\'+time)
    dir_path = now_path+'\\images\\'+time+'\\'
    print("创建目录成功")
url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=10"
data = requests.get(url)
data = data.text
with open(dir_path+time+'.json','w',encoding='utf-8')as f:
    f.write(str(data))
pat = re.compile('url":"'+'(.*?)'+'",',re.S)
data = pat.findall(str(data))
for i in range(0,8):
    img_url = data[i]
    img_url = 'http://www.bing.com'+img_url
    print("正在下载第"+str(i+1)+"张图片")
    urllib.request.urlretrieve(img_url,dir_path+'%s.jpg' % str(i+1))
exit()
