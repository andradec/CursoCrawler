# -*- coding: utf-8 -*-
import scrapy


class UdemySpider(scrapy.Spider):
    name = 'udemy'
    allowed_domains = ['https://www.udemy.com/']
    start_urls = ['http://https://www.udemy.com//']

    def parse(self, response):
        pass
