from web.product_scraper import ProductScraper
from repository.products_repository import Product_Repository
import json
import tempfile

temp_file = tempfile.mkdtemp()

def load_json():
    with open("sites json/sites.json","r") as file:
        return json.load(file)
    

if __name__ == '__main__':

    sites = load_json()

    

    for site in sites:
        try:
            product_scraper = ProductScraper()

            products = product_scraper.get_products(site["url"], site["site_name"], site["product_selector"], site["price_selector"], site["price_fraction_selector"])

            for p in products:
                products_repository = Product_Repository()
                products_repository.save_products_database(p["url"],p["site_name"], p["product_name"], p["product_price"])
            

        except Exception as error:        
            print(f'{error}')

    print('Encerrando a sessão!')
   
