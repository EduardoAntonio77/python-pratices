# Loops
# Life is full of routines. In programming we also do lots of repetitive tasks. In order to handle repetitive task programming languages use loops. Python programming language also provides the following types of two loops:

# 1.while loop
# 2.for loop

# While Loop
# We use the reserved word while to make a while loop. It is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the lines of code after the loop will be continued to be executed.

# syntax
# while condição:
#   código ficara aqui

# Example:

contagem = 0
while contagem < 5:
    print(contagem)
    contagem = contagem + 1

# In the above while loop, the condition becomes false when count is 5. That is when the loop stops. If we are interested to run block of code once the condition is no longer true, we can use else.

# syntax
# while condição:
#   código ficara aqui
# else:
#   código ficara aqui

# Example:
contagem = 0
while contagem < 5:
    print(contagem)
    contagem = contagem + 1
else:
    print(contagem)

# The above loop condition will be false when count is 5 and the loop stops, and execution starts the else statement. As a result 5 will be printed.

# Break and Continue - Part 1

# Break: We use break when we like to get out of or stop the loop.

# syntax
# while condição:
# código ficara aqui
#   if outra_condição:
#       break

# Example:

contagem = 0
while contagem < 5:
    print(contagem)
    contagem = contagem + 1
    if contagem == 3:
        break

# The above while loop only prints 0, 1, 2, but when it reaches 3 it stops.

contagem = 0
while contagem < 5:
    if contagem == 3:
        contagem = contagem + 1
        continue
    print(contagem)
    contagem = contagem + 1

# The above while loop only prints 0, 1, 2 and 4 (skips 3).

# For loop.

# A for keyword is used to make a for loop, similar with other programming languages, but with some syntax differences. Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# For loop with list:

# syntax
# for item in lista:
#   código ficara aqui

# Example:

numeros = [0, 1, 2, 3, 4, 5]
for numero in numeros: # numero é apenas um nome temporario para se referir aos elementos existentes na lista
    print(numero) # Agora os numeros serão exibidos linha por linha, do 0 ao 5

# For loop with string

# syntax
# for elemento in string:
#   código ficara aqui

# Example:

linguagem = 'Python'
for letra in linguagem:
    print(letra)

for i in range(len(linguagem)):
    print(linguagem[i])

# For loop with tuple

# syntax
# for item in tupla:
#   código ficara aqui

# Example:

numeros = (0, 1, 2, 3, 4, 5)
for numero in numeros:
    print(numero)

# For loop with dictionary Looping through a dictionary gives you the key of the dictionary.

# syntax
# for item in dicionario:
#   código ficara aqui

# Example:

pessoa = {
    'primeiro_nome': 'Dicaprio',
    'ultimo_nome': 'Lamonier',
    'idade': 25,
    'estado': 'Acre',
    'casado': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'endereco': {
        'rua': 'Em algum lugar por ai',
        'CEP': '02210'
    }
}
for chave in pessoa:
    print(chave)

for chave, valor in pessoa.items():
    print(chave, valor) # desta forma mostramos chaves e valores.

# Loops in set

# syntax
# for item in set:
#   código ficara aqui

# Example:

empresas_de_ti = {'Dell', 'Lenovo', 'Microsoft', 'Positivo', 'Apple'}
for empresa in empresas_de_ti:
    print(empresa)

# Break and Continue - Part 2

# Short reminder: Break: We use break when we like to stop our loop before it is completed.

# syntax
# for item in sequencia:
#   código ficara aqui
#   if condição:
#       break

# Example:

numeros = (0,1,2,3,4,5)
for numero in numeros:
    print(numero)
    if numero == 3:
        break

# In the above example, the loop stops when it reaches 3.

# Continue: We use continue when we like to skip some of the steps in the iteration of the loop.

# syntax
# for item in sequencia:
#   código ficara aqui
# if condição:
#   continue

# Example:

numeros = (0,1,2,3,4,5)
for numero in numeros:
    print(numero)
    if numero == 3:
        continue
    print('O proximo número deve ser', numero + 1) if numero != 5 else print('fim do loop') # Se for usar a forma abreviada, sempre colocar obrigatoriamente o if e else

# In the example above, if the number equals 3, the step after the condition (but inside the loop) is skipped and the execution of the loop continues if there are any iterations left.

# The Range Function

# The range() function is used list of numbers. The range(start, end, step) takes three parameters: starting, ending and increment. By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end). Creating sequences using range

# Example:

lista = list(range(11))
print(lista) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
conjunto = set(range(1, 11)) # 2 argumentos indicam o inicio e o fim da sequencia, por padrão as etapas serão definidas em 1
print(conjunto) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lista = list(range(0,11,2)) # criara uma sequencia pulando de 2 em 2 numeros de 0 a 11.
print(lista) # [0, 2, 4, 6, 8, 10]
conjunto = set(range(0,11,2))
print(conjunto) # {0, 2, 4, 6, 8, 10}

# syntax
# for item in range(inicio, end, etapas):

# Example:

for numero in range(11):
    print(numero) # exibira os numeros de 0 a 10, não incluindo o 11.

# Nested For Loop
# We can write loops inside a loop.

