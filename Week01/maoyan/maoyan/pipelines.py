# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanPipeline:
    # def process_item(self, item, spider):
    #     return item

    def process_item(self, item, spider):
        film_title = item['title']
        film_type = item['type']
        film_date = item['release_date']
        row = film_title + ',' + film_type + ',' + film_date + '\n'
        with open('E:\\maoyanfilm.txt', 'a+', encoding='utf-8') as f:
            f.write(row)