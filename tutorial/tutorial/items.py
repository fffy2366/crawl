# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
class FjsenItem(scrapy.Item):
    title=scrapy.Field()
    link=scrapy.Field()
    addtime=scrapy.Field()

class JokeItem(scrapy.Item):
    title=scrapy.Field()
    link=scrapy.Field()
    addtime=scrapy.Field()

class CnbetaItem(scrapy.Item):
    title=scrapy.Field()
    url=scrapy.Field()

class MyItem(scrapy.Item):
    id=scrapy.Field()
    name=scrapy.Field()
    description=scrapy.Field()