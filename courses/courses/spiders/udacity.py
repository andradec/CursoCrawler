# -*- coding: utf-8 -*-
import scrapy


class UdacitySpider(scrapy.Spider):

    name = 'udacity' 
    start_urls = ['https://br.udacity.com/courses/all/']

    def parse(self, response):
        divs = response.xpath("/html/body/ir-root/ir-content/ir-course-catalog/section[3]/div/div[2]/ir-course-card-catalog/div/div/div/div[1]/ir-catalog-card/div/div")

        for div in divs:
            link = div.xpath('.//h3/a')          
            href = link.xpath('./@href').extract_first()           
            yield scrapy.Request(
                url = 'https://br.udacity.com%s' %href,
                callback = self.parse_detail
            )
    def parse_detail(self, response):
        title = response.xpath('//title/text()').extract_first()
        headline = response.xpath('//h6[contains(@class, "big hidden-sm-down ng-star-inserted")]/text()').extract_first()
        img = response.xpath('/html/body/ir-root/ir-content/ir-ndop-b/section[6]/ir-nd-features-b/div/div[1]/div/img/@src').extract_first()

        instructors = []
        for div in response.xpath('//div[contains(@class, "card ng-star-inserted")]'):
            instructors.append(
                {
                    'name':div.xpath('.//h5/text()').extract_first(),
                    'image':div.xpath('.//img/@src').extract_first()
                }
            )
        yield{
            'title':title,
            'healine':headline,
            'image': img,
            'instructors': instructors,
        }
            

