# ! /usr/bin/python
#encoding:utf-8
__author__ = 'feng'
'''
http://www.gszadc.com/26212202.html
'''
import os, urllib2, re, time, MySQLdb, sys

reTitle = re.compile('<font[^>]*>(.*?)<\/font><font[^>]*')
reNeiron = re.compile('[1-9|A-Z|a-z].*')
retiqu = re.compile('^(?!MARGINWIDTH|BR).*.[^>|}]$')
rezhong = re.compile('^[^[].*')
shijian = 1190944000
Str1 = "\\n---------------- BLOG OF YAO"
bianhao = 2859
for i in range(1, 1500):
    Str2 = ""
    ltime = time.localtime(shijian)
    timeStr = time.strftime("%Y%m%d", ltime)
    url = "http://www.jokeswarehouse.com/cgi-bin/viewjoke2.cgi?id=%s" % timeStr
    print url
    a = urllib2.urlopen(url).read()
    Title = reTitle.findall(a)
    print "=========================================================================================================="
    for titles in map(None, Title):
        titles = MySQLdb.escape_string(titles)
        print titles
    Neiron = re.findall(reNeiron, a)
    for i in map(None, Neiron):
        x = re.findall(retiqu, i)
        for str in x:
            str = MySQLdb.escape_string(str)
            Str2 += str + "\\n"
    shijian += 86400
    bianhao += 1
    print Str2
    print titles
    # try:
    #     conn = MySQLdb.connect("XXXX.XXXX.XXXX.XXXX", "user", "passwd", "dbname", charset="utf8",
    #                            init_command="set names utf8")
    # except MySQLdb.OperationalError, message:
    #     print "like error"
    # cursor = conn.cursor()
    # sql = "INSERT INTO wp_posts (post_author,post_date,post_date_gmt,post_content,post_content_filtered,post_title,post_excerpt,post_status,post_type,comment_status,ping_status,post_password,post_name,to_ping,pinged,post_modified,post_modified_gmt,post_parent,menu_order,guid) VALUES (\'1\',\'2011-06-01 22:12:25\',\'2011-05-09 04:12:25\',\'\',\'\',\'Auto Draft\',\'\',\'inherit\',\'revision\',\'open\',\'open\',\'\',\'100-revision\',\'\',\'\',\'2011-06-01 22:12:25\',\'2011-05-09 04:12:25\',\'%s\',\'0\',\'\')" % bianhao
    # sql2 = "UPDATE wp_posts SET post_author = 1, post_date = \'2011-06-01 22:12:25\', post_date_gmt = \'2011-06-01 22:12:25\', post_content =\'%s\', post_content_filtered = \'\', post_title = \'%s\', post_excerpt = \'\', post_status = \'publish\', post_type = \'post\', comment_status = \'open\', ping_status = \'open\', post_password = \'\', post_name = \'%s\', to_ping = \'\', pinged = \'\', post_modified = \'2011-06-01 22:12:25\', post_modified_gmt = \'2011-05-09 04:12:30\', post_parent = 0, menu_order = 0, guid = \'http://www.moncleronlineshops.com/?p=%s\' WHERE ID = %s" % (
    # Str2, titles, titles, bianhao, bianhao)
    # cursor.execute(sql)
    # cursor.execute(sql2)
    # cursor.close()
    # conn.close()
    sys.exit()