# syntax
# for x in y:
#   for t in x:
#       print(t)

# Example:

pessoa = {
    'primeiro_nome': 'Dicaprio',
    'ultimo_nome': 'Lamonier',
    'idade': 125,
    'estado': 'Acrê',
    'casado': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'endereco': {
        'rua': 'Em algum lugar por ai',
        'CEP': '02210'
    }
}
for key in pessoa:
    if key == 'skills':
        for skill in pessoa['skills']:
            print(skill)

# For Else

# If we want to execute some message when the loop ends, we use else.

# syntax
# for item in range(inicio, fim, etapas)
#   faça algo
# else:
#   print('Fim do loop')

# Example:

for numero in range(11):
    print(numero) # exibira de 0 a 10, não incluindo o 11
else:
    print('O loop acabou no numero', numero)

# Pass

# In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors. Also we can use it as a placeholder, for future statements.

# Example:

# for numero in range(6):
#   pass
# nota mental (ignorar): ainda acho engraçado como existe uma instrução em python que NAO FAZ NADA!


# Exercises:

# Exercises: Level 1

# 1. Iterate 0 to 10 using for loop, do the same using while loop.

for numero in range(11):
    print(numero)
print('Fim do loop for')

numero = 0
while numero < 11:
    print(numero)
    numero = numero + 1
print('fim do loop while')

# 2. Iterate 10 to 0 using for loop, do the same using while loop.

for numero in range(10, -1, -1):
    print(numero)
print('Fim do loop for inverso')

numero = 10
while numero != -1:
    print(numero)
    numero = numero - 1
print('Fim do loop while inverso')


# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

Hashtag = '#'
quantidade = 0
while quantidade < 8:
    print(Hashtag * quantidade)
    quantidade = quantidade + 1


# 4.Use nested loops to create the following:
'''
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
'''

for numero in range(7):
    print('# # # # # # # #')
    if numero == 8:
        break


# 5.Print the following pattern:

'''
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
'''

numero = 0
while numero < 11:
    print(f"{numero} X {numero} = {numero * numero}")
    numero = numero + 1


# 6.Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

lista = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in lista:
    print(item)


# 7.Use for loop to iterate from 0 to 100 and print only even numbers.

for numero in range(0, 101):
    if numero % 2 == 0:
        print(numero)


# 8.Use for loop to iterate from 0 to 100 and print only odd numbers

for numero in range(0, 100):
    if numero % 2 != 0:
        print(numero)


# Exercises: Level 2

# 1.Use for loop to iterate from 0 to 100 and print the sum of all numbers.

numero_atual = 0
for numero in range(0, 101):
    numero_atual = numero_atual + numero
    if numero == 100:
        print(f'A soma de todos os numero de 0 a 100 é {numero_atual}.')


# 2.Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

numero_par_atual = 0
numero_impar_atual = 0
for numero in range(0,101):
    if numero % 2 == 0:
        numero_par_atual = numero_par_atual + numero
        if numero == 100:
            break
    if numero % 2 != 0:
        numero_impar_atual = numero_impar_atual + numero
        if numero == 100:
            break
print(f'A soma de todos os numeros pares é {numero_par_atual} .E a soma de todos os números impares é {numero_impar_atual}.')


# Exercises: Level 3

# 1.Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
from estados import countries

for estado in countries:
    if 'land' in estado:
        print(estado)

# 2.This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
lista = ['banana', 'laranja', 'manga', 'limão']
lista_inversa = []
for fruta in range(len(lista)-1,-1,-1):
    lista_inversa.append(lista[fruta])
print(lista_inversa)

# 3.Go to the data folder and use the estados_data.py file.

# I.What are the total number of languages in the data
from estados_data import paises

dados = paises
lista_de_linguas = set()
for pais in dados:
    linguas = pais.get('languages')
    lista_de_linguas.update(linguas)
print(f'O numero total de linguagens existentes é {len(lista_de_linguas)}.')

# II.Find the ten most spoken languages from the data.
dados = paises
contador_de_linguas = {}
for pais in dados:
    linguas = set(pais.get('languages'))
    for lingua in linguas:
        if lingua in contador_de_linguas:
            contador_de_linguas[lingua] += 1
        else:
            contador_de_linguas[lingua] = 1
linguas_ordenadas = sorted(contador_de_linguas.items(), key=lambda item: item[1], reverse=True)
top_10_linguas = linguas_ordenadas[:10]

print('-Top 10 linguas mais presentes-')
for lingua, quantidade in top_10_linguas:
    print(f'{lingua} com {quantidade} paises presentes')

# III.Find the 10 most populated countries in the world
dados = paises

populacao_por_pais = []

for pais in dados:
    nome = pais.get('name')
    populacao = pais.get('population')
    populacao_por_pais.append((nome, populacao))

populacao_ordenada = sorted(populacao_por_pais, key=lambda item: item[1], reverse=True)

top_10_paises = populacao_ordenada[:10]

print('-Top 10 paises mais populosos-')
colocacao = 0
for pais, populacao in top_10_paises:
    print(f'{colocacao + 1}º {pais} com {(populacao)} pessoas')
    colocacao = colocacao + 1

# End of exersises today.