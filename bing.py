import os
import http.client
import time
import requests

def get_webservertime(host):
    conn = http.client.HTTPConnection(host)
    conn.request("GET", "/")
    r = conn.getresponse()
    print(r)
    #r.getheaders() #获取所有的http头
    ts =  r.getheader('date') #获取http头date部分
    #将GMT时间转换成北京时间
    ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
    #print(ltime)
    ttime = time.localtime(time.mktime(ltime)+8*60*60)
    #print(ttime)
    dat = "%u-%02u-%02u"%(ttime.tm_year,ttime.tm_mon,ttime.tm_mday)
    return dat

now_path = os.getcwd()
if os.path.exists(now_path+'\\images') == True:
    pass
else:
    dir_path = os.mkdir(now_path+'\\images')
    print(dir_path)
url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=10"
time = get_webservertime('www.baidu.com')
data = requests.get(url)
data = data.text
print(data)