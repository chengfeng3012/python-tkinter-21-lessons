#
from tkinter import *
root = Tk()
root.title('我的第一个Python窗体')
root.geometry('240x240')
root.mainloop()

#
from  tkinter import *
root1 = Tk()
lb = Label(root1,text='我的第一个标签',\
        bg='#d3fbfb',\
        fg='red',\
        font=('华文新魏',32),\
        width=20,\
        height=2,\
        relief=SUNKEN)
lb.pack()
root1.mainloop()

#
from tkinter import *
root2 = Tk()
root2.geometry('320x240')

msg1 = Message(root2,text='''我的水平起始位置相对窗体 0.2，垂直起始位置为绝对位置 80 像素，我的高度是窗体高度的0.4，宽度是200像素''',relief=GROOVE)
msg1.place(relx=0.2,y=80,relheight=0.4,width=200)
root2.mainloop()

#


#方法一：


import tkinter
import time

def gettime():
      timestr = time.strftime("%H:%M:%S") # 获取当前的时间并转化为字符串
      lb.configure(text=timestr)   # 重新设置标签文本
      root3.after(1000,gettime) # 每隔1s调用函数 gettime 自身获取时间

root3 = tkinter.Tk()
root3.title('时钟')

lb = tkinter.Label(root3,text='',fg='blue',font=("黑体",80))
lb.pack()
gettime()
root3.mainloop()

import tkinter
import time


#方法二：


def gettime():
      var.set(time.strftime("%H:%M:%S"))   # 获取当前时间
      root4.after(1000,gettime)   # 每隔1s调用函数 gettime 自身获取时间

root4 = tkinter.Tk()
root4.title('时钟')
var=tkinter.StringVar()

lb = tkinter.Label(root4,textvariable=var,fg='blue',font=("黑体",80))
lb.pack()
gettime()
root4.mainloop()




from tkinter import *
import time
import datetime

def gettime():
       s=str(datetime.datetime.now())+'\n'
       txt.insert(END,s)
       root5.after(1000,gettime)  # 每隔1s调用函数 gettime 自身获取时间

root5=Tk()
root5.geometry('320x240')
txt=Text(root5)
txt.pack()
gettime()
root5.mainloop()

#
from tkinter import *

def run1():
     a = float(inp1.get())
     b = float(inp2.get())
     s = '%0.2f+%0.2f=%0.2f\n' % (a, b, a + b)
     txt.insert(END, s)   # 追加显示运算结果
     inp1.delete(0, END)  # 清空输入
     inp2.delete(0, END)  # 清空输入

def run2(x, y):
     a = float(x)
     b = float(y)
     s = '%0.2f+%0.2f=%0.2f\n' % (a, b, a + b)
     txt.insert(END, s)   # 追加显示运算结果
     inp1.delete(0, END)  # 清空输入
     inp2.delete(0, END)  # 清空输入

root6 = Tk()
root6.geometry('460x240')
root6.title('简单加法器')

lb1 = Label(root6, text='请输入两个数，按下面两个按钮之一进行加法计算')
lb1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
inp1 = Entry(root6)
inp1.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.1)
inp2 = Entry(root6)
inp2.place(relx=0.6, rely=0.2, relwidth=0.3, relheight=0.1)

# 方法-直接调用 run1()
btn1 = Button(root6, text='方法一', command=run1)
btn1.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)

# 方法二利用 lambda 传参数调用run2()
btn2 = Button(root6, text='方法二', command=lambda: run2(inp1.get(), inp2.get()))
btn2.place(relx=0.6, rely=0.4, relwidth=0.3, relheight=0.1)

# 在窗体垂直自上而下位置60%处起，布局相对窗体高度40%高的文本框
txt = Text(root6)
txt.place(rely=0.6, relheight=0.4)

root6.mainloop()

#
from tkinter import *
def Mysel():
      dic = {0:'甲',1:'乙',2:'丙'}
      s = "您选了" + dic.get(var.get()) + "项"
      lb.config(text = s)

root7 = Tk()
root7.title('单选按钮')
lb = Label(root7)
lb.pack()

var = IntVar()
rd1 = Radiobutton(root7,text="甲",variable=var,value=0,command=Mysel)
rd1.pack()

rd2 = Radiobutton(root7,text="乙",variable=var,value=1,command=Mysel)
rd2.pack()

