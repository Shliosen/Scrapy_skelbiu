import scrapy
#import urllib.request

class skelbimas(scrapy.Spider):
    name = 'sk'

    def start_request(self):
        urls = [
           'https://www.skelbiu.lt/skelbimai/paslaugos-darbas/darbo-paieska/it-specialistai/1/',
           'https://www.skelbiu.lt/skelbimai/paslaugos-darbas/darbo-paieska/it-specialistai/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) 



    def parse(self, response):
        page=response.url.split("/")[-2]
        filename= "skelbimai-%s.html" % page
        with open (filename, "wb") as f:
            f.write(response.body)
        self.log("saved file %s" % filename)

