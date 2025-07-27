import pandas as pd
# carregar a base de dados csv
df = pd.read_csv('campanha-instagram.csv')

# visualizar as primeiras linhas
print(df.head())

# mostrar nomes reais das colunas da planilha
print(df.columns)

# substituir vírgula por ponto e converter para número
df['Gasto'] = pd.to_numeric(df['Gasto'].str.replace(',', '.'), errors='coerce')
df['Cliques'] = pd.to_numeric(df['Cliques'], errors='coerce')
df['Impressões'] = pd.to_numeric(df['Impressões'], errors='coerce')

# Criar colunas de métricas
df['CTR por dia'] = (df['Cliques'] / df['Impressões']) * 100
df['CPC por dia'] = df['Gasto'] / df['Cliques']

import matplotlib.pyplot as plt
import seaborn as sns
# Top 5 dias com maior CTR
top5_ctr = df.sort_values(by= 'CTR por dia', ascending = False).head(5)

plt.figure(figsize=(10, 6))
sns.barplot(data=top5_ctr, x='Dia', hue='Dia', palette='Blues_d', legend=False)
plt.title('Top 5 Dias com Maior CTR')
plt.ylabel('CTR por dia')
plt.xlabel('Dia')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig('grafico_top5_ctr.png') #salva a imagem do gráfico na pasta


# Top 5 dias com maior gasto
top5_gasto = df.sort_values(by= 'Gasto', ascending = False).head(5)
plt.figure(figsize=(10, 6))
sns.barplot(data=top5_gasto, x='Dia', hue='Gasto', palette='Blues_d', legend=False)
plt.title('Top 5 Dias com Maior Gasto')
plt.ylabel('Gasto')
plt.xlabel('Dia')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig('grafico_top5_gasto.png') #salva a imagem do gráfico na pasta



