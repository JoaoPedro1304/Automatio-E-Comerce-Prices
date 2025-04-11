from database.db_abstraction import Db_Abstraction
from model.product_model import Base
import os

class Postgres_Connection:

    def __init__(self):        
        #load_dotenv()
        connection_string = os.getenv('CONNECTION_STRING')
        self.db = Db_Abstraction(connection_string)
        

    def get_session(self):
        return self.db.get_session()

    def create_tables(self):
        return Base.metadata.create_all(self.db.get_engine())