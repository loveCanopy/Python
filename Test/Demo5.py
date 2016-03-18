fo=open(r'ml-1m/movies.dat','r')
fw=open("info.txt",'w')
fw1=open("cate.txt",'w')
def getnumber(x):
	while len(x)<4:
		x='0'+x
	return x
cont=fo.read()
li=cont.split('\n')
for i in li:
	if len(i)!=0:
		info=i.split('::')
		moivesid=info[0]
		moviesyear=info[1][-5:-1]
		moviesname=info[1][:-7]
		ss=getnumber(moivesid)+"\t"+moviesname+"\t"+moviesyear+"\n"
		fw.write(ss)
		catee=info[2].split('|')
		for j in catee:
			fw1.write(getnumber(moivesid)+"\t"+j+'\n')

fw1.close()
fw.close()
fo.close()
