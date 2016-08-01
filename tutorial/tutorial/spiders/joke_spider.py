# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
import re
from scrapy.http import Request
import os
import urllib2

class LiangcuntuSpider(scrapy.Spider):
    name = "joke"
    allowed_domains = ["jokeji.cn"]
    start_urls = (
        'http://www.jokeji.cn/list.htm',
    )
    domains = "http://www.jokeji.cn"
    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        print("===========")
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        #selector = scrapy.Selector(response)
        # sites = selector.xpath('//div[@class="list_title"]/text()').extract()
        # print sites
        # lis = response.xpath('//div[@class="list_title"]/ul/li').extract()
        lis = response.xpath('//div[@class="list_title"]/ul/li')
        # print lis
        '''
        <li><b><a href="/jokehtml/fq/2016062923543272.htm" target="_blank">夫妻的幽默PK</a></b><span>浏览：8993次</span><i>2016-6-29</i></li>
        '''
        for index,li in enumerate(lis):
            # print li.extract()
            title = li.xpath('b/a/text()').extract()[0]
            # print li.xpath('b/a/@href').extract()
            #链接
            link = self.domains+li.xpath('b/a/@href').extract()[0]
            # print li.xpath('b/a/@href').extract()
            #日期
            date = li.xpath('i/text()').extract()[0]
            # print date
            #浏览量 分清encode和decode。str --> decode(c) --> unicode, unicode --> encode(c) --> str，其中编码类型c必须相同。
            viewcount = li.xpath('span/text()').extract()[0] ;
            viewcount = viewcount.encode('utf-8').replace("浏览：","").replace("次","")
            args = (index,title,link,date,viewcount)

            # print "\n"
            # print args[2]
            # print 'Li number %d title: %s , link: %s , date: %s,view count: %s' % args
            # 抓取内容
            yield Request(link, callback=self.parse_detail)
            # if link == 'http://www.jokeji.cn/jokehtml/bxnn/2016070414034214.htm':
            #     yield Request(link, callback=self.parse_detail)


    def parse_detail(self,response):
        div_left_up = response.xpath('//div[@class="left_up"]')
        category = div_left_up.xpath('h1/a/text()').extract()[1]
        content = div_left_up.xpath('ul/span[2]/p').extract()
        img = div_left_up.xpath('ul/span[2]/p/img/@src').extract()
        print("-----"+category)
        print("".join(content))
        print("-----"+img[0] if img else "")
        if img:
            if not img[0].find("http") == -1:
                self.download_img(img[0])

    # 根据链接获取图片名称、路径
    def get_img_name(self,src):
        l = src.split("/")
        host = "/".join(l[0:3])
        filename =  l[-1]
        dirname =  "/".join(l[3:-1])
        path = "/".join(l[3:])
        return (host,dirname,filename,path)
    # 下载图片
    def download_img(self,picurl):
        args = self.get_img_name(picurl)
        save_path = os.path.abspath(os.curdir)+"/"+args[1]
        print save_path
        if(not os.path.isdir(save_path)):
            self.mkdirs(save_path)

        req = urllib2.Request(picurl)
        #解决防盗链问题
        req.add_header('Referer','http://www.jokeji.cn/')

        imgData = urllib2.urlopen(req).read()
        # 给定图片存放名称
        print args[3]
        # 文件名是否存在
        if not os.path.exists(args[3]):
            output = open(args[3], 'wb+')
            output.write(imgData)
            output.close()
            print "Finished download \n"
        print "运行完成"

    ### 创建多层目录
    def mkdirs(self,path):
        # 去除首位空格
        path=path.strip()
        # 去除尾部 \ 符号
        path=path.rstrip("\\")

        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists=os.path.exists(path)

        # 判断结果
        if not isExists:
            # 创建目录操作函数
            os.makedirs(path)
            # 如果不存在则创建目录
            print path + u' 创建成功'
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print path + u' 目录已存在'
            return False

