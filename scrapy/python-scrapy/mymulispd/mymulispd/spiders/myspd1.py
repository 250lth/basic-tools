# -*- coding: utf-8 -*-
import scrapy


class Myspd1Spider(scrapy.Spider):
    name = "myspd1"
    allowed_domains = ["sina.com.cn"]
    start_urls = ['http://sina.com.cn/']

    def parse(self, response):
        pass
