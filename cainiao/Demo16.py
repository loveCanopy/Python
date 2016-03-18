__author__ = 'Sherlock'
#实现列表的排序，最大值在前

l1=[4,3,1,2,5,8,2]
# t=0
# j=1
# while j<len(l1):
#     if l1[j]>l1[0]:
#         t=l1[0]
#         l1[0]=l1[j]
#         l1[j]=t
#     j+=1
# print(l1)
#
# j=2
# while j<len(l1):
#     if l1[j]>l1[1]
j=0
while j < len(l1):
    i=j+1
    while i<len(l1):
        if l1[j]>l1[i]:
            t=l1[i]
            l1[i]=l1[j]
            l1[j]=t
        i+=1
    j+=1
print(l1)