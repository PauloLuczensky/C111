# Primeiro Exercício de C111

print("----------------------------Exercicio 1---------------------------------")
#1- Crie uma lista com os 5 primeiros colocados do Campeonato Mundial de Futebol, na ordem de colocação.

times = ['Real Madrid', 'Barcelona', 'Manchester City', 'PSG', 'Milan']

#a) Mostre os 3 primeiros colocados

print(times[0 : 3])

#b) Mostre os dois últimos colocados

print(times[3:5])

#c) Mostre uma lista com os times em ordem alfabética

print(sorted(times))

#d) Mostre em que posição da tabela está o Barcelona

print("A posição do Barcelona é", times.index('Barcelona'))

print("----------------------------Exercicio 2---------------------------------")
#2- Crie dois cojuntos, um para cada loja. Identifique quais modelos de smatrphones cada uma delas vendem.
# Em seguida, mostre quais modelos no total você terá opção de comprar se visitá-las e
# quais modelos se encontram disponíveis em ambas as lojas.

loja1 = {'Iphone', 'Samsung Galaxy', 'Blackberry', 'Nokia'}

loja2 = {'Nokia', 'Motorola', 'Asus', 'LG', 'Iphone'}

#2.1 - Mostrando o numero de elementos de cada loja

print("A loja 1 possui", len(loja1),"celulares e a loja 2 possui", len(loja2), "celulares")

#2.2 - Encontre quais modelos estão disponíveis em ambas as lojas

#print(loja1 & loja2)
print("Os modelos que estão disponíveis em ambas as lojas são:",loja1.intersection(loja2))

print("----------------------------Exercicio 3---------------------------------")
#3- Faça um programa que leia o nome e a média de um aluno e guarde-os em um dicionário. Em seguida, a
# partir da média (se for >= 60), gere a situação final do aluno 'AP'  ou 'RP' e também guarde no dicionário.
# No final mostre o conteúdo do dicionário.

#3.1) Inserindo o nome a media do aluno

nome_aluno = input("Insira o nome do aluno: ")
media_aluno = input("Insira a media do aluno: ")

#Vendo se o aluno passou ou não
if int(media_aluno) >= 60:
    final = "AP"
    print("AP")
else:
    final = "RP"
    print("RP")

aluno = {'nome': nome_aluno, 'media': int(media_aluno), 'situacao_final': final}

#Mostrando conteúdo do dicionário
print(aluno)
