# scripts/teste_sql.py
from conecta_sql import conectar_sql_server

conn = conectar_sql_server()
cursor = conn.cursor()
cursor.execute("SELECT TOP 5 * FROM DimCustomer")
for row in cursor.fetchall():
    print(row)
conn.close()
