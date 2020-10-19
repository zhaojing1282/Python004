import scrapy
from scrapy.selector import Selector
from maoyan.items import MaoyanItem


class Maoyan1Spider(scrapy.Spider):
    name = 'maoyan1'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = "https://maoyan.com/films?showType=3"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = MaoyanItem()
        films = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for film in films:
            item_title = film.xpath('./div[@class="movie-hover-title"][1]/span/text()').extract_first().strip()
            item_type = film.xpath('./div[@class="movie-hover-title"][2]/text()')[1].extract().strip()
            item_date = film.xpath('./div[@class="movie-hover-title movie-hover-brief"]/text()')[1].extract().strip()

            item['title'] = item_title
            item['type'] = item_type
            item['release_date'] = item_date

            yield item

