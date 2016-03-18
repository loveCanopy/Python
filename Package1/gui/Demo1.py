__author__ = 'Sherlock'
from tkinter  import *
root=Tk() #主窗体，label，button
frame1=Frame(root)
frame2=Frame(root)
# image=Image("catimg1.jpg")
# photo=PhotoImage(image)
# lable2=Label(root,photo)
# lable2.pack(side=RIGHT)
#photo=PhotoImage(file="catimg1.jpg") #JPG需要PIL格式 但目前Python3.5不支持

def hello():
    var.set("donot cheat me")

var=StringVar()
var.set("I am a good man")

photo=PhotoImage(file="1.gif")
lable1=Label(frame1,textvariable=var,image=photo,padx=2,pady=2,compound=CENTER,font=("宋体",20),fg="white")
lable1.pack(side=LEFT)
frame1.pack()
lable2=Button(frame2,text="按我",command=hello)
lable2.pack(side=RIGHT)
frame2.pack()

mainloop()