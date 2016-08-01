# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector

class LiangcuntuSpider(scrapy.Spider):
    name = "liangcuntu"
    allowed_domains = ["liangcuntu.com"]
    start_urls = (
        'http://www.liangcuntu.com/',
    )

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        print("===========")
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul/li')
        items = []
        for site in sites:
            print site.select('a/text()').extract()[0]
            print site.select('a/@href').extract()[0]
            print site.select('span/text()').extract()
        # return items