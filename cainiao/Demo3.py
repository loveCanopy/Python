__author__ = 'Sherlock'
#coding=utf-8
#练习1 逐一显示指定列表中的所有元素
l1=[1,2,3,4,5]
# count=0
# while count<len(l1):
#     print(l1[count]),
#     count+=1

# while len(l1)>0:
#     print(l1[0])
#     l1.pop(0)
#练习2 逆序显示指定元素的所有元素
# count=0
# while count<len(l1):
#     print(l1.pop())

# count=0
# while count<len(l1):
#     print(l1)
#     l1=l1[:-1]
#练习3 求100以内偶数之和
# count=0
# sum=0
# while count<100:
#     if count%2==0:
#         sum=sum+count
#     count+=1
# else:
#     print(sum)
#练习4 逐一显示指定字典的所有键，并说明键的总数
# d1={'x':1,'y':2,'z':3}
# dist=d1.keys()
# l2=list(dist) //字典转列表
# l3=len(l2)
# while l2:
#     print(l2[0],end=" ")
#     l2.pop(0)
# else:
#     print(l3)
#练习5 创建一个包含100以内奇数的列表
# l1=[]
# count=0
# while count<100:
#     if count%2!=0:
#         l1.append(count)
#     count+=1
# else:
#     print(l1)
#练习6 俩个列表形成字典
d1={}
l1=[0,1,2,3,4]
l2=['a','b','c','d','e']
count=0
if len(l2)==len(l1):
    while count<len(l1):
        d1[l2[count]]=l1[count]
        count+=1
    else:
        print(d1)