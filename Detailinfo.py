#encoding: utf-8
import urllib2
import time
import json
import lxml
import random
from lxml import etree
import sys
import cookielib
cookie=cookielib.CookieJar()
reload(sys)
sys.setdefaultencoding( "utf-8" )
urls=[]
user_agents = [  
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6"
    ]
with open('movie','r') as f:
    while True:
        line=f.readline()
        if line:
           urls.append(line.split(",")[3])
        else:
            break
f.close()
input2data=open("movie_info","a")
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
proxies=[]
def etl(log):
    return log.replace("\\r","").replace("\\n","").replace("\\t","").replace("\\","").replace("\n","").replace(" ","")
with open('ip.txt','r') as f:
    while True:
        line=f.readline()
        if len(line.split("|"))>=2:
            str=line.split("|")[1]+":"+line.split("|")[2]
            line=etl(str)
            #print line
            if line:
                proxies.append(line)
        else:
            break
    print proxies
def write2file(data):
    input2data.write(data)
tasks=[]
for j in range(len(urls)//100+1):
    tasks.append(urls[j*100:(j+1)*100])
for j in tasks:
    for i in j:
        movie = {}
        try:
            html=getHtml(i,user_agents,proxies).read()
            while len(html)<=10:
                html = getHtml(i, user_agents, proxies).read()
            page = etree.HTML(str(html).lower().decode('utf-8'))
            # 电影名
            movie['title'] = page.xpath('//h1/span[@property="v:itemreviewed"]/text()')
            # 导演
            movie['director'] = page.xpath('//div[@id=\"info\"]/span[1]/span[2]/a/text()')
            # 主演
            movie['actor'] = page.xpath('//a[@rel="v:starring"]/text()')
            # 类型
            movie['type'] = page.xpath('//*[@id="info"]//span[@property="v:genre"]/text()')
            # 国家和地区
            movie['area'] = page.xpath('//*[@id="info"]/text()')
            # 上映时间
            movie['publishtime'] = page.xpath('//span[@property=\"v:initialReleaseDate\"]/text()')
            # 片长
            movie['time'] = page.xpath('//*[@id="info"]//span[@property="v:runtime"]/text()')
            # 评分
            movie['rate_num'] = page.xpath('//strong[@property="v:average"]/text()')
            # 评价
            movie['rate'] = page.xpath('//div[@class="rating_sum"]/a/span/text()')
            # 介绍
            movie['introduce'] = page.xpath('//*[@id="link-report"]/span/text()')
            # print str(movie).decode("unicode-escape")
            write2file(etl(str(movie).decode("unicode-escape")) + "\n")
        except Exception,error:
            print error
    time.sleep(10)

input2data.close()
