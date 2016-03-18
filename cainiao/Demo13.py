__author__ = 'Sherlock'
#coding=utf-8
#下载一只猫猫
import urllib.request
# url="http://www.fishc.com"
# reponse=urllib.request.urlopen(url)
# html=reponse.read()
# html=html.decode('utf-8')
# print(html)

url="http://placekitten.com/g/500/600"
# rep=urllib.request.Request(url)
# reponse=urllib.request.urlopen(rep)

reponse=urllib.request.urlopen(url)

catimg=reponse.read()
print(reponse.geturl()) #得到链接地址
print(reponse.info()) #返回一个http对象
print(reponse.getcode()) #返回一个状态码 200正常
with open('catimg1','wb') as f:
    f.write(catimg)
