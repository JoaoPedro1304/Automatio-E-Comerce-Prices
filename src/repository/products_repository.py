from model.product_model import Produto
from database.postgres_connection import Postgres_Connection

class Product_Repository:

    def __init__(self):
        db = Postgres_Connection()
        db.create_tables()
        self.session = db.get_session()

    def save_products_database(self,url,site_name,product_name, product_price):

        try:
            product = self.session.query(Produto).filter(Produto.product_name == product_name).first()

            if product:

                raise Exception(f'\n \033[91m Product: {product.product_name} from {product.site_name}, Already exists! \n \033[0m')

            else:
                self.session.add(Produto(url=url, site_name=site_name, product_name=product_name, price=product_price))
                self.session.commit()

                print('Sucsses, data saved in database!')

                product = self.session.query(Produto).all()

                for p in product:
                    print(f'ID: {p.id}, Site: {p.site_name}, Produto: {p.product_name}, Preço: R$ {p.price}')

            self.session.close()

        except Exception as error:

            print(f'Error:{error}')
