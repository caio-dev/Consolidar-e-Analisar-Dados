import pandas as pd
import os

# Armazenando o caminho dos arquivos em uma variável
caminho = 'C:/Users/caioc/PycharmProjects/ConsolidarBaseAlunos/repositorio'

# Criando dataframe para manipular os dados
df = pd.DataFrame()

for f in os.listdir(caminho):
    # Percorrendo cada arquivo do repositório
    frames = pd.read_excel(caminho + '/' + f, engine='openpyxl')
    # Unificando os arquivos no dataframe
    df = df.append(frames, ignore_index=True)

# Informações básicas da base de dados
def info_base():
    print('Informações básicas da base de dados!')
    print('Dimensões', df.ndim)
    print('Elementos / Celulas: ', df.size)
    print('Número de Linhas: ', len(df))
    print('Linhas e Colunas: ', df.shape)
    print('Colunas: ', df.columns)

# Trazer os valores agregados por ano
def valor_por_ano():
    vendas_ano = df[['Ano', 'Valor']].groupby('Ano').sum()
    print(vendas_ano)

# Trazer os valores agregados por Produto
def valor_por_produto():
    vendas_produto = df[['Produto', 'Valor']].groupby('Produto').sum()
    print(vendas_produto)

# Trazer os valores agregados por região
def valor_por_regiao():
    vendas_regiao = df[['Região', 'Valor']].groupby('Região').sum()
    print(vendas_regiao)


