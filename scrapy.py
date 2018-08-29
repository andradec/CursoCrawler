import scrapy

class GilenoFilhoSpider(scrapy.Spider):

    name = 'gileno filho'    
    start_urls = ['https://globoesporte.globo.com/futebol/times/palmeiras/']

    def parse(self, response):
        self.log('Hello World')
        self.log(response.body)