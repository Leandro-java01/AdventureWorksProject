# scripts/consultas.py

import pandas as pd

def executar_consulta(query: str, conn) -> pd.DataFrame:
    """
    Executa uma consulta SQL e retorna um DataFrame.
    """
    return pd.read_sql(query, conn)

def vendas_por_territorio(conn) -> pd.DataFrame:
    """
    Retorna o total de vendas agrupado por território.
    """
    query = """
        SELECT SalesTerritoryKey, SUM(SalesAmount) AS TotalVendas
        FROM FactInternetSales
        GROUP BY SalesTerritoryKey
        ORDER BY TotalVendas DESC
    """
    return executar_consulta(query, conn)

def produtos_mais_vendidos(conn, limite: int = 10) -> pd.DataFrame:
    """
    Retorna os produtos mais vendidos com base no valor total de vendas.
    """
    query = f"""
        SELECT TOP {limite} p.EnglishProductName, SUM(fis.SalesAmount) AS TotalVendas
        FROM FactInternetSales fis
        JOIN DimProduct p ON fis.ProductKey = p.ProductKey
        GROUP BY p.EnglishProductName, p.ProductKey
        ORDER BY TotalVendas DESC
    """
    return executar_consulta(query, conn)

def vendas_por_ano(conn) -> pd.DataFrame:
    """
    Retorna o total de vendas agrupado por ano.
    """
    query = """
        SELECT YEAR(OrderDate) AS Ano, SUM(SalesAmount) AS TotalVendas
        FROM FactInternetSales
        GROUP BY YEAR(OrderDate)
        ORDER BY Ano
    """
    return executar_consulta(query, conn)

def vendas_por_cliente(conn, limite: int = 10) -> pd.DataFrame:
    """
    Retorna os clientes com maior volume de vendas.
    """
    query = f"""
        SELECT TOP {limite} c.FirstName + ' ' + c.LastName AS Cliente, SUM(f.SalesAmount) AS TotalVendas
        FROM FactInternetSales f
        JOIN DimCustomer c ON f.CustomerKey = c.CustomerKey
        GROUP BY c.FirstName, c.LastName
        ORDER BY TotalVendas DESC
    """
    return executar_consulta(query, conn)
