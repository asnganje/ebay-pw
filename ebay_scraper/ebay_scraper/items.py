# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass

import scrapy


@dataclass
class EbayScraperItem:
    # define the fields for your item here like:
    # name: str | None = None
    pass
class EbayItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    condition = scrapy.Field()
    quantity = scrapy.Field()
    product_url = scrapy.Field()