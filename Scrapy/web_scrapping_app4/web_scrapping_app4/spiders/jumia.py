
import json
import unicodedata
from pymongo import MongoClient
from scrapy import Request, Spider

from web_scrapping_app4.items import ProduitItem


class JumiaSpider(Spider):
    name = "jumia"
    start_urls = ['https://www.jumia.sn/telephone-tablette/?page=1#catalog-listing']
    site_name = 'Jumia'
    items = []

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)


    def parse(self, response):
        listArticles = response.css('article.prd')
        for article in listArticles:
            designation = article.css('a.core div.name::text').extract_first()
            if designation:
                designation = unicodedata.normalize('NFKD', designation).encode('ASCII', 'ignore').decode('utf-8')
                designation = designation.replace('\u2013', '-').replace('\u2033', '').replace('\"',"")
            image = article.css('a.core img::attr(data-src)').extract_first()
            prix = article.css('a.core div.prc::text').extract_first()
            prix = prix.replace(' ', '').strip() if prix else None


            item = ProduitItem()
            item['designation'] = designation
            item['image'] = image
            item['prix'] = prix
            item['site'] = self.site_name


            self.items.append(item)


        # Récupérer les données des pages 2 à 25
        for page in range(2, 25):
            next_page_url = f'https://www.jumia.sn/telephone-tablette/?page={page}#catalog-listing'
            yield Request(url=next_page_url, callback=self.parse)


    def closed(self, reason):
        # Enregistrement des données dans un fichier JSON à la fermeture de l'araignée
        data = [dict(item) for item in self.items if item['designation'] is not None]

        #with open('jumia.json', 'w') as json_file:
        #   json.dump(data, json_file, indent=4)

        # Connexion à MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['resultat_db']
        collection = db['SiteScrappingApp_resultat']

        # Insérer les données dans la collection MongoDB
        collection.insert_many(data)

        # Fermer la connexion à MongoDB
        client.close()
