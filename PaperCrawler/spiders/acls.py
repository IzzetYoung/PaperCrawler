import scrapy
from PaperSpider.items import PaperItem


class ACLSpider(scrapy.Spider):
    
    name = "acls"
    allowed_domains = ["dblp.uni-trier.de", "aclanthology.org"]
    prefix = 'https://aclanthology.org/'

    start_urls = [
        # 'https://aclanthology.org/volumes/P18-1/',
        # 'https://aclanthology.org/volumes/P18-2/',
        # 'https://aclanthology.org/volumes/P19-1/',
        # 'https://aclanthology.org/volumes/2020.acl-main/',
        # 'https://aclanthology.org/volumes/2021.acl-long/',
        # 'https://aclanthology.org/volumes/2021.acl-short/',
        # 'https://aclanthology.org/volumes/2021.findings-acl/',
        # 'https://aclanthology.org/volumes/2022.acl-long/',
        # 'https://aclanthology.org/volumes/2022.acl-short/',
        # 'https://aclanthology.org/volumes/2022.findings-acl/',
        # 'https://aclanthology.org/volumes/D18-1/',
        # 'https://aclanthology.org/volumes/D19-1/',
        # 'https://aclanthology.org/volumes/2020.emnlp-main/',
        # 'https://aclanthology.org/volumes/2020.findings-emnlp/',
        # 'https://aclanthology.org/volumes/2021.emnlp-main/',
        # 'https://aclanthology.org/volumes/2021.findings-emnlp/',
        # 'https://aclanthology.org/volumes/N18-1/',
        # 'https://aclanthology.org/volumes/N18-2/',
        # 'https://aclanthology.org/volumes/N19-1/',
        # 'https://aclanthology.org/volumes/2021.naacl-main/',
        # 'https://aclanthology.org/volumes/C18-1/',
        # 'https://aclanthology.org/volumes/2020.coling-main/',
    ]
    start_metas = [
        # {'conference': 'ACL', 'year': 2018, 'level': 'Long'},
        # {'conference': 'ACL', 'year': 2018, 'level': 'Short'},
        # {'conference': 'ACL', 'year': 2019, 'level': None},
        # {'conference': 'ACL', 'year': 2020, 'level': None},
        # {'conference': 'ACL', 'year': 2021, 'level': 'Long'},
        # {'conference': 'ACL', 'year': 2021, 'level': 'Short'},
        # {'conference': 'ACL', 'year': 2021, 'level': 'Finding'},
        # {'conference': 'ACL', 'year': 2022, 'level': 'Long'},
        # {'conference': 'ACL', 'year': 2022, 'level': 'Short'},
        # {'conference': 'ACL', 'year': 2022, 'level': 'Finding'},
        # {'conference': 'EMNLP', 'year': 2018, 'level': None},
        # {'conference': 'EMNLP', 'year': 2019, 'level': None},
        # {'conference': 'EMNLP', 'year': 2020, 'level': 'Main'},
        # {'conference': 'EMNLP', 'year': 2020, 'level': 'Finding'},
        # {'conference': 'EMNLP', 'year': 2021, 'level': 'Main'},
        # {'conference': 'EMNLP', 'year': 2021, 'level': 'Finding'},
        # {'conference': 'NAACL', 'year': 2018, 'level': 'Long'},
        # {'conference': 'NAACL', 'year': 2018, 'level': 'Short'},
        # {'conference': 'NAACL', 'year': 2019, 'level': None},
        # {'conference': 'NAACL', 'year': 2021, 'level': None},
        # {'conference': 'COLING', 'year': 2018, 'level': None},
        # {'conference': 'COLING', 'year': 2020, 'level': None},
    ]
    
    def start_requests(self):
        for url, meta in zip(self.start_urls, self.start_metas):
            yield scrapy.Request(url=url, callback=self.parse, meta=meta)
    
    def parse(self, response):
        for paper_selector in response.xpath(
                "//p[@class='d-sm-flex align-items-stretch']/span[@class='d-block']/strong/a[@class='align-middle']/@href"
            )[1:]:
            yield scrapy.Request(url=self.prefix+paper_selector.extract(), callback=self.acl_parse, meta=response.meta)

    def acl_parse(self, response):
        item = PaperItem()
        item['title'] = ' '.join(response.xpath("/html/body/div/section/div[1]/h2/a/text()").extract())
        item['url'] = response.xpath("/html/body/div/section/div[1]/h2/a/@href").extract()[0]
        item['conference'] = response.meta['conference']
        item['year'] = response.meta['year']
        item['level'] = response.meta['level']
        return item