rd3 = Radiobutton(root7,text="丙",variable=var,value=2,command=Mysel)
rd3.pack()

root7.mainloop()

#
from tkinter import *
import tkinter

def run():
     if(CheckVar1.get()==0 and CheckVar2.get()==0 and CheckVar3.get()==0 and CheckVar4.get()==0):
         s = '您还没选择任何爱好项目'
     else:
         s1 = "足球" if CheckVar1.get()==1 else ""
         s2 = "篮球" if CheckVar2.get() == 1 else ""
         s3 = "游泳" if CheckVar3.get() == 1 else ""
         s4 = "田径" if CheckVar4.get() == 1 else ""
         s = "您选择了%s %s %s %s" % (s1,s2,s3,s4)
     lb2.config(text=s)

root8 = tkinter.Tk()
root8.title('复选框')
lb1=Label(root8,text='请选择您的爱好项目')
lb1.pack()

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()

ch1 = Checkbutton(root8,text='足球',variable = CheckVar1,onvalue=1,offvalue=0)
ch2 = Checkbutton(root8,text='篮球',variable = CheckVar2,onvalue=1,offvalue=0)
ch3 = Checkbutton(root8,text='游泳',variable = CheckVar3,onvalue=1,offvalue=0)
ch4 = Checkbutton(root8,text='田径',variable = CheckVar4,onvalue=1,offvalue=0)

ch1.pack()
ch2.pack()
ch3.pack()
ch4.pack()

btn = Button(root8,text="OK",command=run)
btn.pack()

lb2 = Label(root8,text='')
lb2.pack()
root8.mainloop()

#
from tkinter import *
def ini():
      Lstbox1.delete(0,END)
      list_items = ["数学","物理","化学","语文","外语"]
      for item in list_items:
           Lstbox1.insert(END,item)

def clear():
      Lstbox1.delete(0,END)

def ins():
      if entry.get() != '':
          if Lstbox1.curselection() == ():
              Lstbox1.insert(Lstbox1.size(),entry.get())
          else:
              Lstbox1.insert(Lstbox1.curselection(),entry.get())

def updt():
      if entry.get() != '' and Lstbox1.curselection() != ():
           selected=Lstbox1.curselection()[0]
           Lstbox1.delete(selected)
           Lstbox1.insert(selected,entry.get())

def delt():
      if Lstbox1.curselection() != ():
           Lstbox1.delete(Lstbox1.curselection())

root9 = Tk()
root9.title('列表框实验')
root9.geometry('320x240')

frame1 = Frame(root9,relief=RAISED)
frame1.place(relx=0.0)

frame2 = Frame(root9,relief=GROOVE)
frame2.place(relx=0.5)

Lstbox1 = Listbox(frame1)
Lstbox1.pack()

entry = Entry(frame2)
entry.pack()

btn1 = Button(frame2,text='初始化',command=ini)
btn1.pack(fill=X)

btn2 = Button(frame2,text='添加',command=ins)
btn2.pack(fill=X)

btn3 = Button(frame2,text='插入',command=ins) # 添加和插入功能实质上是一样的
btn3.pack(fill=X)

btn4 = Button(frame2,text='修改',command=updt)
btn4.pack(fill=X)

btn5 = Button(frame2,text='删除',command=delt)
btn5.pack(fill=X)

btn6 = Button(frame2,text='清空',command=clear)
btn6.pack(fill=X)

root9.mainloop()

#
from tkinter.ttk import *
from tkinter import *

def calc(event):
       a = float(t1.get())
       b = float(t2.get())
       dic = {0:a+b,1:a-b,2:a*b,3:a/b}
       c = dic[comb.current()]
       lbl.config(text=str(c))

root10 = Tk()
root10.title('四则运算')
root10.geometry('320x240')

t1 = Entry(root10)
t1.place(relx=0.1,rely=0.1,relwidth=0.2,relheight=0.1)

t2 = Entry(root10)
t2.place(relx=0.5,rely=0.1,relwidth=0.2,relheight=0.1)

var = StringVar()

comb = Combobox(root10,textvariable=var,values=['加','减','乘','除',])
comb.place(relx=0.1,rely=0.5,relwidth=0.2)
comb.bind('<<ComboboxSelected>>',calc)

lbl=Label(root10,text='结果')
lbl.place(relx=0.5,rely=0.7,relwidth=0.2,relheight=0.3)

root10.mainloop()

#
from tkinter  import  *

