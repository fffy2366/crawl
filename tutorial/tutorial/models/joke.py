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
    def findByTitleDate(self,title,created_at):
        n = MySQL()

        n.selectDb('joke')
        tbname = 'joke'
        n.query("select id from %s where title = '%s' and created_at= '%s'" %(tbname,title,created_at))
        return n.fetchAll()
    def findById(self,v):
        n = MySQL()

        n.selectDb('joke')
        tbname = 'joke'
        n.query("select j.id, j.title,j.content,j.created_at,j.category_id,c.title ctitle from %s j left join category c on j.category_id=c.category_id where j.id = %s" %(tbname,v))
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
        n = MySQL()
        currRow = (int(page)-1)*int(limit)
        n.selectDb('joke')
        tbname = 'joke'
        print "currRow:"+str(currRow)
        sqlCount = "SELECT FOUND_ROWS() c" ;
        sql = "select j.id, j.title,j.created_at,c.title ctitle from %s j left join category c on j.category_id=c.category_id where 1=1 and j.content!='' order by j.created_at desc limit %s,%s" %(tbname,currRow,limit)
        print sql
        n.query(sql)
        ret = n.fetchAll()
        n.query(sqlCount)
        # totalCount = n.fetchAll()
        totalCount = self.findCount(query)
        print "totalCount:"
        print totalCount
        print len(ret)
        return ret,totalCount
        # return ret,totalCount[0]['c']
        # return ret,10000

    def findCount(sefl,query):
        n = MySQL()
        n.selectDb('joke')
        tbname = 'joke'
        sqlCount = "SELECT count(id) c from %s" %(tbname) ;
        n.query(sqlCount)
        totalCount = n.fetchAll()
        return totalCount[0]['c']
if __name__ == '__main__':
    j = Joke()
    # j.insert({'title':'test','category_id':'1','content':'乱码','created_at':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    # j.list(1,10,"")
    print len(j.findByTitleDate('个个草包','2008-10-06 00:00:00'))