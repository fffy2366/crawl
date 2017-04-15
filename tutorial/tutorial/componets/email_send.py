#!/usr/bin/env python
# -*- coding: utf-8 -*-
#导入smtplib和MIMEText
#http://blog.csdn.net/stonexing5/article/details/6371605
#[python发送各类邮件的主要方法](http://www.cnblogs.com/xiaowuyi/archive/2012/03/17/2404015.html)
#[python发送邮件的实例代码(支持html、图片、附件)](http://www.jb51.net/article/34498.htm)
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
sys.path.append("../../..")
from config.config import Config
conf = Config()
configs = conf.getConfig()
class Email():
    def send_mail(self,to_list,sub,content):
        '''
        to_list:发给谁
        sub:主题
        content:内容
        send_mail("aaa@126.com","sub","content")
        '''
        msgAlternative = MIMEMultipart('alternative')
        me=configs.MAIL['user']+"<"+configs.MAIL['user']+"@"+configs.MAIL['postfix']+">"
        # msg = MIMEText(content)
        #设定HTML信息
        msg = MIMEText(content, 'html', 'utf-8')
        msgAlternative.attach(msg)

        msg['Subject'] = sub #设置主题
        msg['From'] = "Frank<frank.feng@liangcuntu.com>"     #发件人
        msg['To'] = ";".join(to_list) #收件人
        #print msg ;
        try:
            s = smtplib.SMTP()
            s.connect(configs.MAIL['host'])
            s.login(configs.MAIL['user'],configs.MAIL['pass'])
            s.sendmail(me, to_list, msg.as_string())
            s.close()
            return True
        except Exception, e:
            print str(e)
            return False

if __name__ == '__main__':
    pass
    #要发给谁，这里发给1个人
    # mailto_list=["fengxuting@qq.com"]
    # email = Email()
    # if email.send_mail(mailto_list,"你好我是frank","很高兴通知您，网站内容有更新，请查看！"):
    #     print "发送成功"
    # else:
    #     print "发送失败"
