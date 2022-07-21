import urllib.request as r
import urllib.parse as p
import json

def translate(content):
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

    #print(html)

    target = json.loads(html)
    print('翻译结果：%s'%(target['translateResult'][0][0]['tgt']))

if __name__ == '__main__':
    while(True):
        content = input('请输入需要翻译的内容(输入q退出)：')
        if(content == 'q'):
            break
        translate(content)

        
