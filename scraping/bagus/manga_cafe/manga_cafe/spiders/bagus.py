# -*- coding: utf-8 -*-
import scrapy

from manga_cafe.items import MangaCafeItem, MangaCafePrice

class BagusSpider(scrapy.Spider):
    name = 'bagus'
    allowed_domains = ['www.bagus-99.com']
    start_urls = ['https://www.bagus-99.com/shops/']

    def parse(self, response):
        for url in response.css('#sideShopArea > div.box > ul:nth-child(6) a::attr("href")').extract():
            yield scrapy.Request(response.urljoin(url), self.parse_shop)

        for url in response.css('#sideShopArea > div.box > ul:nth-child(8) a::attr("href")').extract():
            yield scrapy.Request(response.urljoin(url), self.parse_shop)
    
    def parse_shop(self, response):
        shop_name = response.css('title ::text').extract_first().split('｜')[0].split('　')[1].replace('詳細','')
        shop_url = response.url

        tables = response.xpath('//table')
        for table in tables:
            item = MangaCafeItem()
            item['shop_name'] = shop_name
            item['shop_url'] = shop_url
            item['sheet_type'] = table.css('td.col1 ::text').extract()

            price_list = []
            for tr in table.xpath('tr'):
                title = tr.css('td.col2 ::text').extract_first() if tr.css('td.col2 ::text').extract_first() is not None else ''
                price = tr.css('td.col3 div.miniRight ::text').extract_first() if tr.css('td.col3 div.miniRight ::text').extract_first() is not None else ''
                time = tr.css('td.col3 div.miniLeft ::text').extract_first() if tr.css('td.col3 div.miniLeft ::text').extract_first() is not None else ''
                if (price):
                    price_item = MangaCafePrice()
                    price_item['name'] = title.strip()
                    price_item['time'] = time.strip()
                    price_item['price'] = price.strip()
                    price_list.append(price_item)
            item['prices'] = price_list
            yield item
