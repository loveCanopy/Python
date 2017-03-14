#encoding: utf-8
import urllib2
import json
import sys
import random
reload(sys)
sys.setdefaultencoding( "utf-8" )
input2data=open("movie","a")
user_agents = [
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36"
    ]
proxies=["120.35.80.175:8998"]
def getHtml(url,headers,proxies):
    random_userAget = random.choice(headers)
    random_proxy = random.choice(proxies)
    print random_proxy,random_userAget
    # 下面是模拟浏览器进行访问
    req = urllib2.Request(url)
    req.add_header("User-Agent", random_userAget)
    req.add_header("GET", url)
    # 下面是使用ip代理进行访问
    proxy_support = urllib2.ProxyHandler({"http": random_proxy})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    html = urllib2.urlopen(req)
    return html
# def download(url):
#     return urllib2.urlopen(url).read()
def write2file(data):
    input2data.write(data)
tag=['最新','经典','可播放','豆瓣高分','冷门佳片',
     '华语','欧美','韩国','日本','动作','喜剧','科幻','恐怖']
page_limit=20000
page_start=0
sort=['recommend','time','rank']
url_common="https://movie.douban.com/j/search_subjects?type=movie&tag="
if __name__ == '__main__':
    for i in sort:
        for j in tag:
            url=url_common+j+"&sort="+i+"&page_limit="+str(page_limit)+"&page_start="+str(page_start)
            #url="https://movie.douban.com/j/search_subjects?type=movie&tag=日本&sort=recommend&page_limit=20&page_start=0"
            data=json.loads(getHtml(url,user_agents,proxies).read())
            for k in data['subjects']:
                    write2file (i+","+k['title']+","+k['id']+","+k['url']+","+k['rate']+"\n")
    input2data.close()


