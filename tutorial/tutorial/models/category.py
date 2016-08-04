#!bin/evn python
# -*-coding:utf8-*-
import datetime
import sys

from mysql import MySQL

reload(sys)
sys.setdefaultencoding('utf-8')

class Category:
    def insert(self,d):
        n = MySQL()

        n.selectDb('joke')
        tbname = 'category'
        ret = n.insert(tbname, d)
        n.commit()
        return ret
    def findByTitle(self,v):
        n = MySQL()

        n.selectDb('joke')
        tbname = 'category'
        n.query("select * from %s where title = '%s'" %(tbname,v))
        return n.fetchAll()
    def findAll(self):
        n = MySQL()

        n.selectDb('joke')
        tbname = 'category'
        # n.query("select name from %s where updated_at <'2016-06-27 00:00:00'" %(tbname) )
        # n.query("select name from %s where is_face!=1 " %(tbname) )
        n.query("select title from %s " %(tbname) )
        return n.fetchAll()
    def updateCategory(self,title,content):
        n = MySQL()
        n.selectDb('joke')
        tbname = 'category'
        n.update(tbname, { 'title': title}, "content='"+content+"'")
        n.commit()

if __name__ == '__main__':
    c = Category()
    # print(c.insert({'title':'test','created_at':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}))
    print c.findByTitle("test")
