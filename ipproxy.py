import urllib.request

proxy_support=urllib.request.ProxyHandler({'http':'117.69.201.174	:9999'}) 
opener=urllib.request.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36')]
urllib.request.install_opener(opener)

respond=urllib.request.urlopen('https://www.whatismyip.com')
txt=respond.read().decode('utf-8')
print(txt)


