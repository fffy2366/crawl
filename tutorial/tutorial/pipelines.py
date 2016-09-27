# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from os import path
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
import sqlite3
from models.category import Category
from models.joke import Joke
import datetime
import re

class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

class JokePipeline(object):
    def process_item(self, item, spider):
        # print item
        category = item['category'] 
        title = item['title'] 
        content = item['content'] 
        view_count = item['view_count'] 
        link = item['link'] 

        created_at = item['created_at'] 
        updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #Todo: 保存分类和内容
        c = Category()
        # 查找分类是否存在，不存在则插入
        categoryModel = c.findByTitle(item['category'])
        if(categoryModel):
            category_id = categoryModel[0]["category_id"]
        else:
            category_id = c.insert({'title':category,'created_at':updated_at,'updated_at':updated_at})

        j = Joke()
        #根据标题和日期查找该数据是否存在，不存在才保存
        # print "len--------->:"
        # print len(j.findByTitleDate(title,created_at+" 00:00:00"))
        if(len(j.findByTitleDate(title,created_at+" 00:00:00"))<1):
            contentStr = ''.join(content)
            contentStr = re.sub(r'<a .*>.*</a>','',contentStr)
            j.insert({'title':title,'category_id':category_id,'content':contentStr,'link':link,'view_count':int(view_count),'created_at':created_at+" 00:00:00",'updated_at':updated_at})
        return item
        
class FjsenPipeline(object):
    filename = './data.sqlite'
    def __init__(self):
        self.conn=None
        dispatcher.connect(self.initialize,signals.engine_started)
        dispatcher.connect(self.finalize,signals.engine_stopped)
    def process_item(self,item,spider):
        # print("==="+item['title'][0])
        # print("==="+item['link'][0])
        # print("==="+item['addtime'][0])
        # self.conn.execute('insert into fjsen values(?,?,?,?)',(None,item['title'][0],'http://www.jb51.net/'+item['link'][0],item['addtime'][0]))
        self.conn.execute('insert into fjsen values(?,?,?,?)',(None,item['title'][0],'http://www.jb51.net/'+item['link'][0],""))
        return item
    def initialize(self):
        if path.exists(self.filename):
            self.conn=sqlite3.connect(self.filename)
        else:
            self.conn=self.create_table(self.filename)
    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn=None
    def create_table(self,filename):
        conn=sqlite3.connect(filename)
        conn.execute("""create table fjsen(id integer primary key autoincrement,title text,link text,addtime text)""")
        conn.commit()
        return conn