# -*- coding: utf-8 -*-
import scrapy


class CourseraSpider(scrapy.Spider):

    name = 'coursera'
    start_urls = ['https://www.coursera.org/browse?language=pt']

    def parse(self, response):
        self.log('Hello World! Scrapy Project')
