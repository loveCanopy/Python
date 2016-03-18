__author__ = 'Sherlock'
import requests
import re
heads={'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:43.0) Gecko/20100101 Firefox/43.0'}
html=requests.get("http://tieba.baidu.com/p/4400048326",heads)
p=r'<img class="BDE_Image" src="([^"]+\.jpg)"'
title=re.findall(p,html.text,re.S)
for each in title:
    print(each)
'''
data['type'] = 'AUTO'
data['i'] = content   #待翻译内容
data['doctype'] = 'json'
data['xmlVersion'] = '1.8'
data['Keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['action'] = 'FY_BY_CLICKBUTTON'
data['typoResult'] = 'true'
html=requests.get("http://tieba.baidu.com/p/4400048326",heads,data) 提交数据
    '''
