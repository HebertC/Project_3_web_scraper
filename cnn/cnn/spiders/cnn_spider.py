import scrapy
from cnn.items import CnnItem
from scrapy.selector import Selector


class CnnSpider(scrapy.Spider):
    name = "cnn"
    allowed_domains = ["edition.cnn.com"]
    start_urls = [
        "http://edition.cnn.com/"
    ]

    def parse(self, response):
        hxs = Selector(response)
        """
        get the xpath of the heading and parse it.
        trying to get the all text in 
        <span class"cd__headline-text"></span>
        """
        big_headline_spans  = hxs.xpath('//span[@class="cd__headline-text"]/text()').extract()
        
        items = []
        
        for big_headline_span in big_headline_spans:
            item = CnnItem()
            item["big_headlines"] = big_headline_span
            items.append(item)

        return items
