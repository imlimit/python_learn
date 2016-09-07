#!/usr/bin/python  
# -*- coding: utf-8 -*-  
import HTMLParser  
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string  
import re
import sys
##reload(sys)
##sys.setdefaultencoding( "utf-8" )  
hosturl = 'https://ssl.chunyuyisheng.com/ssl/api/weblogin/'  
#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）  
posturl = 'https://ssl.chunyuyisheng.com/ssl/api/weblogin/'
#设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie  
cj = cookielib.LWPCookieJar()  
cookie_support = urllib2.HTTPCookieProcessor(cj)  
opener = urllib2.build_opener(cookie_support)
urllib2.install_opener(opener)  
#打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）
h = urllib2.urlopen(posturl)
#这里发现post请求有变量就是cooklis，所以不用抓取直接用cooklis
for index,cookie in enumerate(cj):
    print cookie.value
#构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。  
headers = { 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'ssl.chunyuyisheng.com',
            'Origin':'https://ssl.chunyuyisheng.com',
            'Referer':'https://ssl.chunyuyisheng.com/ssl/api/weblogin/?next=http%3A//www.chunyuyisheng.com/home',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',}  
#构造Post数据，他也是从抓大的包里分析得出的。  
postData = {'csrfmiddlewaretoken':cookie.value,  
            'next':'/home',  
            'username':'18750123004',  
            'password':'666666',} 
#需要给Post数据编码  
postData = urllib.urlencode(postData)  
print postData  
#通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程  
request = urllib2.Request(posturl, postData, headers)  
print request  
response = urllib2.urlopen(request).read()
print response

