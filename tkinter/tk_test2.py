import tkinter as tk

class App:
    def __init__(self,master):
        fra = tk.Frame(master,height='20',width='400',bg='blue')
        fra.pack(side=tk.LEFT,padx=100,pady=100)

        self.hi_there = tk.Button(fra,text='打招呼',bg='green',fg='red',command=self.say_hi)
        self.hi_there.pack()

    def say_hi(self):
        print('来了老弟~')

root = tk.Tk()
root.title('MyGui')

app = App(root)

root.mainloop()
