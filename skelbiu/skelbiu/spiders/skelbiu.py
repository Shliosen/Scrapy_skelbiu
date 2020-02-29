import scrapy
#import urllib.request

class skelbimas(scrapy.Spider):
    name = 'sk'

    start_urls = [
           'http://skelbiu.lt/skelbimai/paslaugos-darbas/darbo-paieska/it-specialistai/1',
           'http://skelbiu.lt/skelbimai/paslaugos-darbas/darbo-paieska/it-specialistai/2',
        ]
 
    def parse(self, response):
        for data in response.css('div.quote'):
            yield{
                
            }

            

