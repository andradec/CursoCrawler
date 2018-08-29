# -*- coding: utf-8 -*-
import scrapy


class UdacitySpider(scrapy.Spider):

    name = 'udacity' 
    start_urls = ['https://br.udacity.com/courses/all/']

    def parse(self, response):
        divs = response.xpath("/html/body/ir-root/ir-content/ir-course-catalog/section[3]/div/div[2]/ir-course-card-catalog/div/div/div/div[1]/ir-catalog-card/div/div")
        for div in divs:
            link = div.xpath('.//h3/a')
            title = link.xpath('./text()').extract_first()
            href = link.xpath('./@href').extract_first()
            img = div.xpath('.//image[contains(@class, "image-overlay")]/@src').extract_first()
            description = div.xpath('.//')

