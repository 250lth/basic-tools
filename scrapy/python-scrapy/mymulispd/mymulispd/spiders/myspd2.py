# -*- coding: utf-8 -*-
import scrapy


class Myspd2Spider(scrapy.Spider):
    name = "myspd2"
    allowed_domains = ["sina.com.cn"]
    start_urls = ['http://sina.com.cn/']

    def parse(self, response):
        pass
