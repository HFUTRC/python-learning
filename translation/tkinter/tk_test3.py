from tkinter import *

def say_hi():
    var.set('来了老弟~')    

root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('笑脸')
textLabel = Label(frame1,textvariable=var,font=('微软雅黑',20))
textLabel.pack()

photo = PhotoImage(file='smile.gif')
imgLabel = Label(frame1,image = photo)
imgLabel.pack()

theButton = Button(frame2,text='打招呼',command=say_hi)
theButton.pack()

frame1.pack()
frame2.pack()

root.mainloop()
