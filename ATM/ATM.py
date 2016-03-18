import pickle
filename="userinfo.txt"
f=open(filename,'rb+')
def readinfo():
	userinfo=pickle.load(f)
	return userinfo
#判断用户名是否在用户列表中
def checkname(username):
	userinfo=readinfo()
	for i in list(userinfo.keys()):
		if i==username:
			return True
		else:
			return False
#如果在则进一步判断密码
def checkpasswd(passwd):
	userinfo=readinfo()
	try:
		userlist=userinfo[username]
	finally:
		if int(passwd)==userlist[0]:
			return True
		else:
			return False
def showATM():
	print("A.shopping B. C.cash D.   E.transfer F.")
print("----Welcome to use ATM---")
print("Please Login....")
username=input("please input your username:").strip('\n')
if checkname(username):
	userinfo=readinfo()
	if 'lock' in userinfo[username]:
		print("the user is lock")
		print("please input another username:")
		username=input("please input your username:").strip('\n')
passwd=input("please input your passwd:").strip('\n')
n=3
while True:
	if checkname(username):
		if checkpasswd(passwd):
			print("Login Successful")
			showATM()
			break
		else:
			print("the passwd is error")
			passwd=input("please input your passwd again:").strip('\n')
			n-=n
			if(n>0):
				print("your chance is %d."%n)
				continue
			else:
				list(userinfo[username][0]).append('lock') #用户加入LOCK标记
				pickle.dump(userinfo,f) #写入文件中

	else:
		print("the username is not exist")
		username=input("please input your username:").strip('\n')
		passwd=input("please input your passwd:").strip('\n')
		continue