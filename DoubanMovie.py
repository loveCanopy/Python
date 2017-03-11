#encoding: utf-8
import urllib2
import json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
input2data=open("movie","a")
def download(url):
    return urllib2.urlopen(url).read()
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
            data=json.loads(download(url))
            for k in data['subjects']:
                    write2file (i+","+k['title']+","+k['id']+","+k['url']+","+k['rate']+"\n")
    input2data.close()


