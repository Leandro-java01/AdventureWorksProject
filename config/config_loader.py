from dotenv import load_dotenv
import os

def carregar_config():
    load_dotenv(dotenv_path='../config/db_config.env')
    config = {
        'server': os.getenv('DB_SERVER'),
        'database': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'driver': os.getenv('DB_DRIVER')
    }
    return config
