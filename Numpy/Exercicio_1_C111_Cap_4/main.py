#Exercicio 1 - Cap 4 de C111
#Paulo Otavio - 1732

import numpy as np

print("---------------Exercicio 1-------------")
# 1- Crie um Array de tamanho 21 com valores linearmente espaçados entre 0 e 1
array1 = np.linspace(0, 1, 21)
print(array1)

print("---------------Exercicio 2-------------")
# 2- Crie dois Arrays: um de números pares de 0 até 51
# e outro também de número pares de 100 até 50. Em seguida, concatene e mostre os resultados ordenados

array2 = np.arange(0, 51, 2)
array3 = np.flip(np.arange(50, 101, 2))

concatenar = np.sort(np.concatenate([array2, array3]))
print(concatenar)

print("---------------Exercicio 3-------------")
# 3- Ordene os resultados do array resultante da Questão 2 em ordem decrescente
decrescente = np.flip(concatenar)
print(decrescente)

print("---------------Exercicio 4-------------")
# 4- Crie uma matriz formada somente por 1's de tamanho 3x4
# Em seguida, tranforme-a em um Array 1-D

mtz = np.ones([3, 4])
# A função tolist, converterá em uma lista
remodelando = np.concatenate(mtz.tolist())
print(remodelando)

print("---------------Exercicio 5-------------")
# 5 - Cire uma matriz de tamanho qualquer. Extraia seu número de linhas e colunas,
# multiplique-os, e diga se esta matriz poderia se tornar um vetor com número par ou ímpar de elementos
matriz = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20]
])
# Mostrando a dimensao da matriz
print(matriz.shape)

# Multiplicando as dimensoes da matriz
multiplicacao = matriz.shape[0] * matriz.shape[1]
print(multiplicacao)

if multiplicacao % 2 == 0:
    print("Vetor com numero par de elementos")
else:
    print("Vetor com numero impar de elementos")


