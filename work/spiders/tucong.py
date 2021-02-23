# -*- coding: utf-8 -*-
import scrapy


class TucongSpider(scrapy.Spider):
    name = "tucong"
    allowed_domains = ["tucong.com"]
    start_urls = ['http://tucong.com/']

import scrapy
import json
from work.items import TuchongItem


class TuchongSpider(scrapy.Spider):
    name = 'tuchong'
    allowed_domains = ['tuchong.com']
    start_urls = ['http://tuchong.com/']

    def start_requests(self):
        for pag in range(1, 20):
            referer_url = 'https://tuchong.com/rest/tags/自然/posts?page={}&count=20'.format(pag)   # url中红字部分可以换
            form_req = scrapy.Request(url=referer_url, callback=self.parse)
            form_req.headers['referer'] = referer_url
            yield form_req

    def parse(self, response):
        tuchong_info_html = json.loads(response.text)
        # print(tuchong_info_html)
        postList_c = len(tuchong_info_html['postList'])
        # print(postList_c)
        for c in range(postList_c):
            print(c)
            # print(tuchong_info_html['postList'][c])
            title = tuchong_info_html['postList'][c]['title']
            print('图集名称:'+title)
            views = tuchong_info_html['postList'][c]['views']
            print('有'+str(views)+'人浏览')
            favorites = tuchong_info_html['postList'][c]['favorites']
            print('喜欢的人数:'+str(favorites))
            images_c = len(tuchong_info_html['postList'][c]['images'])
            for img_c in range(images_c):
                user_id = tuchong_info_html['postList'][c]['images'][img_c]['user_id']
                img_id = tuchong_info_html['postList'][c]['images'][img_c]['img_id']
                img_url = 'https://photo.tuchong.com/{}/f/{}.jpg'.format(user_id,img_id)
                item = TuchongItem()
                item['title'] = title
                item['img_url'] = img_url
            # 返回我们的item
                yield item
