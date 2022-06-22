import scrapy
from PaperSpider.items import PaperItem


class ICLRSpider(scrapy.Spider):
    
    name = "iclr"
    allowed_domains = ["dblp.uni-trier.de", "openreview.net"]

    start_urls = [
        'https://dblp.uni-trier.de/db/conf/iclr/iclr2018.html',
        'https://dblp.uni-trier.de/db/conf/iclr/iclr2019.html',
        'https://dblp.uni-trier.de/db/conf/iclr/iclr2020.html',
        'https://dblp.uni-trier.de/db/conf/iclr/iclr2021.html',
    ]
    start_metas = [
        {'conference': 'ICLR', 'year': 2018, 'level': None},
        {'conference': 'ICLR', 'year': 2019, 'level': None},
        {'conference': 'ICLR', 'year': 2020, 'level': None},
        {'conference': 'ICLR', 'year': 2021, 'level': None},
    ]
    
    def start_requests(self):
        for url, meta in zip(self.start_urls, self.start_metas):
            yield scrapy.Request(url=url, callback=self.parse, meta=meta)
    
    def parse(self, response):
        for head_selector, publist_selector in zip(
            response.xpath("//h2")[1:],
            response.xpath("//ul[@class='publ-list']")[1:]
        ):
            level = head_selector.xpath("text()").extract()[0].split()[0]
            for url_selector, paper_selector in zip(
                publist_selector.xpath("li[@class='entry inproceedings']/nav/ul/li[1]/div/a/@href"),
                publist_selector.xpath("li[@class='entry inproceedings']/cite/span[@class='title']/text()")
            ):
                item = PaperItem()
                item['title'] = paper_selector.extract()
                item['url'] = url_selector.extract().replace("forum","pdf")
                item['conference'] = response.meta['conference']
                item['year'] = response.meta['year']
                item['level'] = level
                yield item
