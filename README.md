# Análise da Pirâmide Populacional - Brasil, 2022

Este projeto realiza uma análise visual da pirâmide populacional do Brasil para o ano de 2022, utilizando gráficos de barras para representar a distribuição de homens e mulheres em diferentes faixas etárias.

## Objetivo

O objetivo principal deste código é apresentar a distribuição da população brasileira por idade e sexo, permitindo uma compreensão visual das diferenças entre as populações masculina e feminina nas diversas faixas etárias. Essa análise é útil para estudos demográficos, planejamento de políticas públicas e compreensão de tendências populacionais.

## Bibliotecas Utilizadas

O projeto utiliza as seguintes bibliotecas:

- **Pandas**: Para manipulação e análise de dados.
- **Matplotlib**: Para criação de gráficos.
- **Seaborn**: Para visualizações estatísticas, que facilita a criação de gráficos informativos e esteticamente agradáveis.

## Funcionamento do Código

1. **Carregamento dos Dados**: Os dados são carregados de um arquivo Excel, ignorando as primeiras linhas e a última linha. O arquivo deve estar no caminho especificado.
   
2. **Renomeação de Colunas**: As colunas do DataFrame são renomeadas para facilitar a manipulação, sendo elas: `idade`, `Masculino` e `Feminino`.

3. **Cálculo do Total Populacional**: Uma nova linha é adicionada ao DataFrame, que contém o total de homens e mulheres para cada faixa etária, sendo esta linha nomeada como `total`.

4. **Cálculo de Porcentagens**: Os valores de homens e mulheres são convertidos para porcentagens em relação ao total populacional.

5. **Definição das Faixas Etárias**: As faixas etárias são definidas em uma lista, que é utilizada para a ordenação dos gráficos.

6. **Criação dos Gráficos**: Dois gráficos de barras são gerados usando o Seaborn, um para a população masculina e outro para a feminina. Os gráficos são configurados com títulos e rótulos adequados.

7. **Divisão dos Valores**: Uma nova leitura dos dados é realizada para mostrar os valores absolutos divididos por mil, proporcionando uma segunda visualização da pirâmide populacional.

8. **Exibição dos Gráficos**: Os gráficos gerados são exibidos, mostrando a distribuição da população brasileira em diferentes faixas etárias.

## Visualizações

Os gráficos gerados ajudam a visualizar:

- As proporções de homens e mulheres em cada faixa etária.
- As diferenças entre as populações masculina e feminina.
- Tendências demográficas que podem influenciar a formulação de políticas públicas.

## Conclusão

Este projeto oferece uma análise visual da pirâmide populacional brasileira, destacando as diferenças de gênero nas várias faixas etárias. As visualizações resultantes podem ser úteis para pesquisadores, sociólogos, demógrafos e formuladores de políticas que desejam entender melhor a estrutura populacional do Brasil.

## Como Executar

1. Certifique-se de ter Python instalado em sua máquina.
2. Instale as bibliotecas necessárias:
   ```bash
   pip install pandas matplotlib seaborn openpyxl
