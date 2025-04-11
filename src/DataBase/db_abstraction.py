from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Aplicando o Princípio da Inversão de Dependência (DIP), estou separando a lógica de negócio da implementação concreta da conexão com o banco de dados.
# Em vez de depender diretamente de uma tecnologia específica, a lógica de negócio depende de uma abstração,
# permitindo que diferentes implementações (como PostgreSQL, MySQL, etc.)sejam injetadas conforme necessário.

class Db_Abstraction:

    def __init__(self, connection_string : str):

        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)
        

    def get_session(self):
        return self.Session()
    
    def get_engine(self):
        return self.engine

