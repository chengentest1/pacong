'''
在上一个版本上进行升级，上个版本只能爬取一个页面的内容。当前版本可以爬去多个页面的内容
'''

import os

import requests

from bs4 import BeautifulSoup
def read(url):
    headers={

        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }
    html=requests.get(url,headers=headers)
    # html.encoding=html.apparent_encoding
    soup=BeautifulSoup(html.text,'lxml')
    div=soup.find(id='content-left')
    a=div.find_all('div',class_='author clearfix')
    #
    h=1
    k={}
    for i in a:
        ti=i.find('h2').text
        t=ti.strip()
        title=('第%s标题：' %str(h) )+t
        te=i.find_next_sibling().find('span').text
        tp=te.strip()
        tet='文本：'+tp
        k[title]=tet
        h+=1
    return k

def write():

    for i in range(1, 4):
        path = os.getcwd() + '/qiushibaike'+str(i)+'.txt'
        f = open(path, 'w', encoding='utf-8')
        w=read('https://www.qiushibaike.com/text/page/'+str(i)+'/')
        for i in w:
            f.write(i+'\n')
            f.write(w[i]+'\n')
        f.close()
write()
    #
    #
    # f.write(tet)
    #
    #