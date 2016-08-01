# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from os import path
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
import sqlite3

class TutorialPipeline(object):
    def process_item(self, item, spider):
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