from database.postgres_connection import Postgres_Connectcion
from sqlalchemy import text

# Reseta a sequencia serial da tabela id
# Este código foi utilizado somente durante os teste com o banco

db = Postgres_Connectcion()
session = db.get_session()

def reset_id_sequence(session, table_name, column_name='id', restart_value=1):
    seq_sql = f"SELECT pg_get_serial_sequence('{table_name}', '{column_name}')"
    seq_name = session.execute(text(seq_sql)).scalar()

    if seq_name:
        reset_sql = f"ALTER SEQUENCE {seq_name} RESTART WITH {restart_value}"
        session.execute(text(reset_sql))
        session.commit()
        print(f"Sequência '{seq_name}' resetada para começar em {restart_value}.")
    else:
        print("Sequência não encontrada.")

reset_id_sequence(session, 'produtos')

session.close()