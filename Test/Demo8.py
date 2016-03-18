fo=open('info.txt','r')
fo1=open('cate.txt','r')
info=str(input("please input a number:"))
if info!="goodbye":
	movieinfo=fo.readlines()
	x=[i.strip("\n").replace('\t','|') for i in movieinfo[:7]]
	moviecate=fo1.readlines()
	y=[i.strip("\n").replace('\t','|') for i in moviecate[:100]]
	for i in x:
		i=i.split("|")
		if i[1]==info:
			id=i[0]
			name=i[1]
			year=i[2]
			print(id,name,year,end=",")
	for j in y:
		j=j.split("|")
		if j[0]==id:
			print(j[1],end=",")
else:
	print("thank you ")