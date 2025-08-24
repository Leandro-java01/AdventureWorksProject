# scripts/visualizacoes.py

import matplotlib.pyplot as plt

def grafico_vendas_por_territorio(df):
    """
    Gera um gráfico de barras horizontais com vendas por território.
    """
    plt.figure(figsize=(10, 6))
    plt.barh(df['SalesTerritoryKey'].astype(str), df['TotalVendas'], color='skyblue')
    plt.xlabel('Total de Vendas')
    plt.ylabel('Território')
    plt.title('Vendas por Território')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

def grafico_produtos_mais_vendidos(df):
    """
    Gera um gráfico de barras verticais com os produtos mais vendidos.
    """
    plt.figure(figsize=(12, 6))
    plt.bar(df['EnglishProductName'], df['TotalVendas'], color='orange')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Produto')
    plt.ylabel('Total de Vendas')
    plt.title('Top Produtos Mais Vendidos')
    plt.tight_layout()
    plt.show()

def grafico_vendas_por_ano(df):
    """
    Gera um gráfico de linha com evolução das vendas por ano.
    """
    plt.figure(figsize=(8, 5))
    plt.plot(df['Ano'], df['TotalVendas'], marker='o', linestyle='-', color='green')
    plt.xlabel('Ano')
    plt.ylabel('Total de Vendas')
    plt.title('Evolução das Vendas por Ano')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def grafico_vendas_por_cliente(df):
    """
    Gera um gráfico de pizza com os clientes que mais compraram.
    """
    plt.figure(figsize=(8, 8))
    plt.pie(df['TotalVendas'], labels=df['Cliente'], autopct='%1.1f%%', startangle=140)
    plt.title('Distribuição de Vendas por Cliente')
    plt.tight_layout()
    plt.show()
