import json
from scrapy import Request, Spider

from web_scrapping_app4.items import ProduitItem




class DakarMarketSpider(Spider):
    name = "dakarmarket"
    start_urls = ['https://dakarmarket.sn/categorie/telephone-portable?page=1']
    site_name = 'DakarMarket'
    items = []


    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)


    def parse(self, response):
        listItems = response.css('div.card')
        for item in listItems:
            designation = item.css('a::attr(title)').get()
            designation = designation.encode('ascii', 'ignore').decode('utf-8')
            image = item.css('img::attr(data-src)').get()
            prix = item.css('span.fs-4::text').get()
            prix = prix.replace('\n', '').replace('\u202f', '').replace('\u00a0', '').strip() if prix else None


            comparateur_item = ProduitItem()
            comparateur_item['designation'] = designation
            comparateur_item['image'] = image
            comparateur_item['prix'] = prix
            comparateur_item['site'] = self.site_name


            self.items.append(comparateur_item)


        # Récupérer les données des pages 2 à 27
        for page in range(2, 28):
            next_page_url = f'https://dakarmarket.sn/categorie/telephone-portable?page={page}'
            yield Request(url=next_page_url, callback=self.parse)


    def closed(self, reason):
        # Enregistrement des données dans un fichier JSON à la fermeture de l'araignée
        data = [dict(item) for item in self.items]


        with open('dakarmarket.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
