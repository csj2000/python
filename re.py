import re

def re_txt(pattern, str):
    obj=re.search(pattern, str)
    txt1=obj.group()
    print(txt1)
    return txt1

