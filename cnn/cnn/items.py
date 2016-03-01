# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnnItem(scrapy.Item):
    # define the fields for your item here like:
    big_headlines = scrapy.Field()
    featured_sections_headline = scrapy.Field()
    allinone = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
