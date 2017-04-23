# -*- coding: utf-8 -*-
import scrapy


class LthSpider(scrapy.Spider):
    name = "lth"
    allowed_domains = ["iqianyue.com"]
    start_urls = ['http://iqianyue.com/']

    def parse(self, response):
        pass
