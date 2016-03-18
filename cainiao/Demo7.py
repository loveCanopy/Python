__author__ = 'Sherlock'
#coding=utf-8
#函数操作
def f1(x):
    if x>1:
        return True
l1=[2,3,1,0]
# l2=filter(f1,l1)
# for i in l2 :
#     print(i,end=" ")

l3=['sun','mon','tus','too']
def f2(x):
    return x*2
# l4=map(f2,l1)
# list()
# l5=list(map(None,l1,l3))
# for i in l4:
#     print(i,end=" ")
# #
# print(l5)
def f3(x,y):
    return (x,y)
l=map(f3,l1,l3)           #返回一个map对象，map的第一个参数不能为none
# for i in l:      俩者等价
#     print(i)
# print(list(l))
l5=map(lambda x:x*2,l1)
print(list(l5))
def f4(x,y):
    return x+y
from functools import reduce
print(reduce(f4,l1))