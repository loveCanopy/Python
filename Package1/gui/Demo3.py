__author__ = 'Sherlock'
from tkinter import *
def getinfo():
    print("作品：《%s》" % text1.get())
    print("作者：《%s》" % text2.get())

root=Tk()
frame1=LabelFrame(root)
frame2=LabelFrame(root)
frame3=LabelFrame(root)
lable1=Label(frame1,text="作品").grid(row=0,column=0)
text1=Entry(frame1)
text1.grid(row=0,column=1)
lable2=Label(frame2,text='作者').grid(row=1,column=0)
text2=Entry(frame2,show="*") #*号显示
text2.grid(row=1,column=1)

button1=Button(frame3,text="获取信息",command=getinfo)
button2=Button(frame3,text="退出",command=frame3.quit)

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
frame1.pack()
frame2.pack()
frame3.pack()
mainloop()