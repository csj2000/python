import urllib.request
import json
import re
import urllib.parse

def re_txt(pattern, str):
    obj=re.search(pattern, str)
    txt1=obj.group()
    print(txt1)
    return txt1

def url_open(url):
    res=urllib.request.Request(url)
    res.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36')
    respond=urllib.request.urlopen(res)
    html=respond.read()
    return html

def page_url(url):
    html=url_open(url).decode('utf-8')
    tip=re_txt(r'//jandan\.net/pic/.{0,}#comments',html)
    return 'http:'+tip


def src_url(url):
    html=url_open(url).decode('utf-8')
    tip=re_txt(r'//wx[0-9]\.sinaimg\.cn/mw600/.{0,}\.jpg',html)
    return 'http:'+tip

def download_mm(url):
    html=url_open(url)
    with open("mm_img.jpg",'wb') as f:
        f.write(html)

url='http://jandan.net/pic'

pageurl=page_url(url)
srcurl=src_url(pageurl)
download_mm(srcurl)
