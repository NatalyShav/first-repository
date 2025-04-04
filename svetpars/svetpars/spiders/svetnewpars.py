import scrapy


class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["https://www.divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        svet = response.css("div.lsooF")
        for svet in svet:
            yield{
                "name" : svet.css("div.lsooF span::text").get(),
                "price" : svet.css("div.ui-LD-ZU KIkOH span::text").get(),
                "url" : svet.css("a").attrib["href"]
            }




