from scrapy import Request, Spider
from comparateur_prix.items import ComparateurPrixItem


class PrixSpider(Spider):
    name = "prix"
    start_urls = ['https://tech-access-dakar.com/categorie-produit/articles-hommes/']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        listArticles = response.css('div.product-block')
        for article in listArticles:
            image = article.css('div.product-image img::attr(src)').extract_first()
            designation = article.css('h3.woocommerce-loop-product__title a::text').extract_first()
            prix = article.css('span.price ins span bdi::text').extract_first()

            item = ComparateurPrixItem()
            item['image'] = image
            item['designation'] = designation
            item['prix'] = prix
            yield item
