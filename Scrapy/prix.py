from scrapy import Request, Spider

from items import ProduitItem


class PrixSpider(Spider):
    name = "prix"
    start_urls = ['https://dakarmarket.sn/categorie/telephone-portable?page=1']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        listItems = response.css('div.card')
        for item in listItems:
            designation = item.css('a::attr(title)').get()

            image = item.css('img::attr(data-src)').get()
            prix = item.css('span.fs-4::text').get()
            prix = prix.replace('\n', '').strip() if prix else None

            comparateur_item = ProduitItem()
            comparateur_item['designation'] = designation

            comparateur_item['image'] = image
            comparateur_item['prix'] = prix
            yield comparateur_item

        # Récupérer les données des pages 2 à 27
        for page in range(2, 29):
            next_page_url = f'https://dakarmarket.sn/categorie/telephone-portable?page={page}'
            yield Request(url=next_page_url, callback=self.parse)
