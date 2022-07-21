from tkinter import *

root = Tk()

def callback():
    print('你好')

menubar = Menu(root)


menubar.add_command(label='hello',command=callback)
menubar.add_command(label='quit',command=root.quit)

#root.config(menu=menubar)          置顶菜单

frame = Frame(root,width=512,height=512)
frame.pack()

def popup(event):
    menubar.post(event.x_root,event.y_root) #x_root，y_root表示相对于屏幕坐标

frame.bind('<Button-3>',popup)      #右键弹出菜单




root.mainloop()
