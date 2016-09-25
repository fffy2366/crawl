import re, urllib
htmlSource = urllib.urlopen("http://www.sharejs.com").read(200000)
linksList = re.findall('<a href=(.*?)>.*?</a>',htmlSource)
for link in linksList:
    print link