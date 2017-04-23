# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from ..items import MyxmlItem


class PersonSpider(XMLFeedSpider):
    name = 'person'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/test.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'person' # change it accordingly

    def parse_node(self, response, selector):
        i = MyxmlItem()
        #i['url'] = selector.select('url').extract()
        #i['name'] = selector.select('name').extract()
        #i['description'] = selector.select('description').extract()
        i['link'] = selector.xpath('/person/email/text()').extract()
        print(i['link'])
        return i
