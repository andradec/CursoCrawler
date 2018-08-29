import scrapy

class GilenoFilhoSpider(scrapy.Spider):

    name = 'gileno filho'    
    start_urls = ['http://www.gilenofilho.com.br']

    def parse(self, response):
        self.log('Hello World')
        self.log(response.body)