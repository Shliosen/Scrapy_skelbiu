import scrapy
import urllib.request

class skelbimas(scrapy.Spider):
    name = 'sk'

    start_urls = [
           'http://skelbiu.lt/skelbimai/paslaugos-darbas/darbo-paieska/it-specialistai/1',
           'http://skelbiu.lt/skelbimai/paslaugos-darbas/darbo-paieska/it-specialistai/2',
        ]
 
    

            

