fw=open('data.txt','w')
with open('NUT_DATA.txt','r') as f:
	cont=f.readlines()
	c=[x.strip("\n").replace("~","").replace("^"," ").replace("/"," ") for x in cont]
	for i in c:
		fw.write(i+"\n")
	fw.close()
	f.close()
