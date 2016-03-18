__author__ = 'Sherlock'
#checkbutton  radiobutton lableframe
from tkinter import *
root=Tk()
girls=['a','b','c','d']
g=[]
for girl in girls:
    g.append(IntVar())
    c=Checkbutton(root,text=girl,variable=g[-1])
    c.pack(anchor=W)
#
# v=IntVar()
# Radiobutton(root,text='one',variable=v,value=1).pack(anchor=W)
# Radiobutton(root,text='one',variable=v,value=2).pack(anchor=W)
# Radiobutton(root,text='one',variable=v,value=3).pack(anchor=W)

list=[('a',1),('b',2),('c',3)]
frame=LabelFrame(root,text="hello")
frame.pack(padx=10,pady=10)
v=IntVar()

for lang,num in list:
    b=Radiobutton(frame,text=lang,variable=v,value=num,indicatoron=FALSE).pack(anchor=W)



mainloop()