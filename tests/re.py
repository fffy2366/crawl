#-*-coding:utf-8-*-
#用正则简单过滤html的<>标签
import re
str = "<img /><a>srcd</a>hello</br><br/>"
str = re.sub(r'</?\w+[^>]*>','',str)
print str

str = "<img /><a>srcd</a>hello</br><br/>"
print re.sub(r'<a>.*</a>','',str)