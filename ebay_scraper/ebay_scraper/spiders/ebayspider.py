import scrapy


class EbayspiderSpider(scrapy.Spider):
    name = "ebayspider"
    allowed_domains = ["ebay.com"]
    start_urls = ["https://ebay.com"]

    def parse(self, response):
        pass
