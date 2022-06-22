import scrapy
from PaperSpider.items import PaperItem


class ACLSpider(scrapy.Spider):
    
    name = "tacls"
    allowed_domains = ["dblp.uni-trier.de", "aclanthology.org"]
    prefix = 'https://aclanthology.org/'

    start_urls = [
        # 'https://aclanthology.org/volumes/Q18-1/',
        # 'https://aclanthology.org/volumes/Q19-1/',
        # 'https://aclanthology.org/events/tacl-2020/',
        # 'https://aclanthology.org/events/tacl-2021/',
        # 'https://aclanthology.org/events/tacl-2022/',
        # 'https://aclanthology.org/volumes/J18-1/',
        # 'https://aclanthology.org/volumes/J18-2/',
        # 'https://aclanthology.org/volumes/J18-3/',
        # 'https://aclanthology.org/volumes/J18-4/',
        # 'https://aclanthology.org/volumes/J19-1/',
        # 'https://aclanthology.org/volumes/J19-2/',
        # 'https://aclanthology.org/volumes/J19-3/',
        # 'https://aclanthology.org/volumes/J19-4/',
        # 'https://aclanthology.org/volumes/2020.cl-1/',
        # 'https://aclanthology.org/volumes/2020.cl-2/',
        # 'https://aclanthology.org/volumes/2020.cl-3/',
        # 'https://aclanthology.org/volumes/2020.cl-4/',
        # 'https://aclanthology.org/volumes/2021.cl-1/',
        # 'https://aclanthology.org/volumes/2021.cl-2/',
        # 'https://aclanthology.org/volumes/2021.cl-3/',
        # 'https://aclanthology.org/volumes/2021.cl-4/',
        # 'https://aclanthology.org/volumes/2022.cl-1/',
    ]
    start_metas = [
        # {'conference': 'TACL', 'year': 2018, 'level': None},
        # {'conference': 'TACL', 'year': 2019, 'level': None},
        # {'conference': 'TACL', 'year': 2020, 'level': None},
        # {'conference': 'TACL', 'year': 2021, 'level': None},
        # {'conference': 'TACL', 'year': 2022, 'level': None},
        # {'conference': 'CL', 'year': 2018, 'level': None},
        # {'conference': 'CL', 'year': 2018, 'level': None},
        # {'conference': 'CL', 'year': 2018, 'level': None},
        # {'conference': 'CL', 'year': 2018, 'level': None},
        # {'conference': 'CL', 'year': 2019, 'level': None},
        # {'conference': 'CL', 'year': 2019, 'level': None},
        # {'conference': 'CL', 'year': 2019, 'level': None},
        # {'conference': 'CL', 'year': 2019, 'level': None},
        # {'conference': 'CL', 'year': 2020, 'level': None},
        # {'conference': 'CL', 'year': 2020, 'level': None},
        # {'conference': 'CL', 'year': 2020, 'level': None},
        # {'conference': 'CL', 'year': 2020, 'level': None},
        # {'conference': 'CL', 'year': 2021, 'level': None},
        # {'conference': 'CL', 'year': 2021, 'level': None},
        # {'conference': 'CL', 'year': 2021, 'level': None},
        # {'conference': 'CL', 'year': 2021, 'level': None},
        # {'conference': 'CL', 'year': 2022, 'level': None},
    ]
    
    def start_requests(self):
        for url, meta in zip(self.start_urls, self.start_metas):
            yield scrapy.Request(url=url, callback=self.parse, meta=meta)
    
    def parse(self, response):
        for paper_selector in response.xpath(
                "//p[@class='d-sm-flex align-items-stretch']/span[@class='d-block']/strong/a[@class='align-middle']/@href"
            ):
            yield scrapy.Request(url=self.prefix+paper_selector.extract(), callback=self.acl_parse, meta=response.meta)

    def acl_parse(self, response):
        item = PaperItem()
        item['title'] = ' '.join(response.xpath("/html/body/div/section/div[1]/h2/a/text()").extract())
        item['url'] = response.xpath("/html/body/div/section/div[1]/h2/a/@href").extract()[0]
        item['conference'] = response.meta['conference']
        item['year'] = response.meta['year']
        item['level'] = response.meta['level']
        return item
