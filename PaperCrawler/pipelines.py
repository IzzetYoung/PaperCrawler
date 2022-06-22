# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class PapercrawlerPipeline:
    def process_item(self, item, spider):
        return item


class PaperDownloadPipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None, *, item=None):
        title = item['title'].replace("/", "-").strip() if "/" in item['title'] else item['title'].strip()
        if item['level'] is not None:
            file_name = item['conference'] + str(item['year']) + item['level'] + '-' + title
            return f"{item['conference']}/{str(item['year'])}/{item['level']}/{file_name}.pdf"
        else:
            file_name = item['conference'] + str(item['year']) + '-' + title
            return f"{item['conference']}/{str(item['year'])}/{file_name}.pdf"

    def get_media_requests(self, item, info):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            }
        yield scrapy.Request(item['url'], headers=headers)

