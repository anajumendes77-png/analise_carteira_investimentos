import pandas as pd
dados = pd.read_csv('carteira.csv')

dados.columns = dados.columns.str.upper()
dados.columns = dados.columns.str.strip()
dados = pd.read_csv('carteira.csv', sep=';')

dados['Valor'] = dados['Preço'] * dados['Quantidade']
print(dados.head())

valor_total = dados.groupby('Data')['Valor'].sum()
print(valor_total)

valor_inicial = valor_total.iloc[0]
valor_final = valor_total.iloc[-1]
retorno = (valor_final - valor_inicial)
print (retorno)

retorno_ativos = dados.groupby('Ativo')['Preço'].agg(['first', 'last'])
retorno_ativos['Retornos'] = (retorno_ativos['last'] - retorno_ativos['first']) / retorno_ativos['first']
print(retorno_ativos)

dados.to_csv('dados_tratados.csv', index= False)

