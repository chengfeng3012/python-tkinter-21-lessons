

#方法一：


import tkinter
import time

def gettime():
      timestr = time.strftime("%H:%M:%S") # 获取当前的时间并转化为字符串
      lb.configure(text=timestr)   # 重新设置标签文本
      root.after(1000,gettime) # 每隔1s调用函数 gettime 自身获取时间

root = tkinter.Tk()
root.title('时钟')

lb = tkinter.Label(root,text='',fg='blue',font=("黑体",80))
lb.pack()
gettime()
root.mainloop()

import tkinter
import time


#方法二：


def gettime():
      var.set(time.strftime("%H:%M:%S"))   # 获取当前时间
      r.after(1000,gettime)   # 每隔1s调用函数 gettime 自身获取时间

r = tkinter.Tk()
r.title('时钟')
var=tkinter.StringVar()

lb = tkinter.Label(r,textvariable=var,fg='blue',font=("黑体",80))
lb.pack()
gettime()
r.mainloop()




from tkinter import *
import time
import datetime

def gettime():
       s=str(datetime.datetime.now())+'\n'
       txt.insert(END,s)
       r1.after(1000,gettime)  # 每隔1s调用函数 gettime 自身获取时间

r1=Tk()
r1.geometry('320x240')
txt=Text(r1)
txt.pack()
gettime()
r1.mainloop()
