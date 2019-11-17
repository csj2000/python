import urllib.request
import urllib.parse
import json
import time
while 1 :
    content=input('请输入你要翻译的句子(输入q结束程序)：')
    if content=='q' :
        break
    url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    head={}
    head['User-Agent']='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'

    data={}
    data['i']=content
    data['from']='zh-CHS'
    data['to']=' en'
    data['smartresult']='dict'
    data['client']='fanyideskweb'
    data['salt']=' 15727810828256'
    data['sign']=' d133624be87f3b50c44ed43c0fef23dc'
    data['ts']='1572781082825'
    data['bv']='7d4ac98e0e04505e57a74dd5992cc541'
    data['doctype']='json'
    data['version']=' 2.1'
    data['keyfrom']=' fanyi.web'
    data['action']=' FY_BY_CLICKBUTTION'
    data=urllib.parse.urlencode(data).encode('utf-8')
    res=urllib.request.Request(url,data,head)
    response=urllib.request.urlopen(res)
    txt=response.read().decode('utf-8')
    line=json.loads(txt)
    print(line["translateResult"][0][0]["tgt"])
    time.sleep(3)
