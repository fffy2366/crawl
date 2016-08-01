import urllib2
import re

url = 'http://www.jokeji.cn/list.htm'

req = urllib2.Request(url)
con = urllib2.urlopen(req)
doc = con.read()
con.close()

links = re.findall(r'href\=\"(http\:\/\/[a-zA-Z0-9\.\/]+)\"', doc)
for a in links:
    print a