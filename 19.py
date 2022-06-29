import tkinter as tk
import os

root = tk.Tk()
path = os.getcwd() + '/'

#增加背景图片
photo = tk.PhotoImage(file=path + "18.png")
theLabel = tk.Label(root,
text="我是内容,\n请你阅读",#内容
justify=tk.LEFT,#对齐方式
image=photo,#加入图片
compound = tk.CENTER,#关键:设置为背景图片
font=("华文行楷",20),#字体和字号
fg = "white")#前景色
theLabel.pack()

 

tk.mainloop()
