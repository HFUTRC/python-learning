from tkinter import *

root = Tk()
root.title('My Window')
root.geometry('500x300')

MOVIES = ['寄生虫','升级','小偷家族','燃烧']

v = []

for movie in MOVIES:
    v.append(IntVar())
    b = Checkbutton(root,text = movie,variable=v[-1])#v[-1]表示列表最后一个元素
    b.pack(anchor=W)

root.mainloop()

