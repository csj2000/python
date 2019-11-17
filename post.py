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

