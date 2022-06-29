from tkinter import *

def show(event):
    s = event.keysym
    lb.config(text=s)

root=Tk()
root.title('按键实验')
root.geometry('200x200')
lb=Label(root,text='请按键',font=('黑体',48))
lb.bind('<Key>',show)
lb.focus_set()
lb.pack()
root.mainloop()
