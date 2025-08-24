from config.config_loader import carregar_config
import pyodbc

def conectar_sql_server():
    config = carregar_config()
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={config['server']};"
        f"DATABASE={config['database']};"
        f"UID={config['user']};"
        f"PWD={config['password']};"
    )
    return conn
