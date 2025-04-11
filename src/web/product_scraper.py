from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductScraper:
        
    def __init__(self):
        options =Options()    
        options.add_argument('--disable-notifications')
        self.driver = webdriver.Chrome(options=options)

    def get_products( self,url,site_name, product_selector, price_selector, price_fraction_selector):           
        
        self.driver.get(url)

        try:
            WebDriverWait(self.driver,15).until(
                EC.presence_of_all_elements_located((By.XPATH, product_selector))
            )
            product_name = self.driver.find_element(By.XPATH, product_selector).text

            WebDriverWait(self.driver,15).until(
                EC.presence_of_all_elements_located((By.XPATH,price_selector))
            )
            product_price = self.driver.find_element(By.XPATH,price_selector).text

            full_price = product_price

            if not price_fraction_selector: #Alguns sites possuem valor decimal do preço separado no html.
                
                pass

            else:

                WebDriverWait(self.driver,15).until(
                EC.presence_of_all_elements_located((By.XPATH,price_fraction_selector))
                )
                price_fraction = self.driver.find_element(By.XPATH,price_fraction_selector).text

                full_price = product_price +','+ price_fraction

            clean_price = (full_price.replace('ou','')
                           .replace('\x0a','')
                           .replace('R$','')
                           .replace('.','')
                           .replace(',','.')
                           )
                      
            float_price = round(float(clean_price),2)

            self.driver.quit()
            
            return {"url":url, "site_name":site_name, "product_name":product_name, "product_price":float_price}

        except Exception as error:
            print(error) 