from tkinter import*

root = Tk()

def func1(event):
    print('点击位置：',event.x,event.y)
    
def func2(event):
    print(event.keysym)     #keysym为按键码

def func3(event):
    root.destroy()
    
def func4(event):
    print('您已成功退出程序')
    
frame = Frame(root,width=200,height=200)
#frame.bind('<Button-1>',func1)   #Button表示鼠标响应 '-1'左键 '-2'滚轮 '-3'右键
frame.bind('<Motion>',func1)    #Motion表示鼠标在组件内移动的整个过程均触发该事件
frame.bind('<Key>',func2)       #Key表示键盘响应，‘K’为大写
frame.bind('<KeyPress-Q>',func3)    #按特定的键进行响应
frame.bind('<Destroy>',func4)   #当组件被销毁时触发改事件
frame.focus_set()               #选中当前组件才能响应键盘

frame.pack()



root.mainloop()
