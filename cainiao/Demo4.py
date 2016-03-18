__author__ = 'Sherlock'
#coding=utf-8
#for循环
#生成字典
l1=[1,2,3]
l2=['a','b','c']
d1=dict(zip(l1,l2))
# print(d1)
# d2={}
# for(k,v) in zip(l1,l2):
#     d2[k]=v
# else:
#     print(d2)
#逐一分开显示指定字典的所有元素
# for k in d1:
#     print(k,d1[k],end=" ")
#逐一显示列表为索引为奇数的元素
l3=[1,2,3,4,5,6,7,8,9]
# for i in range(0,len(l3),2):
#     print(l3[i],end=" ")
#将属于列表了l3,不属于列表l1的元素定义为新列表
l4=[]
# for i in l3:
#     if i not in l1:
#         l4.append(i)
# else:
#     print(l4)

# for i in list(set(l3).difference(set(l1))):
#     l4.append(i)
# else:
#     print(l4)
#l3删除掉属于l1的部分

# for i in l3:
#     if i in l1:
#        l4.append(i)
# else:
#     print(l4)
#     print(l3)
#
# for i in l1:
#     if i in l3:
#         l3.remove(i)
#         # l3.pop(i)
# else:
#     print(l3)


