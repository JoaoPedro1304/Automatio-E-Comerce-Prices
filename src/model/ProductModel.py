from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True)
    url = Column(String)
    site_name = Column(String)
    product_name = Column(String)    
    price = Column(Float)