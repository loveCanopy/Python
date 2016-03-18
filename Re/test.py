__author__ = 'Sherlock'
import re
import urllib.request
import os
url="http://tieba.baidu.com/p/4400048326"
def openurl(url):
	res=urllib.request.Request(url)
	res.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 5.1; rv:43.0) Gecko/20100101 Firefox/43.0')
	req=urllib.request.urlopen(res)
	html=req.read().decode('UTF-8')
	return html
def getimglist(html):
	p=r'<img class="BDE_Image" src="([^"]+\.jpg)"'
	p1=r'<img id="dlg_pi_img" src="http://imgsrc.baidu.com/forum/w%3D288/sign=f9bc357ef2d3572c66e29bd4b2126352/e288f8edab64034f8b9da091afc379310b551d4c.jpg'
	imglist=re.findall(p,html)
	return imglist

def save_imgs(img_list,folder='teibamm'):
	os.mkdir(folder)
	os.chdir(folder)
	for each in img_list:
		filename = each.split('/')[-1]
		# with open(filename, 'wb') as f:
		# 	img = urllib.request.urlopen(each)
		# 	f.write(img)
		urllib.request.urlretrieve(each,filename)
if __name__=="__main__":
	imglist=getimglist(openurl(url))
	save_imgs(imglist)