#统计特定的字符出现的次数，每个字符出现的次数
fo=open('c.txt','r')
cont=fo.read()
li=cont.replace(',','').replace('.','').split()
count=0
s="the"
def getcount(x):
	return x,li.count(x)*1.0/len(li)
t=[]
for i in li:
	if i not in t:
		t.append(i)
m=map(getcount,t)
for i in m:
	print(i)