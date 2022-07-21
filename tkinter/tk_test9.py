from tkinter import *
from tkinter import messagebox

if messagebox.askokcancel('提示窗口','发射核弹？'):
    messagebox.showinfo(title='注意',message='发射成功')
    

mainloop()
