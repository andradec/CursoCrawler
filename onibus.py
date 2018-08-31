# -*- coding: utf-8 -*-
import scrapy


class OnibusSpider(scrapy.Spider):
    name = 'onibus'
    allowed_domains = ['http://www.ctaonline.com.br/index.php/linhas.html']
    start_urls = ['http://http://www.ctaonline.com.br/index.php/linhas.html/']

    def parse(self, response):
        pass
