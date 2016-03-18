__author__ = 'Sherlock'
#coding='utf-8'
import urllib.request
# import html.parser
murl="https://mm.taobao.com/json/request_top_list.htm?type=0&page=" #淘宝妹妹主页
mourl="http://img.alicdn.com/imgextra/i2/539549300/TB1bQUtFVXXXXc.XVXXXXXXXXXX_!!539549300-0-tstar.jpg"
i=2
ph=-1
http="https:"
temp='''<img src='''
temp2='''<img style='''
while i<6:
    url=murl+str(i)
    up=urllib.request.urlopen(url)
    cout=up.read()
    # print(cout)
    # print(url)   #生成URL
    # print("==================")
    head="<img src=".encode(encoding="utf-8")
    tail=".jpg".encode(encoding="utf-8")
    ph=cout.find(head)
    pf=cout.find(tail,ph+1)

    ahref="href=".encode(encoding="utf-8")
    target="target".encode(encoding="utf-8")

    pa=cout.find(ahref)
    pt=cout.find(target,pa)

    ps=http+cout[ph+len(temp)+1:pf+len(tail)].decode()
    #print(ps)

    pq=http+cout[pa+len(ahref)+1:pt-1].decode()
    print(pq)  #某个模特的地址

    mup=urllib.request.urlopen(pq)
    mcout=mup.read()
    # print(mcout) #某个模特网址的内容

    imgh="style".encode(encoding="utf-8")
    imge=".jpg".encode(encoding="utf-8")

    iph=mcout.find(imgh)
    ipe=mcout.find(imge,iph)
    print(mcout[iph:ipe+len(imge)])
    # # print("==================")
    i+=1
