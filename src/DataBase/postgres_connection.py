from database.db_abstraction import Db_Abstraction
from model.ProductModel import Base
from dotenv import load_dotenv
import os

class Postgres_Connectcion:

    def __init__(self):

        load_dotenv()
        connection_string = os.getenv('CONNECTION_STRING')
        self.db = Db_Abstraction(connection_string)
        

    def get_session(self):
        return self.db.get_session()

    def create_tables(self):
        return Base.metadata.create_all(self.db.get_engine())