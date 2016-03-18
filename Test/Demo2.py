fo=open('a.txt','r')
fw=open('b.txt','w')
for i in fo:
	fw.write(i)
fw.close()
fo.close()