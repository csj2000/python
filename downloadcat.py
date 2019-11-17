import urllib.request
url="http://placekitten.com/g/200/300"
response=urllib.request.urlopen(url)
cat_img=response.read()

with open("cat_img.jpg",'wb') as f:
    f.write(cat_img)
