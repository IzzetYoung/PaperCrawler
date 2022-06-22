import scrapy
from PaperSpider.items import PaperItem


class ICMLSpider(scrapy.Spider):
    
    name = "icml"
    allowed_domains = ["dblp.uni-trier.de", "proceedings.mlr.press/"]

    start_urls = [
        'http://proceedings.mlr.press/v80/',
        'http://proceedings.mlr.press/v97/',
        'http://proceedings.mlr.press/v119/',
        'http://proceedings.mlr.press/v139/',
    ]
    start_metas = [
        {'conference': 'ICML', 'year': 2018, 'level': None},
        {'conference': 'ICML', 'year': 2019, 'level': None},
        {'conference': 'ICML', 'year': 2020, 'level': None},
        {'conference': 'ICML', 'year': 2021, 'level': None},
    ]
    
    def start_requests(self):
        for url, meta in zip(self.start_urls, self.start_metas):
            yield scrapy.Request(url=url, callback=self.parse, meta=meta)
    
    def parse(self, response):
        for paper_selector in response.xpath(
                "//div[@class='paper']"):
            item = PaperItem()
            item['title'] = paper_selector.xpath("p[@class='title']/text()").extract()[0]
            item['url'] = paper_selector.xpath("p[@class='links']/a[2]/@href").extract()[0]
            item['conference'] = response.meta['conference']
            item['year'] = response.meta['year']
            item['level'] = response.meta['level']
            yield item

