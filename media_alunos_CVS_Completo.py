from statistics import median
import pandas as pd

## Lendo o arquivo CSV
tabela = pd.read_csv("notas_alunos.csv", sep=",")
print(tabela,'\n')

## Criando novas colunas com Média e "
tabela["Média"] = (tabela["Nota_1"] + tabela["Nota_2"]) / 2
tabela["Situação"] = "Pendente"

## Alterando os valores da tabela Situação
tabela.iloc[(tabela["Média"] < 7) | (tabela["Faltas"] > 5), "Situação"] = "Reprovado"
tabela.iloc[(tabela["Média"] >= 7) & (tabela["Faltas"] <= 5), "Situação"] = "Aprovado"

## Novo arquivo CSV com os dados atualizados
tabela.to_csv("alunos_situacao.csv") 
print(tabela)

## Maior número de faltas
maiorFalta = tabela["Faltas"].max()
print('\nO maior número de faltas: ' +str(maiorFalta))

## Maior média da tabela
maiorMedia = tabela["Média"].max()
print('\nA maior média: ' + str(maiorMedia))

## Média dos valores da tabela
mediaGeral = tabela["Média"].median()
print('\nA média geral: ' + str(mediaGeral))