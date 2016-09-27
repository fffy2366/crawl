# ! /usr/bin/python
#-*-coding:utf-8-*-
import sys
import re
import datetime
sys.path.append("..")
from tutorial.tutorial.models.joke import Joke

class Tool():
    def findAll(self):
        j = Joke()
        list = j.findAll()
        return list
    def replaceA(self,str):
        return re.sub(r'<a .*>.*</a>','',str)
    def deal(self,jokes):
        j = Joke()
        for joke in jokes:
            # print j
            content = self.replaceA(joke['content'])
            # 更新
            j.updateJoke(content,joke['id'])
    def htmlspecialchars(self,text):
        return (
            text.replace("&", "&amp;").
            replace("'", "&#039;").
            replace('"', "&quot;").
            replace("<", "&lt;").
            replace(">", "&gt;")
        )
    def main(self):
        list = self.findAll()
        self.deal(list)

if __name__=="__main__":
    t = Tool()
    t.main()
    print "finish"
    print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
