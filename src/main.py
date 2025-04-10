from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from model.ProductModel import Produto,Base
from database.postgres_connection import Postgres_Connectcion 
import json

db = Postgres_Connectcion()
db.create_tables()
session = db.get_session()

def load_json():
    with open("sites json/sites.json","r") as file:
        return json.load(file)

def start_driver():
    options =Options()
    options.add_argument('--disable-notifications')
    return webdriver.Chrome(options=options)


def save_products_database(url,site_name,product_name, product_price):
    try:
        product = session.query(Produto).filter(Produto.product_name == product_name).first()

        if product:

            raise Exception(f'\n \033[91m Product: {product.product_name} from {product.site_name}, Already exists! \n \033[0m')

        else:
            session.add(Produto(url=url, site_name=site_name, product_name=product_name, price=product_price))
            session.commit()

            print('Sucsses, data saved in database!')

            product = session.query(Produto).all()

            for p in product:
                print(f'ID: {p.id}, Site: {p.site_name}, Produto: {p.product_name}, Preço: R$ {p.price}')

    except Exception as error:

        print(f'Error:{error}')


def get_products(url,site_name, product_selector, price_selector, price_fraction_selector):

    driver = start_driver()
    driver.get(url)
    
    WebDriverWait(driver,15).until(
        EC.presence_of_all_elements_located((By.XPATH, product_selector))
    )
    product_name = driver.find_element(By.XPATH, product_selector).text

    WebDriverWait(driver,15).until(
        EC.presence_of_all_elements_located((By.XPATH,price_selector))
    )
    product_price = driver.find_element(By.XPATH,price_selector).text

    full_price = product_price

    if not price_fraction_selector: #Alguns sites possuem valor decimal do preço separado no html.
        
        pass

    else:
        WebDriverWait(driver,15).until(
        EC.presence_of_all_elements_located((By.XPATH,price_fraction_selector))
        )
        price_fraction = driver.find_element(By.XPATH,price_fraction_selector).text

        full_price = product_price +','+ price_fraction

    driver.quit()
    
    clean_price = full_price.replace('ou','').replace('\x0a','').replace('R$','').replace('.','').replace(',','.')

    float_price = round(float(clean_price),2)
    
    save_products_database(url,site_name, product_name, float_price)


if __name__ == '__main__':

    sites = load_json()

    for site in sites:
        try:
            get_products(site["url"], site["site_name"], site["product_selector"], site["price_selector"], site["price_fraction_selector"])

        except Exception as error:        
            print(f'{error}')

    print('Encerrando a sessão!')
    session.close()
