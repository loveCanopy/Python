from pip._vendor.distlib.compat import raw_input

__author__ = 'Sherlock'
#coding=utf-8
#文件操作
import os
import os.path
import pickle
filename='D:\\b.txt'
if os.path.isfile(filename):
  f1=open(filename,'r') #a+为追加 w+每次都打开一个新文件
# f1.write("world")
# f1.write("hellp")
# f1.flush()
# f1.seek(0)
# print(f1.readline())
# f1.close()

# while True:
#     line=raw_input("please input a number:")
#     if line=='q' or line=='quit':
#         break
#     else:
#         f1.write(line+'\r\n')
# else:
#     f1.close()
# f1.seek(0)
# l1=['a','b','c']
# l2=('d','e','f')
# l3={'a':1,'b':2,'c':3}
# f1.writelines(l1)
# f1.writelines(l2)
# f1.writelines(l3)
# print(f1.fileno())文件描述符
# print(f1.buffer)
f1.seek(0)
print(f1.readline()) #必须有读模式打开文件,追加模式也读不出来
# # print(f1.readlines()) #列表形式返回
# # print(f1.readlines()) #必须有读模式打开文件,追加模式也读不出来
# f1.close()

# os.mkdir("d:\\a")
# os.makedirs("d:\\a\\v\\g")
# print(os.getcwd())
# print(os.stat("d:\\b.txt"))
# print(os.listdir("d:\\")) #d目录下的所有文件
# os.remove("d:\\a")
# os.removedirs("d:\\a\\v\\g")
# os.rename("d:\\a","d:\\b")
# os.chmod("d:\\b.txt",777)
# os.symlink("d:\\b.txt","b.lnk",target_is_directory=False,dir_fd=None)
# print(os.utime("d:\\b.txt"))???
# os.tmpfile("d:\\abc.txt")???
# g=os.walk("d:\\b")
# for i in g:
#     print(i)
# os.path.basename("E:\\untitled\\src\\img")
# os.path.dirname("E:\\untitled\\src\\img")
# print(os.path.isabs("d:\\b.txt"))
# print(os.path.islink("d:\\b.txt"))
# print(os.path.samefile("d:\\b.txt","e:\\a.txt"))
# print(os.path.isdir("d:\\c++"))
# l3={'a':1,'b':2,'c':3}
# f1.write(l3) #不能写入字典
# f1.writelines(l3)#能写入字典的键值
# f1.close()



# 对象的持久输出
# d={'x':1,'y':'hell','z':"word"}
# # pickle.dump(d,f1)
# f1.flush()
# # f1.seek(0)
# # print(f1.readlines())
# print(pickle.load(f1))
# f1.close()
