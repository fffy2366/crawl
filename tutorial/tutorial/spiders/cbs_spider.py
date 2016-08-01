#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from tutorial.items import CnbetaItem
class CBSpider(CrawlSpider):
    name = 'cnbeta'
    allowed_domains = ['cnbeta.com']
    start_urls = ['http://www.jb51.net']
    rules = (
        Rule(LinkExtractor(allow=('/articles/.*\.htm', )),
             callback='parse_page', follow=True),
    )
    def parse_page(self, response):
        item = CnbetaItem()
        sel = Selector(response)
        item['title'] = sel.xpath('//title/text()').extract()
        item['url'] = response.url
        return item