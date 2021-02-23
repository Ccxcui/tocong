# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WorkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class TuchongItem(scrapy.Item):
    title = scrapy.Field() #图片名字
    views = scrapy.Field() #浏览人数
    favorites = scrapy.Field()#点赞人数
    img_url = scrapy.Field()#图片地址