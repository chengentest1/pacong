import os
import time  #'http://jandan.net/ooxx/page-47#comments'
import uuid

from selenium import webdriver
from bs4 import BeautifulSoup
import threading
import requests
li=[]
def readl(url):
    driver=webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    data=driver.page_source
    soup=BeautifulSoup(data,'lxml')
    hh=soup.select('a.view_img_link')
    for i in hh:
        z=i.get('href')
        ul="http:"+z
        li.append(ul)
    return li

def red(kk):
    file_name = str(uuid.uuid4()) + '.jpg'
    path = os.getcwd()+"/" + file_name
    img = requests.get(kk)
    with open(path, 'wb') as f:
        f.write(img.content)
if __name__ == "__main__":
    # readl()
    for i in range(1, 3):
        w=readl('http://jandan.net/ooxx/page-'+str(i)+'#comments')
        w+=w
        time.sleep(10)
    for i in w:
        red(i)
