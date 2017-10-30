# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append("..")
from tutorial.models.bjjs_redis import BjjsRedis
from tutorial.componets.email_send import Email
reload(sys)
sys.setdefaultencoding( "utf-8" )

'''
# 自住型商品房 内容更新邮件通知
http://www.bjjs.gov.cn/bjjs/fwgl/zzxspzf/index.shtml
'''
class BjjsSpider(scrapy.Spider):
    name = "bjjs"
    allowed_domains = ["www.bjjs.gov.cn"]
    start_urls = (
        'http://www.bjjs.gov.cn/bjjs/xxgk/ztzl/gycqzf/index.shtml',
    )
    domains = "http://www.bjjs.gov.cn"
    def parse(self, response):
        print("crwwl start:--------------------------------------->")
        lis = response.xpath('//div[@id="tzgg1"]/ul[@class="ul_list"]/li')
        for index,li in enumerate(lis):
            if index>0:
                break
            title = li.xpath('a/text()').extract()[0]
            date_arr = li.xpath('span/text()').extract()
            # 对比是否最新消息，如果最新发邮件通知
            # 保存redis
            br = BjjsRedis()
            last_news = br.get("bjjs_last_news")
            if last_news != title+date_arr[0] :
                br.save("bjjs_last_news",title+date_arr[0])
                # 邮件通知
                print "email notice"
                email = Email()
                link = "<a href=\"http://www.bjjs.gov.cn/bjjs/xxgk/ztzl/gycqzf/index.shtml\">查看</a>"
                content  = title+link
                content = u''.join(content).encode('utf-8').strip()
                # Todo:1.字符编码√
                # Todo:2.发送html内容√
                if email.send_mail(["fengxuting@qq.com"],"共有产权房内容更新了",content):
                    print "send success"
                else:
                    print "send fail"
