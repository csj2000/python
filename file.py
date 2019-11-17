def download_mm(url,name):
    html=url_open(url)
    with open(name,'wb') as f:
        f.write(html)