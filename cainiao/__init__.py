__author__ = 'Sherlock'
#coding=utf-8
#异常
# try:
#     while True:
#         a=input("please a number:")
#         b=input("please a number:")
#         if a=='q' or a=="quit":
#             break
#         print(int(a)+int(b))
# except ValueError as e:
#     print("do not str")
#     print(e)
# else:#不异常的时候执行
#     print("hello")
# finally:#最后执行
#     print("world")

#
# class Myexception(BaseException):
#     print("this is my exception")
def add(l1,l2):
    if not l2 or not l1:
        raise ValueError("the list is empty")
    else:
        print(l1+l2)
l1=[1,23,0]
l2=[1,2,3]
add(l1,l2)


