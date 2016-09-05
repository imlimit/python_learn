# -*- coding:utf-8 -*-
import re
import urllib2
from bs4 import BeautifulSoup
import redis
import time

r0=redis.StrictRedis(
    host='localhost',
    port=6379,
    db=0,
    password=None,
    socket_timeout=None,
    connection_pool=None,
    charset='utf-8',
    errors='strict',
    unix_socket_path=None
)

def get_content(url):
    header_dict = {'User-Agent': \
                       'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko'}
    # python3
    # req = urllib.request.Request(url=url, headers=header_dict)
    # request = urllib.request.Request('http://www.xicidaili.com/nn/', headers=header_dict)
    # info = urllib.request.urlopen(request)
    #python2
    request = urllib2.Request(url, headers=header_dict)
    info = urllib2.urlopen(request)
    soup = BeautifulSoup(info.read(), "html5lib")
    all_ip = soup.find_all('tr')
    info.close()
    return all_ip



for i in range(1, 1029):
    url = 'http://www.xicidaili.com/nn/'
    url = "%s%d" % (url, i)
    print(url)
    all_ip = get_content(url)
    for proxy_ip in all_ip:
        #r0.hsetnx("proxy", proxy_ip.contents[3].string, proxy_ip.contents[5].string)
        print(proxy_ip.contents[3].string"+"proxy_ip.contents[5].string)
    print("入库成功")
    time.sleep(10)


