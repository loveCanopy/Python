from lxml import etree
import requests
import re
import sys
import urllib.request
import os
import  json
import sys
head={}
head['User-Agent']="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
url="http://tieba.baidu.com/p/4390754990"
html=requests.get(url,head)
selector=etree.HTML(html.text)
dield=selector.xpath('//*/img[@class="BDE_Image"]')
flod="图片"
# os.mkdir(flod)
# os.chdir(flod)
d=[]
for i in dield:
    http=i.xpath('//@src')
    for j in http:
       # print(j[-3:],end=",")
       if j[-3:]=="jpg":
           d.append(j)
fold="tupian"
os.mkdir(flod)
os.chdir(flod)
for i in d:
    filename=i[-7:]
    urllib.request.urlretrieve(i,filename)





