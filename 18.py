#插入文件图片
import tkinter as tk
import os

path = os.getcwd()

root = tk.Tk()

#创建一个标签类, [justify]:对齐方式
textLabel = tk.Label(root,text="你在右边会看到一个图片，\n我在换个行",
justify = tk.LEFT)#左对齐
textLabel.pack(side=tk.LEFT)#自动对齐,side：方位

 

#创建一个图片管理类
photo = tk.PhotoImage(file=path + "/18.png")#file：t图片路径
imgLabel = tk.Label(root,image=photo)#把图片整合到标签类中
imgLabel.pack(side=tk.RIGHT)#自动对齐


tk.mainloop()
