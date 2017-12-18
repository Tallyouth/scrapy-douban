from scrapy.spiders import Spider
from scrapy.selector import Selector
from satomi_pic.items import SatomiPicItem
from scrapy import Request
from scrapy.spiders import CrawlSpider
class stom_spider(Spider):
    name = 'spider'
    download_delay = 1
    start_urls = [
        'https://movie.douban.com/celebrity/1016930/photos/?type=C&start=0&sortby=like&size=a&subtype=a'
    ]
    def parse(self,response):
        sel = Selector(response)
        item = SatomiPicItem()
        image_url = sel.xpath('//div[@class="cover"]/a/img/@src').extract()
        print 'the urls:/n'
        print image_url
        print '/n'

        item = SatomiPicItem()
        item['a_image_url'] = image_url
        yield item
        next_url = response.xpath('//span[@class="next"]/a/@href').extract()[0]
        yield Request(next_url)






