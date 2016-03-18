__author__ = 'Sherlock'
# def add(**x):
#     num=0
#     for i in x.values():
#         num+=i
#     return num
# print(add(x=1,y=2,z=3))


# d=dict(a=1,b=2,c=3,d=2)
# print(d)
# key=list(d.keys())
# value=list(d.values())
# print(key,value)

#找到俩字典共同的键
# d1=dict(x=1,y=2,z=3,k=4)
# d2=dict(y=2,m=2,n=4)
#用集合
# s1=set(d1)
# s2=set(d2)
# s=s1.intersection(s2)
# s111=s2.intersection(s1)
# #列表
# t=[]
# list1=list(d1.keys())
# list2=list(d2.keys())
# for i in list1:
#     if i in list2:
#         t.append(i)
#
# print(t)

#判断一个列表中的元素是否都在例外一个列表中
# l1=[1,2,3,4]
# l2=[2,3,4]
# s11=set(l1)
# s22=set(l2)
# s=s11.intersection(s22)
# if len(s)==len(l2):
#     print(l2)

print("=================")
#找出俩元组中不相同的元素项
# t1=(1,2,3,'a')
# t2=(4,5,6,'b',2)
#用集合
# t11=set(t1)
# t22=set(t2)
# t33=t11.difference(t22)
# t34=t22.difference(t11)
# # t33.add(frozenset(t34))
# for i in t34:
#     t33.add(i)
# print(t33)
#用元祖
# t=tuple()
# l=list(t)
# for i in t1:
#     if i not  in t2:
#         l.append(i)
# for i in t2:
#     if i not  in t1:
#         l.append(i)
# print(tuple(l))

#合并俩个列表，要求去重
#用集合
# l1=[1,2,3,4,5]
# l2=[2,3,4,5,6]
# s1=set(l1)
# s2=set(l2)
#print(list(s1.union(s2)))
#print(list(s1+s2))
#用列表
# t=[]
# l=l1+l2
# for i in l:
#     if i not in t:
#        t.append(i)
# print(t)
#找到相同值的键
# d1=dict(x=1,y=2,z=3,k=4,m=4,n=1)
# #用列表
# l1=list(d1.values())
# d=[]
# for i in l1:
#     if l1.count(i)>1:
#         if i not in d:
#          d.append(i)
# for i in d:
#     for j in d1:
#        if d1[j]==i:
#           print(j)
#     print("++")
#列表a除去列表b中的元素
# a=[1,3,3,5,1,6,5,5]
# b=[1,3,7,9]
# s1=set(a).intersection(set(b))
# l1=list(s1)
# for i in l1:
#     c=a.count(i)
#     for j in range(0,c-1):
#         a.remove(i)
# print(a)
#统计某段英文里各单词出现的次数
params="i am yujie,i am from liaoning provicce, i study in jilin university"
l=set(params)
count=0
for i in l:
    if i in params:
        count=params.count(i)
    print(count)

