# -*-coding:utf-8-*-
__author__ = 'feng'
import urllib
import urllib2
import os

picurl = "http://images.51cto.com/files/uploadimg/20100630/104906665.jpg"
picurl = "http://gaoxiao.jokeji.cn/upfilesnew/pig.jpg"
save_path = os.path.abspath(os.curdir)
print save_path
req = urllib2.Request(picurl)
req.add_header('Referer','http://www.jokeji.cn/')
imgData = urllib2.urlopen(req).read()

# 给定图片存放名称
fileName = save_path + "/ddd.jpg"
print fileName
# 文件名是否存在
if not os.path.exists(fileName):
    output = open(fileName, 'wb+')
    output.write(imgData)
    output.close()
    print "Finished download \n"
print "运行完成"
