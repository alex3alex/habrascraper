from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from hscraper.items import HscraperItem

class HspiderSpider(CrawlSpider):
    name = 'hspider'
    allowed_domains = ['habrahabr.ru']
    start_urls = ['http://habrahabr.ru/post/%d/' % i for i in xrange(1, 200000)]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        i = HscraperItem()
        try:
            i['title'] = hxs.select("//span[@class='post_title']/text()").extract()[0]
            i['text'] = hxs.select("//div[@class='content html_format']").extract()[0]
            i['comments'] = hxs.select("//div[@class='message html_format ']").extract()
            i['url'] = response.url
        except IndexError:
            return None
        return i
