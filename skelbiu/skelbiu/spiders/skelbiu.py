import scrapy
import urllib.request

class skelbimas(scrapy.Spider):
    name = 'sk'

    start_urls = [
           'http://skelbiu.lt/skelbimai/paslaugos-darbas/darbo-paieska/it-specialistai/1',
           'http://skelbiu.lt/skelbimai/paslaugos-darbas/darbo-paieska/it-specialistai/2',
        ]
 
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

            

