__author__ = 'Sherlock'
#coding=utf-8
#利用有道词典翻译
import urllib.request
import urllib.parse
import json
url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/"
data={}
content=input("please input a str:")
data['type']='AUTO'
data['i']=content
data['doctype']='json'
data['xmlVersion']='1.8'
data['keyfrom']='fanyi.web'
data['ue']='UTF-8'
data['action']='FY_BY_CLICKBUTTON'
data['typoResult']='true'
#隐藏访问的来源
head={}
head['User-Agent']="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
data=urllib.parse.urlencode(data).encode(encoding='utf-8') #将unicode变为utf-8
rep=urllib.request.Request(url,data,head)
# rep.add_header('User-Agent',"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36")
reponse=urllib.request.urlopen(rep)
html=reponse.read().decode('utf-8') #utf-8解码
# print(html)
target = json.loads(html) #返回字典类型
# print(target)
# 根据Fig8的格式，取出最终的翻译结果
result = target["translateResult"][0][0]['tgt']
 # 这里用unicode显示中文，避免乱码
print(u"翻译结果：%s" % (target["translateResult"][0][0]['tgt']))
