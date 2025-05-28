# If Condition

# In python and other programming languages the key word if is used to check if a condition is true and to execute the block code. Remember the indentation after the colon.
# syntax
# if condition:
#   this part of code runs for truthy conditions

a = 3
if a > 0:
    print('Verdadeiro') # Verdadeiro

if a < 0:
    print('Verdadeiro') # It will not return anything

a = -1
if a < 0:
    print('Verdadeiro') # Now something will come back
 
# If Else

# If condition is true the first block will be executed, if not the else condition will run.
# syntax
#if condition:
#    this part of code runs for truthy conditions
#else:
#    this part of code runs for false conditions

a = 3
if a < 0:
    print('é um numero negativo') # Returns nothing because a is greater than 0
else:
    print('è um numero positivo') # Returns value


# If Elif Else

# In our daily life, we make decisions on daily basis. We make decisions not by checking one or two conditions but multiple conditions. As similar to life, programming is also full of conditions. We use elif when we have multiple conditions.
# syntax
#if condition:
#    code
#elif condition:
#    code
#else:
#    code

a = 0
if a > 0:
    print('é um numero positivo') # Returns nothing
elif a < 0:
    print('è um numero negativo') # Returns nothing
else:
    print('é zero') # é zero

# Short Hand
# syntax
# code if condition else code

a = 3
print('é um numero positivo') if a > 0 else print('é um numero negativo') # primeira condição atendida, 'é um numero positivo' será impresso

# Nested Conditions
# Conditions can be nested
# syntax
#if condition:
#    code
#    if condition:
#    code

a = 0
if a > 0:
    if a % 2 == 0:
        print('o numero é positivo, inteiro e par')
    else:
        print('é um numero positivo')
elif a == 0:
    print('é zero')
else:
    print('é um numero negativo')


# If Condition and Logical Operators
# syntax
#if condition and condition:
#   code

a = 0
if a > 0 and a % 2 == 0:
    print('é um numero inteiro, positivo e par')
elif a > 0 and a % 2 != 0:
    print('é um numero positivo inteiro')
elif a == 0:
    print('é zero')
else:
    print('é um numero negativo')


# If and Or Logical Operators
# syntax
#if condition or condition:
#    code

usuario = 'James'
level_de_acesso = 3
if usuario == 'admin' or level_de_acesso >= 4:
    print('Acesso permitido')
else:
    print('Acesso negado')


# Exercises: Level 1

# 1.Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

idade = int(input('Quantos anos você tem? '))
if idade >= 18:
    print('Você ja tem idade para dirigir.')
else:
    print(f'Vocẽ ainda nao tem idade para dirigir, precisara esperar {18 - idade} anos ainda')


# 2.Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.

sua_idade = int(input('Quanto anos vocẽ tem? '))
minha_idade = 25
if sua_idade < minha_idade:
    if minha_idade - sua_idade == 1:
        print(f'Você é {minha_idade - sua_idade} ano mais novo que eu.')
    else:
        print(f'Você é {minha_idade - sua_idade} anos mais novo que eu.')
if sua_idade > minha_idade:
    if sua_idade - minha_idade == 1:
        print(f'Vocẽ é {sua_idade - minha_idade} ano mais velho do que eu.')
    else:
        print(f'Vocẽ é {sua_idade - minha_idade} anos mais velho do que eu.')
if minha_idade == sua_idade:
    print('Nós temos a mesma idade.')


# 3.Get two numbers from the user using input prompt.
# If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

n1 = int(input('Insira o primeiro numero: '))
n2 = int(input('Insira o segundo numero: '))
if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n1 < n2:
    print(f'{n1} é menor que {n2}')
else:
    print('Os dois numeros são iguais.')


# Exercises: Level 2

# 1.Write a code which gives grade to students according to theirs scores:

# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

pontuacao = int(input('Qual foi sua pontuação? '))
if pontuacao >= 0 and pontuacao <= 49:
    print('Vocẽ tirou uma nota F.')
elif pontuacao >= 50 and pontuacao <= 59:
    print('Você tirou uma nota D.')
elif pontuacao >= 60 and pontuacao <= 69:
    print('Você tirou uma nota C.')
elif pontuacao >= 70 and pontuacao <= 89:
    print('Você tirou uma nota B.')
elif pontuacao >= 80 and pontuacao <= 100:
    print('Vocẽ tirou uma nota A.')
else:
    print('Sua pontuação não é uma pontuação valida.')


# 2.Check if the season is Autumn, Winter, Spring or Summer.
# If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer

mes = input('Insira uma mẽs: ').lower()
if mes == 'janeiro' or mes == 'fevereiro' or mes == 'março':
    print(f'O mẽs de {mes} faz parte do Inverno')
if mes == 'abril' or mes == 'maio' or mes == 'junho':
    print(f'O mês de {mes} faz parte da Primavera')
if mes == 'julho' or mes == 'agosto' or mes == 'setembro':
    print(f'O mẽs de {mes} pertence ao Verão')
if mes == 'outubro' or mes == 'novembro' or mes == 'dezembro':
    print(f'O mẽs de {mes} pertence ao Outono')


# 3.The following list contains some fruits:

frutas = ['banana', 'pera', 'laranja', 'manga', 'jabuticaba']
fruta_input = input('Digite o nome de uma fruta: ')
if not fruta_input in frutas:
    frutas.append(fruta_input)
    print(frutas)
else:
    print('Esta fruta ja existe na lista')


# Exercises: Level 3

# 1. Here we have a person dictionary. Feel free to modify it!

pessoa = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

 #* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 #* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 #* If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 #* If the person is married and if he lives in Finland, print the information.

if 'is_marred' in pessoa == True:
    print(f'{pessoa["first_name"]} {pessoa["last_name"]} vive em: {pessoa["country"]}. Ele(a) é casado(a)')
else:
    print(f'{pessoa["first_name"]} {pessoa["last_name"]} vive em: {pessoa["country"]}. Ele(a) não é  casado(a)')

skills = pessoa['skills']
middle_skills = len(skills) // 2 

if 'skills' in pessoa:
    print(pessoa['skills'][middle_skills])

if 'skills' in pessoa:
    skills_check = pessoa['skills']
    if 'Python' in skills_check:
        print(skills_check)

if 'JavaScript' in skills_check and 'React' in skills_check:
    print('Ele(a) é uma desenvolvedor(a) front end')
elif 'Python' in skills_check and 'Node' in skills_check and 'MongoDB' in skills_check:
    print('Ele(a) é uma desenvolvedor(a) back end')
elif 'React' in skills_check and 'Node' in skills_check and 'MongoDB' in skills_check:
    print('Ele(a) é uma desenvolvedor(a) fullstack')
else:
    print('desconhecido')
    
# End of python exercises on conditionals.