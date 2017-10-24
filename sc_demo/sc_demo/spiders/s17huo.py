# -*- coding: utf-8 -*-
import scrapy


class S17huoSpider(scrapy.Spider):
    name = 's17huo'
    allowed_domains = ['17huo.com']
    start_urls = ['http://17huo.com/']

    def parse(self, response):
        pass
