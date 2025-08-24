# dashboards/app.py

import streamlit as st
import pandas as pd
from data.conexao import conectar


# Configuração da página
st.set_page_config(page_title="AdventureWorks Dashboard", layout="wide")
st.title("📊 Dashboard AdventureWorks")
st.markdown("Olá, Leandro! O sistema está funcionando 🎉")

# Conexão com o banco
engine = conectar()

# Sidebar com filtros
st.sidebar.header("🔎 Filtros")
ano = st.sidebar.selectbox("Ano", [2019, 2020, 2021, 2022])
categoria = st.sidebar.selectbox("Categoria", ["Bikes", "Accessories", "Clothing"])
regiao = st.sidebar.selectbox("Região", ["Northwest", "Southwest", "Central", "Northeast", "Southeast"])

# KPIs
query_kpi = f"""
SELECT 
    COUNT(DISTINCT h.SalesOrderID) AS Pedidos,
    SUM(s.LineTotal) AS TotalVendas,
    AVG(s.LineTotal) AS TicketMedio
FROM Sales.SalesOrderDetail s
JOIN Sales.SalesOrderHeader h ON s.SalesOrderID = h.SalesOrderID
JOIN Sales.SalesTerritory t ON h.TerritoryID = t.TerritoryID
WHERE YEAR(h.OrderDate) = {ano} AND t.Name = '{regiao}'
"""

df_kpi = pd.read_sql(query_kpi, engine)
pedidos = int(df_kpi["Pedidos"][0])
total = round(df_kpi["TotalVendas"][0], 2)
ticket = round(df_kpi["TicketMedio"][0], 2)

col1, col2, col3 = st.columns(3)
col1.metric("📦 Pedidos", f"{pedidos}")
col2.metric("💰 Total de Vendas", f"R$ {total:,.2f}")
col3.metric("🧾 Ticket Médio", f"R$ {ticket:,.2f}")

# Gráfico de produtos mais vendidos
query_produtos = f"""
SELECT p.Name AS Produto, SUM(s.LineTotal) AS TotalVendas
FROM Sales.SalesOrderDetail s
JOIN Production.Product p ON s.ProductID = p.ProductID
JOIN Sales.SalesOrderHeader h ON s.SalesOrderID = h.SalesOrderID
JOIN Sales.SalesTerritory t ON h.TerritoryID = t.TerritoryID
WHERE YEAR(h.OrderDate) = {ano} AND t.Name = '{regiao}' AND p.ProductLine = '{categoria[0]}'
GROUP BY p.Name
ORDER BY TotalVendas DESC
"""

df_produtos = pd.read_sql(query_produtos, engine)

st.subheader(f"🏆 Top Produtos Vendidos ({categoria}) - {ano}")
st.bar_chart(df_produtos.set_index("Produto"))

# Gráfico de vendas mensais
query_mensal = f"""
SELECT MONTH(h.OrderDate) AS Mes, SUM(s.LineTotal) AS Total
FROM Sales.SalesOrderDetail s
JOIN Sales.SalesOrderHeader h ON s.SalesOrderID = h.SalesOrderID
JOIN Sales.SalesTerritory t ON h.TerritoryID = t.TerritoryID
WHERE YEAR(h.OrderDate) = {ano} AND t.Name = '{regiao}'
GROUP BY MONTH(h.OrderDate)
ORDER BY Mes
"""

df_mensal = pd.read_sql(query_mensal, engine)
df_mensal["Mes"] = df_mensal["Mes"].apply(lambda x: f"{x:02d}")

st.subheader("📈 Vendas Mensais")
st.line_chart(df_mensal.set_index("Mes"))

# Rodapé
st.markdown("---")
st.caption("Desenvolvido por Leandro • AdventureWorks • Streamlit • SQL Server")
