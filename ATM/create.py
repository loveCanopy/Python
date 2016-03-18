import pickle
f=open('userinfo.txt','rb+')
userinfo={'yujie':[123,5000,5000],'yuhong':[123,2000,2000]}
pickle.dump(userinfo,f)
f.close()