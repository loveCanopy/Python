s="hello,world"
s1=s.replace('e',"i")
l1=s.split(',')
l2=s.strip(',')
print(s1,l1,l2)

l2=['ajkljklg\n','dgag\n']
for i in l2:
	i1=i.strip('\n')
	print(i1)