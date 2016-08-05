#!bin/evn python
# -*-coding:utf8-*-
import datetime
import sys

from mysql import MySQL

reload(sys)
sys.setdefaultencoding('utf-8')

class Joke:
    def insert(self,d):
        n = MySQL()

        n.selectDb('joke')
        tbname = 'joke'
        n.insert(tbname, d)
        n.commit()
    def findByTitle(self,v):
        n = MySQL()

        n.selectDb('joke')
        tbname = 'joke'
        n.query("select name from %s where title = %s" %(tbname,v))
        return n.fetchAll()
    def findAll(self):
        n = MySQL()

        n.selectDb('joke')
        tbname = 'joke'
        # n.query("select name from %s where updated_at <'2016-06-27 00:00:00'" %(tbname) )
        # n.query("select name from %s where is_face!=1 " %(tbname) )
        n.query("select name from %s " %(tbname) )
        return n.fetchAll()
    def updateJoke(self,title,content):
        n = MySQL()
        n.selectDb('joke')
        tbname = 'joke'
        n.update(tbname, { 'title': title}, "content='"+content+"'")
        n.commit()
    def list(self,page, limit, query):
        return [],10

if __name__ == '__main__':
    j = Joke()
    j.insert({'title':'test','category_id':'1','content':'乱码','created_at':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
