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
        n.query("select j.id, j.title,j.content,j.view_count,j.created_at,j.category_id,c.title ctitle from %s j left join category c on j.category_id=c.category_id where j.id = %s" %(tbname,v))
        return n.fetchAll()
    def findAll(self):
        n = MySQL()

        n.selectDb('joke')
        tbname = 'joke'
        # n.query("select name from %s where updated_at <'2016-06-27 00:00:00'" %(tbname) )
        # n.query("select name from %s where is_face!=1 " %(tbname) )
        n.query("select * from %s " %(tbname) )
        return n.fetchAll()
    def updateJoke(self,content,id):
        n = MySQL()
        n.selectDb('joke')
        tbname = 'joke'
        n.update(tbname, { 'content': content}, "id='"+id+"'")
        n.commit()
    def addViewCount(self,id):
        n = MySQL()
        n.selectDb('joke')
        tbname = 'joke'
        sql = "update {0} set view_count = view_count+1".format(tbname)
        n.query(sql)
        # n.update(tbname, { 'view_count': "view_count+1"}, "id='"+id+"'")
        n.commit()
    def list(self,page, limit, cid,menu):
        n = MySQL()
        currRow = (int(page)-1)*int(limit)
        n.selectDb('joke')
        tbname = 'joke'
        print "currRow:"+str(currRow)
        conditions = (tbname,)
        sqlCount = "SELECT FOUND_ROWS() c"
        sql = "select j.id, j.title,j.view_count,j.created_at,c.title ctitle from %s j left join category c on j.category_id=c.category_id where 1=1 and j.content!='' "
        if(cid):
            print "cid:"+cid
            sql += " AND j.category_id = %s"
            conditions = conditions + (cid ,)
        print "conditions:"+str(conditions)
        conditions = conditions+(currRow,limit)
        if(menu=="latest"):
            sql += " order by j.created_at desc,j.id desc "
        elif(menu=="hot"):
            sql += " order by j.view_count desc,j.id desc "
        sql += " limit %s,%s"
        print "conditions:"+str(conditions)

        sql = sql % conditions
        print sql
        n.query(sql)
        ret = n.fetchAll()
        n.query(sqlCount)
        # totalCount = n.fetchAll()
        totalCount = self.findCount(cid)
        print "totalCount:"
        print totalCount
        print len(ret)
        return ret,totalCount
        # return ret,totalCount[0]['c']
        # return ret,10000

    def findCount(sefl,cid):
        n = MySQL()
        n.selectDb('joke')
        tbname = 'joke'
        conditions = (tbname,)
        sqlCount = "SELECT count(id) c from %s where content!=''"
        if(cid):
            sqlCount += " AND category_id = %s"
            conditions = conditions+(cid ,)
        sqlCount = sqlCount % conditions
        n.query(sqlCount)
        totalCount = n.fetchAll()
        return totalCount[0]['c']
    def prev_next(self,type,joke,order):
        n = MySQL()
        n.selectDb('joke')
        tbname = 'joke'
        # 按日期
        if type=="prev" and order=="date":
            sql = "select * from {0} where content!='' and id> {1} and created_at>='{2}'".format(tbname,joke['id'],joke['created_at'])

            orders = " order by created_at asc,id asc limit 1"
        if type=="next" and order=="date":
            sql = "select * from {0} where content!='' and id< {1} and created_at<='{2}'".format(tbname,joke['id'],joke['created_at'])

            orders = " order by created_at desc,id desc limit 1"
        #按分类
        if type=="prev" and order=="cate":
            sql = "select * from {0} where content!='' and id> {1} and created_at>='{2}' and category_id={3}".format(tbname,joke['id'],joke['created_at'],joke['category_id'])

            orders = " order by created_at asc,id asc limit 1"
        if type=="next" and order=="cate":
            sql = "select * from {0} where content!='' and id< {1} and created_at<='{2}' and category_id={3}".format(tbname,joke['id'],joke['created_at'],joke['category_id'])

            orders = " order by created_at desc,id desc limit 1"

        print "".join([sql,orders])
        n.query("".join([sql,orders]))
        joke = n.fetchRow()
        return joke

if __name__ == '__main__':
    j = Joke()
    # j.insert({'title':'test','category_id':'1','content':'乱码','created_at':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    # j.list(1,10,"")
    print len(j.findByTitleDate('个个草包','2008-10-06 00:00:00'))