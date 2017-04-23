# -*- coding: utf-8 -*-
import scrapy
from ..items import AutopjtItem
from scrapy.http import Request


class AutospdSpider(scrapy.Spider):
    name = "autospd"
    allowed_domains = ["dangdang.com"]
    start_urls = ['http://category.dangdang.com/pg1-cid10010056.html']

    def parse(self, response):
        item = AutopjtItem()
        item["name"] = response.xpath("//a[@class='pic']/@title").extract()
        item["price"] = response.xpath("//span[@class='price_n']/text()").extract()
        item["link"] = response.xpath("//a[@class='pic']/@href").extract()
        item["comnum"] = response.xpath("//a[@name='P_pl']/text()").extract()

        yield item

        for i in range (1, 76):
            url = "http://category.dangdang.com/pg" + str(i) + "-cid10010056.html"
            yield Request(url, callback=self.parse)
