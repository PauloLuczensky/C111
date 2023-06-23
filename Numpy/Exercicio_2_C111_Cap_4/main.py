#Exercicio 2 - Cap. 4 - C111
#Paulo Otavio - 1732

import numpy as np

#1-Crie um array de floats com 10 elementos positivos e negativos entre -1 e 1
#Em seguida, multiplique seus valores por 100 e crie um novo vetor apenas com
#a parte inteira destes numeros

print("--------------Exercício 1---------------")
#1.1 - Gerando um vetor de 10 numeros entre -1 e 1
np.random.seed(5)
array = np.random.uniform(-1, 1, 10)

print(array)

#1.2 - Multiplicando cada valor do vetor por 100
array_multiplicado = array * 100
print(array_multiplicado)

#1.3 - Extraindo a parte inteira de cada elemento do vetor
print(np.trunc(array_multiplicado))


print("--------------Exercício 2---------------")
#2 - Crie uma matriz de tamanho 4x4 formada por numeros
#aleatorios inteiros entre 1 e 50;(use seed(10) antes)

np.random.seed(10)
mtz = np.random.randint(1,50,16)
matriz = mtz.reshape(4,4)
print(matriz)

print("--------------Exercício 3---------------")
#3 - Mostre o resultado da media de cada linha e cada coluna da matriz gerada ple questao 2,
#e em seguida, apresente o maior valor das médias para as linhas e também para as colunas

#3.1-Calculando a media de cada linha
print("Linhas")
media_linhas = [matriz.mean(axis=1)[0], matriz.mean(axis=1)[1] , matriz.mean(axis=1)[2],matriz.mean(axis=1)[3]]
print(media_linhas)
#Pegando o maior valor das medias calculadas
print(max(media_linhas))
print("Colunas")
#3.2 - Calculando a media de cada coluna
media_colunas = [matriz.mean(axis=0)[0], matriz.mean(axis=0)[1] , matriz.mean(axis=0)[2],matriz.mean(axis=0)[3]]
print(media_colunas)
#Pegando o maior valor das medias calculadas
print(max(media_colunas))

print("--------------Exercício 4---------------")
#4 - Baseado na matriz gerada na questao 2, mostre a quantidade de aparições
#de cada um dos numeros na mesma.Em seguida, mostre apenas os numeros que aparecem 2 vezes

#4.1 - Mostrando a quantidade de aparições de cada valor na matriz
print(np.unique(matriz, return_counts=True))

#4.2 - Mostrando os numeros que aparecem 2 vezes
duplicado = [] #guardando elementos duplicados numa lista
nao_duplicado = []#guardando os elementos nao duplicados numa lista
for i in mtz:
    if i not in nao_duplicado:
        nao_duplicado.append(i)
    else:
        duplicado.append(i)

print(duplicado)