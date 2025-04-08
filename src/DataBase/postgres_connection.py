from database.db_connection import create_engine_db, create_session
from dotenv import load_dotenv
import os

load_dotenv()

connectionString = os.getenv('CONNECTION_STRING')

engine = create_engine_db(connectionString)

Session = create_session(engine)

def get_session():
    return Session()