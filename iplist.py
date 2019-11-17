import urllib.request
import urllib.parse
import json
import time
import re


def url_open(url):
    res=urllib.request.Request(url)
    res.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36')
    respond=urllib.request.urlopen(res)
    html=respond.read()
    return html


ip1=[]
ip2=[]
ip3=[]
ip=[]
url='https://www.xicidaili.com'
txt=url_open(url).decode('utf-8')
pattern1=r'<td>([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})</td>'
pattern2=r'<td>([0-9]{4,5})</td>'
pattern3=r'<td>(HTTPS{0,1})</td>'
obj1=re.finditer(pattern1, txt)
obj2=re.finditer(pattern2, txt)
obj3=re.finditer(pattern3, txt)
for mat in obj1:
    ip1.append(mat.group()[4:-5])
for mat in obj2:
    ip2.append(mat.group()[4:-5])
for mat in obj3:
    ip3.append(mat.group()[4:-5])
for i in range(len(ip3)):
    ip.append(ip1[i]+':'+ip2[i]+','+ip3[i])

    

