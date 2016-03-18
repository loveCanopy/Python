__author__ = 'Sherlock'
#coding=utf-8
__metaclass__=type #注明新式类
#类
class Perclass(object):
    '这是一个父类'
    def setdata(self,data):
        '这是父类的方法'
        self.data=data



class Childclass(Perclass):
    '这是一个子类'
    def setdata(self,data):
     '这是子类的方法'
     super(Childclass,self).setdata(data) #回调父类的方法，避免重写
     self.gender='man'


p1=Perclass()
p1.setdata("hello")
c1=Childclass()
c1.setdata("world")
# print("the number is %s,%s,%s."%(p1.data,c1.data,c1.gender))
# print(Perclass.__doc__,Childclass.__doc__) #打印类的文档说明
# print(Perclass.__class__,Childclass.__class__) #类的类型 还是类型
# print(p1.__class__,c1.__class__) #对象的类型为自定义的类
print(p1.__dict__,c1.__dict__) #打印对象的属性，以字典形式
# print(Perclass.__name__,Childclass.__name__) #类的名字
print(Perclass.__dict__,Childclass.__dict__) #类的属性
# print(Perclass.__bases__,Childclass.__bases__) #类的父类
# print(Perclass.__base__,Childclass.__base__)
print(p1.__dir__()) #对象的方法和属性


class Animals:
    def __init__(self,data="hello"):
        self.data=data
    def __del__(self):
        pass
    def showdata(self):
        print(self.data)

a=Animals()
a.showdata()
a1=Animals("world")
a1.showdata()


