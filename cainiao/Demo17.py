__author__ = 'Sherlock'
import random
l1=list()
d1=dict()
v=list()
for i in range(0,1000000):
    num=random.randint(1000000,10000000)
    l1.append(num)

key=random.sample(l1,100000)

for i in range(0,100000):
    name="yujie"+str(key[i])
    year=random.randint(1900,1999)
    if i%5==1:
        national="menggu"
    else:
        national="han"

    if i%3==1:
        sex="female"
    else:
        sex="male"
    v=[name,year,national,sex]

    d1.setdefault(key[i],v)
c=0
c1=0
for key in d1:
    if d1[key][1]==1995:
        c+=1
        print(d1[key][0])
        if d1[key][3]=='female':
            c1+=1
print(c1/(c-c1))