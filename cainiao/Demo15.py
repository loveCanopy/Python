__author__ = 'Sherlock'
#coding=utf-8
#代理IP
url="http://whatismyip.com.tw"
import random
import urllib.request
import urllib.parse
l1=['121.42.158.116:80','182.90.3.204:80','49.66.189.70:8080','150.255.174.58:8090','182.90.80.207:8123']
proxy_support=urllib.request.ProxyHandler({'http':random.choice(l1)})
opener=urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
req=urllib.request.Request(url)
reponse=urllib.request.urlopen(req)
html=reponse.read().decode('utf-8')
print(html)