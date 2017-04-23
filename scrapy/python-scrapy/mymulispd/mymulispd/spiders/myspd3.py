# -*- coding: utf-8 -*-
import scrapy


class Myspd3Spider(scrapy.Spider):
    name = "myspd3"
    allowed_domains = ["sina.com.cn"]
    start_urls = ['http://sina.com.cn/']

    def parse(self, response):
        pass
