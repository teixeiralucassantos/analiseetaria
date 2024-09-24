import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações do estilo do gráfico
sns.set(style='whitegrid', palette='pastel')

# Carrega os dados, pulando as linhas iniciais e a última
dados = pd.read_excel(r'C:\Users\User\Documents\portfolio\tabela.xlsx', skiprows=6, skipfooter=1)
print(dados)

# Renomeia as colunas do DataFrame
dados.columns = ['idade', 'Masculino', 'Feminino']
dados.loc['total'] = dados.sum()

# Nomeia a última linha como 'total'
dados.loc[dados.index[-1], 'idade'] = 'total'

# Calcula o total geral
total_populacional = dados.loc[dados.index[-1], 'Feminino'] + dados.loc[dados.index[-1], 'Masculino']
print(total_populacional)

# Converte os valores em porcentagens
dados['Masculino'] = dados['Masculino'] / total_populacional * -100
dados['Feminino'] = dados['Feminino'] / total_populacional * 100

# Define a ordem das idades
faixas_etarias = [
    '80 anos ou mais',
    '75 a 79 anos',
    '70 a 74 anos',
    '65 a 69 anos',
    '60 a 64 anos',
    '55 a 59 anos',
    '50 a 54 anos',
    '45 a 49 anos',
    '40 a 44 anos',
    '35 a 39 anos',
    '30 a 34 anos',
    '25 a 29 anos',
    '20 a 24 anos',
    '15 a 19 anos',
    '10 a 14 anos',
    '5 a 9 anos',
    '0 a 4 anos'
]

# Cria os gráficos de barras
sns.barplot(x='Masculino', y='idade', data=dados, order=faixas_etarias, color="teal")
sns.barplot(x='Feminino', y='idade', data=dados, order=faixas_etarias, color="lightseagreen")

# Configurações do gráfico
plt.title("Pirâmide Populacional (%) - Brasil, 2022")
plt.xlabel("Masculino/Feminino")
plt.grid(False)
plt.xticks(ticks=[-4, -3, -2, -1, 0, 1, 2, 3, 4], labels=['4', '3', '2', '1', '0', '1', '2', '3', '4'])
plt.show()

# Carrega os dados novamente
dados = pd.read_excel(r'C:\Users\User\Documents\portfolio\tabela.xlsx', skiprows=6, skipfooter=1)
print(dados.head())

# Renomeia as colunas novamente
dados.columns = ['idade', 'Masculino', 'Feminino']
dados.head()

# Divide os valores por 1.000
dados['Masculino'] = dados['Masculino'] / -1000
dados['Feminino'] = dados['Feminino'] / 1000

# Plota os gráficos de barras novamente
sns.barplot(x='Masculino', y='idade', data=dados, order=faixas_etarias, color="teal")
sns.barplot(x='Feminino', y='idade', data=dados, order=faixas_etarias, color="lightseagreen")

# Título e configurações do gráfico
plt.title("Pirâmide Populacional - Brasil, 2022")
plt.xlabel("Masculino/Feminino")
plt.grid(False)
plt.xticks(ticks=[-8000, -7000, -6000, -5000, -4000, -3000, -2000, -1000, 0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
           labels=['8M', '7M', '6M', '5M', '4M', '3M', '2M', '1M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M'])
plt.show()
