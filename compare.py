import json

from difflib import SequenceMatcher
from itertools import combinations

# Chargement des fichiers JSON contenant les données des produits
file1 = 'data1.json'
file2 = 'data2.json'
file3 = 'data3.json'
file4 = 'data4.json'

# Fonction pour comparer les noms de produits en utilisant la similarité de séquence
def compare_product_names(name1, name2):
    return SequenceMatcher(None, name1, name2).ratio()

# Fonction pour comparer les produits des fichiers JSON
def compare_products(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

        # Liste pour stocker les résultats de comparaison
        compared_results = []

        # Parcours des produits dans le premier fichier
        for product1 in data1:
            product_name1 = product1['name']
            similar_products = []

            # Parcours des produits dans le deuxième fichier
            for product2 in data2:
                product_name2 = product2['name']

                # Comparaison des noms de produits
                similarity = compare_product_names(product_name1, product_name2)

                # Ajout du produit similaire à la liste si la similarité est supérieure à un certain seuil
                if similarity > 0.7:
                    similar_products.append(product2)

            # Ajout du produit et de ses produits similaires à la liste des résultats
            compared_results.append({
                'product': {
                    'name': product1['name'],
                    'site': 'site1',
                    'price': product1['price']
                },
                'similar_products': [{
                    'name': product2['name'],
                    'site': 'site2',
                    'price': product2['price']
                } for product2 in similar_products]
            })

        return compared_results

# Comparaison des produits entre les différents fichiers JSON
compared_results_1_2 = compare_products(file1, file2)
compared_results_1_3 = compare_products(file1, file3)
compared_results_1_4 = compare_products(file1, file4)

# Fusion des résultats de comparaison
all_compared_results = compared_results_1_2 + compared_results_1_3 + compared_results_1_4

# Écriture des résultats dans un fichier JSON
output_file = 'compared_results.json'
with open(output_file, 'w') as f:
    json.dump(all_compared_results, f, indent=4)



