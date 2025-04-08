from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from model.ProductModel import Base, Produto
from database.postgres_connection import get_session, engine
import json


def load_json():
    with open("sites json/sites.json","r") as file:
        return json.load(file)

def start_driver():
    options =Options()
    options.add_argument('--disable-notifications')
    return webdriver.Chrome(options=options)

def save_products_database(url,site_name,product_name, product_price):
    
    # session = get_session()
    # Base.metadata.create_all(engine)
    # try:
    #     session.add(Produto(url=url, site_name=site_name, product_name=product_name, price=product_price))
    # except Exception as error:
    #     print(f'Error:{error}')

    #Testando
    print(url,site_name,product_name, product_price)

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

    #print(f'{site_name}, {product_name}, {float_price}')
    
    save_products_database(url,site_name, product_name, float_price)


site = load_json()

for s in site:
    try:
        get_products(s["url"], s["site_name"], s["product_selector"], s["price_selector"], s["price_fraction_selector"])
    except Exception as error:
        print(f'{error}')