from database.db_abstraction import Db_Abstraction
from dotenv import load_dotenv
import os

class Postgres_Connectcion:

    def __init__(self):
        pass
    
    load_dotenv()
    
    connection_string = os.getenv('CONNECTION_STRING')
    
    Session = Db_Abstraction(connection_string).get_session()
    
    def get_session(self):
        return self.Session    
