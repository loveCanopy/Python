import re
import urllib.request
'''
<img id="dlg_pi_img" src="http://imgsrc.baidu.com/forum/w%3D288/sign=3981fcc3034f78f0800b9dfb41300a83/364efbdcd100baa10f7d252c4710b912c9fc2e43.jpg"
'''
url="http://tieba.baidu.com/p/3563409202"
def openurl(url):
	res=urllib.request.Request(url)
	res.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 5.1; rv:43.0) Gecko/20100101 Firefox/43.0')
	req=urllib.request.urlopen(res)
	html=req.read().decode('utf-8')
	return html
def getimglist(html):
	p=r'<img class="BDE_Image" src="([^"]+\.jpg)"'
	imglist=re.findall(p,html)
	for each in imglist:
		filename=each.split('/')[-1]
		urllib.request.urlretrieve(each,filename)
if __name__=='__main__':
	getimglist(openurl(url))