# data/conexao.py
import os
import sqlalchemy
from dotenv import load_dotenv
load_dotenv()
# Dicionário de configuração
config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'server': os.getenv('DB_SERVER'),
    'database': os.getenv('DB_NAME'),
    'driver': 'ODBC Driver 17 for SQL Server'
}

def conectar():
    """
    Cria e retorna uma engine SQLAlchemy para o banco de dados configurado.
    """
    # Validação das variáveis
    for key, value in config.items():
        if not value:
            raise ValueError(f"Configuração '{key}' não definida.")
    try:
        conn_str = (
            f"mssql+pyodbc://{config['user']}:{config['password']}@{config['server']}/"
            f"{config['database']}?driver={config['driver'].replace(' ', '+')}"
        )
        engine = sqlalchemy.create_engine(conn_str)
        return engine
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return None
