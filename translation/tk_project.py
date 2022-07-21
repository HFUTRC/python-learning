import urllib.request as r
import urllib.parse as p
import json
from tkinter import *

def translate():
    content = t1.get(0.0,END)
    
    url = 'http://fanyi.youdao.com/translate'

    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    
    data = {}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] =  'AUTO'
    data['smartresult'] ='dict'
    data['client'] = 'fanyideskweb'  
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] ='fanyi.web'
    data['action'] = 'FY_BY_REALTlME'

    data = p.urlencode(data).encode('utf-8')
    req = r.Request(url,data,head)
    response = r.urlopen(req)
    html = response.read().decode('utf-8')

    target = json.loads(html)
    translation=target['translateResult'][0][0]['tgt']
    
    t2.delete(0.0,END)
    t2.insert(INSERT,translation)
    


root = Tk()
root.title('简易翻译器')
root.geometry('780x250')

Label(root,text='请输入你要翻译的内容：',font=('微软雅黑',15))\
        .grid(row=0,column=0,sticky=W,padx=20)
Label(root,text='翻译结果为：',font=('微软雅黑',15))\
        .grid(row=0,column=1,sticky=W,padx=60)

v1 = StringVar()

t1 = Text(root,width=38,height=8,font=('consolas',12))
t2 = Text(root,width=38,height=8,font=('consolas',12))
t1.grid(row=1,column=0,padx=5)
t2.grid(row=1,column=1,padx=30)

Button(root,text='翻译',width=10,command=translate)\
        .grid(row=3,column=1,sticky=E,padx=200,pady=10)
Button(root,text='退出',width=10,command=root.quit)\
        .grid(row=3,column=1,sticky=E,padx=100,pady=10)


root.mainloop()
