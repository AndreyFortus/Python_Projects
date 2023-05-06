import scrapy


class BmwSpider(scrapy.Spider):
    name = 'shop_bmw'
    start_urls = ['https://shop.bmw.ua']

    def parse(self, response):
        for link in response.css('div.line-goods a::attr(href)'):
            yield response.follow(link, callback=self.parse_bmw)

    def parse_bmw(self, response):
        yield {
            'name': response.css('div#product.col-md-12.clear.gody-main-block h1::text').get(),
            'code': response.css('span.say-num::text').get() + response.css('span.num::text').get()
        }
