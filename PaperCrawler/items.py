# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PaperItem(scrapy.Item):
    title = scrapy.Field()
    conference = scrapy.Field()
    year = scrapy.Field()
    level = scrapy.Field()
    url = scrapy.Field()

