# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MangaCafeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    shop_name = scrapy.Field()
    shop_url = scrapy.Field()
    sheet_type = scrapy.Field()
    prices = scrapy.Field()

class MangaCafePrice(scrapy.Item):
    name = scrapy.Field()
    time = scrapy.Field()
    price = scrapy.Field()
