#code de jumia 
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



# code de https://www.senboutique.com/


from scrapy import Request, Spider
from comparateur_prix.items import ComparateurPrixItem


class PrixSpider(Spider):
    name = "prix"
    start_urls = ['https://www.senboutique.com/']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        listArticles = response.css('div.feat_in')
        for article in listArticles:
            image = article.css('div.feat_img.prod_img a img::attr(src)').extract_first()
            designation = article.css('div.feat_cont p a::text').extract_first()
            prix = article.css('div.add span::text').extract_first()

            item = ComparateurPrixItem()
            item['image'] = image
            item['designation'] = designation
            item['prix'] = prix
            yield item



#code de https://tech-access-dakar.com/
from scrapy import Request, Spider
from comparateur_prix.items import ComparateurPrixItem


class PrixSpider(Spider):
    name = "prix"
    start_urls = ['https://tech-access-dakar.com/']

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




# code pour https://www.electromenager-dakar.com/
from scrapy import Request, Spider
from comparateur_prix.items import ComparateurPrixItem


class PrixSpider(Spider):
    name = "prix"
    start_urls = ['https://www.electromenager-dakar.com/']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        listArticles = response.css('div.product-small')
        for article in listArticles:
            image_link = article.css('div.box-image img::attr(data-lazy-src)').extract_first()
            designation = article.css('p.name.product-title.woocommerce-loop-product__title a::text').extract_first()
            prix = article.css('span.price ins span.woocommerce-Price-amount.amount bdi::text').extract_first()

            yield Request(url=image_link, callback=self.parse_image, meta={'designation': designation, 'prix': prix})

    def parse_image(self, response):
        item = ComparateurPrixItem()
        item['image'] = response.url
        item['designation'] = response.meta['designation']
        item['prix'] = response.meta['prix']
        yield item


# code pour https://samabestshop.com/
from scrapy import Request, Spider
from comparateur_prix.items import ComparateurPrixItem


class PrixSpider(Spider):
    name = "prix"
    start_urls = ['https://samabestshop.com/']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        listArticles = response.css('div.product-small')
        for article in listArticles:
            image_link = article.css('div.box-image a img::attr(src)').extract_first()
            designation = article.css('div.box-text p.name.product-title.woocommerce-loop-product__title a::text').extract_first()
            prix = article.css('div.box-text span.price span.woocommerce-Price-amount.amount bdi::text').extract_first()

            item = ComparateurPrixItem()
            item['image'] = image_link
            item['designation'] = designation
            item['prix'] = prix
            yield item



# code pour https://discount-senegal.com/
from scrapy import Request, Spider
from comparateur_prix.items import ComparateurPrixItem


class PrixSpider(Spider):
    name = "prix"
    start_urls = ['https://discount-senegal.com/']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        listArticles = response.css('div.product-hover-swap')
        for article in listArticles:
            image_link = article.css('div.product-image-wrapper a.product-content-image img::attr(src)').extract_first()
            designation = article.css('div.text-center.product-details h2.product-title a::text').extract_first()
            prix = article.css('div.text-center.product-details span.price span.woocommerce-Price-amount.amount bdi::text').extract_first()

            item = ComparateurPrixItem()
            item['image'] = image_link
            item['designation'] = designation
            item['prix'] = prix
            yield item


from scrapy import Request, Spider
from comparateur_prix.items import ComparateurPrixItem


class PrixSpider(Spider):
    name = "prix"
    start_urls = ['https://www.senboutique.com/']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        listItems = response.css('form[name^="item_form"]')
        for item in listItems:
            designation = item.css('div.feat_cont p a::text').get()
            image = item.css('div.feat_img.prod_img a img::attr(src)').get()
            prix = item.css('div.feat_cont div.add span::text').get()

            comparateur_item = ComparateurPrixItem()
            comparateur_item['designation'] = designation
            comparateur_item['image'] = image
            comparateur_item['prix'] = prix
            yield comparateur_item
