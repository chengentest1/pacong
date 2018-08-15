import os
import time
from bs4 import BeautifulSoup
import requests
def timer(fun):
    def wep(*args, **kwargs):
        a=fun(*args, **kwargs)
        path = os.getcwd() + '/' + 'write.txt'
        with open(path, 'w', encoding='utf-8') as f:
            for i in a:
                o = i.find('a')
                name = o.attrs['title']
                if '?' in name:
                    name = name.strip('?')
                na='标题：'+name
                f.write(na)
                f.write(o.text+'\n')
    return wep
@timer
def foo(url):
    headers={
        "Content-Type":"text/javascript",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }
    response=requests.get(url,headers=headers)
    response.encoding=response.apparent_encoding
    soup=BeautifulSoup(response.text,'lxml')
    div=soup.find(class_='section')
    a=div.find_all(class_='videoPlayBox')
    return a
foo('http://www.haotijin.com/xiaohua/index_1.html')