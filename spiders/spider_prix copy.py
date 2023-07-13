from scrapy import Request, Spider
from comparateur_prix.items import ComparateurPrixItem


class PrixSpider(Spider):
    name = "prix"
    start_urls = ['https://www.jumia.sn/']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        listArticles = response.css('article.prd')
        for article in listArticles:
            designation = article.css('a.core div.name::text').extract_first()
            image = article.css('a.core img::attr(data-src)').extract_first()
            prix = article.css('a.core div.prc::text').extract_first()
            pourcent = article.css('a.core div.tag::text').extract_first()

            item = ComparateurPrixItem()
            item['designation'] = designation
            item['image'] = image
            item['pourcent'] = pourcent
            item['prix'] = prix
            yield item
