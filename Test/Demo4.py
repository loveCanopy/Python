#将数据写入文件d.txt，结果如下：
'''
0001 jeapedu0001 'f'
0002 jeapedu0002 'm'
0003 jeapedu0003 'f'
....
1000 jeapedu1000  ''
'''
fw=open('d.txt','w')

def getnumber(x):
	x=str(x)
	while len(x)<4:
		x='0'+x
	return x	
for i in range(0,1000):
	id=getnumber(i)
	name="jeapedu"+id
	sex="m"
	if i%2==0:
		sex='f'
	fw.write(id+'\t'+name+'\t'+sex+'\n')	
fw.close()