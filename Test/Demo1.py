#将1-10000分行写入到a.txt中
fw=open('a.txt','w')
for i in range(1,10000):
	fw.write(str(i)+"\n")
fw.close()	
