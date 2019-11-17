import urllib.request
import urllib.parse
import json
import time
import re
content='我真棒'
url='http://jandan.net/pic'
head={}
head['User-Agent']='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'


res=urllib.request.Request(url,None,head)
response=urllib.request.urlopen(res)
txt=response.read().decode('utf-8')

pattern=re.compile(r'//jandan\.net/pic/.{0,}#comments')
h=pattern.search(txt) 

#f=open('1.txt','w+')
#f.write(txt[a:b])
#f.close()
#pattern=r'//jandna\.net/pic/.{16}#comments'
#txt=re.match(pattern, txt)



