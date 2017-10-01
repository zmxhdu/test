# -*- coding: utf-8 -*-
import scrapy


class GithubsSpider(scrapy.Spider):
    name = 'githubs'

    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return(url_tmpl.format(i) for i in range(1, 5))

    def parse(self, response):
        for github in response.xpath('.//li[contains(@itemprop,"owns")]'):
            yield {
                'name': github.xpath('.//a[contains(@itemprop,"name codeRepository")]/text()[1]').extract_first().strip(),
                'update_time': github.xpath('.//div[@class="f6 text-gray mt-2"]/relative-time/@datetime').extract_first()
            }

