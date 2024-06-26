from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ArticleSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items', follow=True)]

    def parse_items(self, response):
        url = response.url
        title = response.css('h1 > span::text').extract_first()
        text_elements = response.xpath('//div[@id="mw-content-text"]//*[not(self::script or self::style or self::noscript)]/text()').extract()
        text = ' '.join([t.strip() for t in text_elements if t.strip()])
        lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
        lastUpdated = lastUpdated.replace(
            'This page was last edited on ', ''
        )
        print('URL is: {}'.format(url))
        input('url')
        print('title is: {}'.format(title))
        input('titulo')
        print('text is: {}'.format(text))
        input('texto')
        print('Last updated: {}'.format(lastUpdated))
        input('data')