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
from tutorial.items import JokeItem
'''
# 自住型商品房
http://www.bjjs.gov.cn/bjjs/fwgl/zzxspzf/index.shtml
'''
class BjjsSpider(scrapy.Spider):
    name = "bjjs"
    allowed_domains = ["www.bjjs.gov.cn"]
    start_urls = (
        'http://www.bjjs.gov.cn/bjjs/fwgl/zzxspzf/index.shtml',
    )
    domains = "http://www.bjjs.gov.cn"
    def parse(self, response):
        # filename = response.url.split("/")[-2] + '.html'
        print("crwwl start:--------------------------------------->")
        lis = response.xpath('//div[@class="tzgg_list_box"]/ul/li')
        for index,li in enumerate(lis):
            title = li.xpath('a/text()').extract()[0]
            date = li.xpath('span/text()').extract()[0]
            # print title
            # print date
            # 对比是否最新消息，如果最新发邮件通知
            # 保存redis
            


    