from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Aplicando o Princípio da Inversão de Dependência (DIP), estou separando a lógica de negócio da implementação concreta da conexão com o banco de dados.
# Em vez de depender diretamente de uma tecnologia específica, a lógica de negócio depende de uma abstração,
# permitindo que diferentes implementações (como PostgreSQL, MySQL, etc.)sejam injetadas conforme necessário.

 
def create_engine_db(connectionString: str):
    return create_engine(connectionString)

def create_session_factory(engine):
    return sessionmaker(bind=engine)