def show(event):
      s = '滑块的取值为' + str(var.get())
      lb.config(text=s)

root11 = Tk()
root11.title('滑块实验')
root11.geometry('320x180')
var=DoubleVar()
scl = Scale(root11,orient=HORIZONTAL,length=200,from_=1.0,to=5.0,label='请拖动滑块',tickinterval=1,resolution=0.05,variable=var)
scl.bind('<ButtonRelease-1>',show)
scl.pack()

lb = Label(root11,text='')
lb.pack()

root11.mainloop()

#
from tkinter import *

def new():
     s = '新建'
     lb1.config(text=s)

def ope():
     s = '打开'
     lb1.config(text=s)

def sav():
     s = '保存'
     lb1.config(text=s)

def cut():
     s = '剪切'
     lb1.config(text=s)

def cop():
     s = '复制'
     lb1.config(text=s)

def pas():
     s = '粘贴'
     lb1.config(text=s)

def popupmenu(event):
     mainmenu.post(event.x_root,event.y_root)

root12 = Tk()
root12.title('菜单实验')
root12.geometry('320x240')

lb1 = Label(root12,text='显示信息',font=('黑体',32,'bold'))
lb1.place(relx=0.2,rely=0.2)

mainmenu = Menu(root12)
menuFile = Menu(mainmenu)  # 菜单分组 menuFile
mainmenu.add_cascade(label="文件",menu=menuFile)
menuFile.add_command(label="新建",command=new)
menuFile.add_command(label="打开",command=ope)
menuFile.add_command(label="保存",command=sav)
menuFile.add_separator()  # 分割线
menuFile.add_command(label="退出",command=root12.destroy)

menuEdit = Menu(mainmenu)  # 菜单分组 menuEdit
mainmenu.add_cascade(label="编辑",menu=menuEdit)
menuEdit.add_command(label="剪切",command=cut)
menuEdit.add_command(label="复制",command=cop())
menuEdit.add_command(label="粘贴",command=pas())

root12.config(menu=mainmenu)
root12.bind('Button-3',popupmenu) # 根窗体绑定鼠标右击响应事件
root12.mainloop()

#
from tkinter import *

def newwind():
      winNew = Toplevel(root13)
      winNew.geometry('320x240')
      winNew.title('新窗体')
      lb2 = Label(winNew,text='我在新窗体上')
      lb2.place(relx=0.2,rely=0.2)
      btClose=Button(winNew,text='关闭',command=winNew.destroy)
      btClose.place(relx=0.7,rely=0.5)

root13 = Tk()
root13.title('新建窗体实验')
root13.geometry('320x240')

lb1 = Label(root13,text='主窗体',font=('黑体',32,'bold'))
lb1.place(relx=0.2,rely=0.2)

mainmenu = Menu(root13)
menuFile = Menu(mainmenu)
mainmenu.add_cascade(label='菜单',menu=menuFile)
menuFile.add_command(label='新窗体',command=newwind)
menuFile.add_separator()
menuFile.add_command(label='退出',command=root13.destroy)

root13.config(menu=mainmenu)
root13.mainloop()

#
from tkinter import *
import tkinter.messagebox

def xz():
    answer=tkinter.messagebox.askokcancel('请选择','请选择确定或取消')
    if answer:
        lb.config(text='已确认')
    else:
        lb.config(text='已取消')

root14 = Tk()

lb = Label(root14,text='')
lb.pack()
btn=Button(root14,text='弹出对话框',command=xz)
btn.pack()
root14.mainloop()

#
from tkinter.simpledialog import *
from tkinter import *

def xz():
    s=askstring('请输入','请输入一串文字')
    lb.config(text=s)

root15 = Tk()

lb = Label(root15,text='')
lb.pack()
btn=Button(root15,text='弹出输入对话框',command=xz)
btn.pack()
root15.mainloop()

#
from tkinter import *
import tkinter.filedialog

def xz():
    filename=tkinter.filedialog.askopenfilename()
    if filename != '':
         lb.config(text='您选择的文件是'+filename)
    else:
         lb.config(text='您没有选择任何文件')

root16 = Tk()

lb = Label(root16,text='')
lb.pack()
btn=Button(root16,text='弹出文件选择对话框',command=xz)
btn.pack()
root16.mainloop()

#
from tkinter import *
import tkinter.colorchooser

