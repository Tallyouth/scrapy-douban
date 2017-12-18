# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SatomiPicItem(scrapy.Item):
    a_image_url = scrapy.Field()
    images = scrapy.Field()
