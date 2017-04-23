# -*- coding: utf-8 -*-
import scrapy
from ..items import FirstscrapyItem


class LthSpider(scrapy.Spider):
    name = "lth"
    allowed_domains = ["sina.com.cn"]
    start_urls = ['http://slide.news.sina.com.cn/s/slide_1_2841_123175.html',
                  'http://slide.mil.news.sina.com.cn/k/slide_8_260_50032.html/d/#p=1',
                  'http://news.sina.com.cn/china/xlxw/2017-04-22/doc-ifyepsch2529468.shtml']

    def parse(self, response):
        item = FirstscrapyItem()
        item["urlname"] = response.xpath("/html/head/title/text()")
        print(item["urlname"])
