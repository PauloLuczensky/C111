#Exercicio 3 Cap 4 - C111

import numpy as np

#1-Abrindo o Dataset
arr = np.loadtxt('space.csv',
                 delimiter=';',
                 encoding='utf8',
                 dtype=str
                 )


print("-----------------Exercicio 1--------------------")
#1 - Apresente a porcentagem de quantas missoões deram certo
#Verificando quantas vezes "Success" apareceu
status_mission = arr[1:4323,7]
success = np.unique(status_mission, return_counts= True)
sucesso = np.array(success)
print(sucesso)
print("Retornando o numero de vezes que uma missão foi bem sucedida:")
print(sucesso[1,3])
print("Porcentagem de quantas missoões deram certo:")
porcentagem_sucesso = (int(sucesso[1,3])/4323)*100
#Arredondando o numero para cima
print(np.ceil(porcentagem_sucesso))

print("-----------------Exercicio 2--------------------")
#2 - Qual a média de gastos de uma missao espacial se baseando  em missoes que possuam valores disponiveis(>0)?
custo = np.unique(arr[1:,6], return_counts=True)
#pegando o array de frequencias
freq_soma = sum(np.unique(arr[1:,6], return_counts=True)[1])
#Total de missoes que gastaram possuem valores disponiveis
total = freq_soma-int(np.array(custo)[1,0])
print("O total de missoes que possuem gastos eh de", total)
#Pegando o array com os valores de custo possíveis
custo1 = np.unique(arr[1:,6], return_counts=True)[0]

#arr = custo1.astype(float)
#print(type(arr))

#Multiplicando o primeiro array com o segundo
custo1_int = np.trunc([float(i) for i in custo1] * np.unique(arr[1:,6], return_counts=True)[1])
#custo1_int = np.trunc(arr * freq_soma )
#Preço total
print("O custo total foi de",  sum(custo1_int))
#Média de gastos
print("A media de gastos eh de ", np.trunc(sum(custo1_int)/total))

print("-----------------Exercicio 3--------------------")
#3 - Encontre quantas missoes espaciais foram realizadas pelos EUA neste Dataset

missoes = arr[1:4323, 2]
missions = missoes.reshape(1,4322)
#Mostrando as missoes feitas
print(missions)

#Vendo quantas missoes possuem USA
print("Numero de missoes que possuem USA")
print(len(arr[np.char.find(arr,'USA') > 0]))# retorna os valores

print("-----------------Exercicio 4--------------------")
#Qual a missao mais cara feita pela Space X
#Buscando a empresa e seu respectivo gasto

spacex = arr[arr[:,1] == 'SpaceX']
print("Mostrando todas as missoes da Space X")
print(spacex)
valores_spacex = spacex[1:,6].astype(float)
print("Mostrando a missao de maior custo da SpaceX")
print(np.max(valores_spacex))


print("-----------------Exercicio 5--------------------")
#Mostre o nome das empresas que já realizaram Missoes Espaciais juntamente
#com suas respectivas quantidades de missões
#empresa = np.unique(arr[1:,1], return_counts=True)[0]
#quantas missoes foram realizadas por cada empresa
empresa = np.unique(arr[1:, 1], return_counts=True)
print(empresa)
print("Mostrando cada empresa e a quantidade de cada missao executada por elas")
print(np.stack((empresa[0],empresa[1]), axis = 1))
