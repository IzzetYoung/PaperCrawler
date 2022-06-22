import scrapy
from PaperSpider.items import PaperItem


class NeurIPSSpider(scrapy.Spider):
    
    name = "nips"
    allowed_domains = ["dblp.uni-trier.de", "proceedings.neurips.cc"]
    prefix = 'https://proceedings.neurips.cc'

    start_urls = [
        'https://proceedings.neurips.cc/paper/2018',
        'https://proceedings.neurips.cc/paper/2019',
        'https://proceedings.neurips.cc/paper/2020',
        'https://proceedings.neurips.cc/paper/2021',
    ]
    start_metas = [
        {'conference': 'NeurIPS', 'year': 2018, 'level': None},
        {'conference': 'NeurIPS', 'year': 2019, 'level': None},
        {'conference': 'NeurIPS', 'year': 2020, 'level': None},
        {'conference': 'NeurIPS', 'year': 2021, 'level': None},
    ]
    
    def start_requests(self):
        for url, meta in zip(self.start_urls, self.start_metas):
            yield scrapy.Request(url=url, callback=self.parse, meta=meta)
    
    def parse(self, response):
        for paper_selector in response.xpath(
                "//div[@class='container-fluid']/div[@class='col']/ul/li/a/@href"):
            yield scrapy.Request(url=self.prefix+paper_selector.extract(), callback=self.nips_parse, meta=response.meta)
    
    def nips_parse(self, response):
        item = PaperItem()
        item['title'] = response.xpath("//div[@class='container-fluid']/div[@class='col']/h4[1]/text()").extract()[0]
        item['url'] = self.prefix + response.xpath("//a[text()='Paper']/@href").extract()[0]
        item['conference'] = response.meta['conference']
        item['year'] = response.meta['year']
        item['level'] = response.meta['level']
        return item

