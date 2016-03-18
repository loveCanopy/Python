__author__ = 'Sherlock'
#coding=utf-8
#函数的闭包,yield,装饰器
# def f1(x):
#     def f2(y):
#         return y**x
#     return f2
# f3=f1(2)
# print(f3(3))
#
# l1=(i**2 for i in range(1,11))
# for i in l1:
#     print(i,end=" ")
#
#
# def getnum(x):
#     y=1
#     while y<11:
#         yield y**2
#         y+=1
# l2=getnum(10)
# print(list(l2))
#
# for i in l2:
#     print(i,end=" ")
#函数的装饰器
def deco(func):
    def wrapper():
        print("hello")
        func()
        print("world")
    return wrapper
@deco

def show():
    print("i am yujie")
show()

def deco1(func):
    def wrapper(x):
        print("hel")
        func(x)
        print("world")
    return wrapper
@deco1
def show1(x):
    print(x)
show1("iam fan")

#函数的递归
def fac(x):
    if x<=1:
        return 1
    else:
        return fac(x-1)*x
print(fac(4))

def power(x,y):
    if y==0:
        return 1
    else:
        return power(x,y-1)*x
print(power(2,3))
