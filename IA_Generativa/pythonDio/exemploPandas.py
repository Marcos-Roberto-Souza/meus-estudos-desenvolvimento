import pandas as pd
'''
dados = {
    "produto": ["Notebook", "Mouse", "Teclado", "Monitor", "Mouse", "Teclado"],
    "preco": [3500,120,150,1500,120,150]

    }

df = pd.DataFrame(dados)
resultado = df.groupby("produto").mean() #agrupa os dados por produto e calcula a média dos preços para cada produto
print(resultado)
'''
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

print(df.head())#mostra os resultados e dados das primeiras 5 linhas do DataFrame

print(df.info())#mostra o tipo de dados e a quantidade de dados em cada coluna

print(df.describe()) #mostra as estatísticas descritivas para as colunas numéricas do DataFrame, como média, desvio padrão, valores mínimos e máximos, etc.






