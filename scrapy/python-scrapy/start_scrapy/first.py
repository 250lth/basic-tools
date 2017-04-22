from scrapy.spiders import Spider


class FirstSpider(Spider):
    name = "first"
    allowed_domains = ["baidu.com"]
    start_urls = [
        "http://www.baidu.com"
    ]

    def parse(self, response):
        pass