def xz():
    color=tkinter.colorchooser.askcolor()
    colorstr=str(color)
    print('打印字符串%s 切掉后=%s' % (colorstr,colorstr[-9:-2]))
    lb.config(text=colorstr[-9:-2],background=colorstr[-9:-2])

root17 = Tk()

lb = Label(root17,text='请关注颜色的变化')
lb.pack()
btn=Button(root17,text='弹出颜色选择对话框',command=xz)
btn.pack()
root17.mainloop()

#
from tkinter import *

def show(event):
    s = event.keysym
    lb.config(text=s)

root18=Tk()
root18.title('按键实验')
root18.geometry('200x200')
lb=Label(root18,text='请按键',font=('黑体',48))
lb.bind('<Key>',show)
lb.focus_set()
lb.pack()
root18.mainloop()

#
#插入文件图片
import tkinter as tk
import os

path = os.getcwd()

root19 = tk.Tk()

#创建一个标签类, [justify]:对齐方式
textLabel = tk.Label(root19,text="你在右边会看到一个图片，\n我在换个行",
justify = tk.LEFT)#左对齐
textLabel.pack(side=tk.LEFT)#自动对齐,side：方位

 

#创建一个图片管理类
photo = tk.PhotoImage(file=path + "/18.png")#file：t图片路径
imgLabel = tk.Label(root19,image=photo)#把图片整合到标签类中
imgLabel.pack(side=tk.RIGHT)#自动对齐


tk.mainloop()

import tkinter as tk
import os

root20 = tk.Tk()
path = os.getcwd() + '/'

#增加背景图片
photo = tk.PhotoImage(file=path + "18.png")
theLabel = tk.Label(root20,
text="我是内容,\n请你阅读",#内容
justify=tk.LEFT,#对齐方式
image=photo,#加入图片
compound = tk.CENTER,#关键:设置为背景图片
font=("华文行楷",20),#字体和字号
fg = "white")#前景色
theLabel.pack()

 

tk.mainloop()

#
#插入文件图片
import tkinter as tk

root21 = tk.Tk()

frame1 = tk.Frame(root21)#这是上面的框架
frame2 = tk.Frame(root21)#这是下面的框架


var = tk.StringVar()#储存文字的类
var.set("你在右边会看到一个图片，\n我在换个行")#设置文字

#创建一个标签类, [justify]:对齐方式，[frame]所属框架
textLabel = tk.Label(frame1,textvariable=var,
justify = tk.LEFT)#显示文字内容 
textLabel.pack(side=tk.LEFT)#自动对齐,side：方位

 

#创建一个图片管理类
photo = tk.PhotoImage(file="18.png")#file：t图片路径
imgLabel = tk.Label(frame1,image=photo)#把图片整合到标签类中
imgLabel.pack(side=tk.RIGHT)#自动对齐


def callback():#触发的函数
    var.set("你还真按了")#设置文字

#[frame]所属框架 ，text 文字内容 command：触发方法
theButton = tk.Button(frame2,text="我是下面的按钮",command=callback)
theButton.pack()#自动对齐

 

frame1.pack(padx=10,pady=10)#上框架对齐
frame2.pack(padx=10,pady=10)#下框架对齐


tk.mainloop()

#
from tkinter import *
import cv2
from PIL import Image,ImageTk
def take_snapshot():
    print("有人给你点赞啦！")
    
def video_loop():
    success, img = camera.read()  # 从摄像头读取照片
    if success:
        cv2.waitKey(100)
        cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)#转换颜色从BGR到RGBA
        current_image = Image.fromarray(cv2image)#将图像转换成Image对象
        imgtk = ImageTk.PhotoImage(image=current_image)
        panel.imgtk1 = imgtk
        panel.config(image=imgtk)
        root.after(1, video_loop)
    
    camera = cv2.VideoCapture(0)    #摄像头
    
    root22 = Tk()
    root22.title("opencv + tkinter")
    #root.protocol('WM_DELETE_WINDOW', detector)
    
    
    panel = Label(root22)  # initialize image panel
    panel.pack(padx=10, pady=10)
    # root.config(cursor="arrow")
    btn = Button(root22, text="点赞!", command=take_snapshot)
    btn.pack(fill="both", expand=True, padx=10, pady=10)
    
    video_loop()
    
    root22.mainloop()
    # 当一切都完成后，关闭摄像头并释放所占资源
    camera.release()
    cv2.destroyAllWindows()

#root19那里的图片位于 