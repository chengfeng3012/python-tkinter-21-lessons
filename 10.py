from tkinter  import  *

def show(event):
      s = '滑块的取值为' + str(var.get())
      lb.config(text=s)

root = Tk()
root.title('滑块实验')
root.geometry('320x180')
var=DoubleVar()
scl = Scale(root,orient=HORIZONTAL,length=200,from_=1.0,to=5.0,label='请拖动滑块',tickinterval=1,resolution=0.05,variable=var)
scl.bind('<ButtonRelease-1>',show)
scl.pack()

lb = Label(root,text='')
lb.pack()

root.mainloop()
