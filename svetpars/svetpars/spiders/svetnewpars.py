import scrapy


class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        svet_items = response.css("div.lsooF")
        for svet in svet_items:
            yield{
                "name" : svet.css("div.lsooF span::text").get(),
                "price": svet.css("span.ui-LD-ZU.KIkOH::text").get(),
                "url": response.urljoin(svet.css("a::attr(href)").get())
            }




