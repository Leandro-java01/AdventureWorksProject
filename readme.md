# 📊 AdventureWorksProject

Projeto de análise de dados com base no banco AdventureWorksDW2022, utilizando Python, Jupyter Notebooks, e visualizações interativas com Streamlit.

---

## 🗂️ Estrutura do Projeto
AdventureWorksProject/
├── data/                     # Arquivos brutos, backups, CSVs, etc.
│   └── AdventureWorksDW2022.bak
├── notebooks/                # Jupyter Notebooks para exploração
│   └── exploracao.ipynb
├── scripts/                  # Scripts Python (.py) reutilizáveis
│   ├── conecta_sql.py
│   ├── consultas.py
│   └── visualizacoes.py
├── dashboards/               # Dashboards com Streamlit ou Plotly
│   └── app.py
├── outputs/                  # Resultados gerados (gráficos, relatórios)
│   └── vendas_por_territorio.png
├── config/                   # Arquivos de configuração (.env, credenciais)
│   └── db_config.env
├── README.md                 # Documentação do projeto
└── requirements.txt          # Lista de dependências do projeto

notebooks/: ótimo pra testes rápidos e análises exploratórias.
scripts/: separa lógica de conexão, consultas SQL e visualizações.
dashboards/: onde você pode montar apps interativos com Streamlit.
outputs/: salva gráficos, relatórios ou dados exportados.
config/: ideal pra guardar variáveis de ambiente e credenciais (quando for pra produção).


---

## 🧩 Pré-requisitos

- Python 3.9+
- SQL Server (local ou remoto)
- ODBC Driver 17 for SQL Server
- DBeaver (opcional, para visualização do banco)
- Pacotes Python listados em `requirements.txt`

Instale os pacotes com:

```bash
pip install -r requirements.txt

## 🗃️ Base de Dados
🔗 Download
Baixe o arquivo .bak da base AdventureWorksDW2022 diretamente do site oficial da Microsoft:

👉 https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver17&tabs=ssms

Escolha a versão AdventureWorksDW2022.bak e salve em data/.

## 🛠️ Importação no SQL Server
Abra o SQL Server Management Studio (SSMS) ou DBeaver.

Restaure o arquivo .bak como um novo banco de dados:

Nome sugerido: AdventureWorksDW2022

Verifique se o usuário tem permissão de leitura.

## ⚙️ Configuração do Projeto
Crie o arquivo .env em config/db_config.env com os dados de conexão:
server=localhost
database=AdventureWorksDW2022
user=seu_usuario
password=sua_senha

## 📈 Executando os Notebooks
Abra o notebook notebooks/exploracao.ipynb no Jupyter e execute as células:
Conexão com o banco via conecta_sql.py
Consultas SQL via consultas.py
Visualizações com matplotlib ou seaborn via visualizacoes.py
Exemplos de gráficos gerados:
Vendas por território
Produtos mais vendidos
Vendas por cliente
Vendas por ano
Os gráficos são salvos em outputs/.

## 🖥️ Executando o Dashboard
O dashboard interativo está em dashboards/app.py. Para rodar:
streamlit run dashboards/app.py

## 📚 Créditos
Base de dados: AdventureWorksDW2022 - Microsoft Ferramentas: Python, Pandas, Matplotlib, Seaborn, Streamlit, DBeaver

