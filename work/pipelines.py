# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests
import pymysql

class WorkPipeline(object):
    def process_item(self, item, spider):
        return item
class TuchongPipeline(object):
    def process_item(self, item, spider):
        img_url = item['img_url'] #从items中得到图片url地址
        img_title= item['title'] #得到图片的名字
        headers = {
             'User-Agnet': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
             'cookie':'webp_enabled=1; bad_ide7dfc0b0-b3b6-11e7-b58e-df773034efe4=78baed41-a870-11e8-b7fd-370d61367b46; _ga=GA1.2.1188216139.1535263387; _gid=GA1.2.1476686092.1535263387; PHPSESSID=4k7pb6hmkml8tjsbg0knii25n6'
         }
        if not os.path.exists("picture"):
            os.mkdir("picture")
        filename = img_title
        with open("picture"+'/'+filename, 'wb+') as f:
            f.write(requests.get(img_url, headers=headers).content)
        f.close()
        return item
    
class TuchongsqlPipeline(object):
    #connect sql
    def __init__(self):
        self.connect = pymysql.connect(host = 'localhost', user = 'root', password = 'gentry',db = 'tupian',port = 3306)
        self.cursor=self.connect.cursor()
    def process_item(self,item,spider):
        self.cursor.execute('insert into tupian_table(name,url)VALUE("{}","{}")'.format(item['title'],item['img_url']))
        self.connect.commit()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()