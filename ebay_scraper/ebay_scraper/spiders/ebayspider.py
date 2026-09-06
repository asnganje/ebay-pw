import scrapy
from ..items import EbayItem


class EbayspiderSpider(scrapy.Spider):
    name = "ebayspider"
    async def start(self):
        url = ("https://www.ebay.com/sch/i.html?_dcat=177&_fsrp=1&rt=nc&_from=R40&RAM%2520Size=32%2520GB&_nkw=laptop+computers+ram+32gb&_sacat=0&SSD%2520Capacity=1%2520TB")
        yield scrapy.Request(
            url=url,
            meta={"playwright": True}
        )
    def parse(self, response):
        laptop_links = response.css("div.su-card-container__header a::attr(href)").getall()
        for link in laptop_links:
            if "/itm" not in link:
                continue
            yield scrapy.Request(
                url = link,
                callback = self.parse_product,
                meta = {"playwright": True}
            )
    def parse_product(self, response):
        ebay_itm = EbayItem()
        name = response.css("span.ux-textspans.ux-textspans--BOLD::text").get()
        price = response.xpath("//span[@class='x-price-primary__price']/span[@class='ux-textspans']/text()").get()
        condition = response.xpath("//span[@data-testid='ux-textual-display']/span[@class='ux-textspans']/text()").get()
        quantity = response.css("input#qtyTextBox::attr(value)").get()
        product_url = response.url
        ebay_itm['name'] = name
        ebay_itm['price'] = price
        ebay_itm['condition'] = condition
        ebay_itm['quantity'] = quantity
        ebay_itm['product_url'] = product_url
        yield ebay_itm
