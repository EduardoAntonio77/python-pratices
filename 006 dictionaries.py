# Syntax
dicionario_vazio = {}

# Dicionarie with data values
dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3', 'chave4': 'valor4'}

# Dicionarie example:
pessoa = {
    'primeiro_nome': 'Castiel',
    'ultimo_nome': 'Lamonier',
    'idade': 80,
    'nacionalidade': 'Kazakhstan',
    'casado': True,
    'skills': ['Python', 'Flask', 'MySQL',], #  In case of more items assigned to a key, put them in a list
    'endereço': {
        'rua': 'Em algum lugar desse mundão',
        'CEP': '4002-8922'
    } # Yes, it is possible to put a dictionary inside another.
}

# It checks the number of 'key: value' pairs in the dictionary.
dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3', 'chave4': 'valor4'}
print(len(dicionario)) #  4

print(len(pessoa)) #  7

# We can access Dictionary items by referring to its key name.
dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3', 'chave4': 'valor4'}
print(dicionario['chave2']) # valor2
print(dicionario['chave4']) # valor4

print(pessoa['primeiro_nome']) # Castiel
print(pessoa['skills']) # ['Python', 'Flask', 'MySQL']
print(pessoa['skills'][1]) # Flask
print(pessoa['endereço']) # {'rua': 'Em algum lugar desse mundão', 'CEP': '4002-8922'}
print(pessoa['endereço']['rua']) # Em algum lugar desse mundão
print(pessoa['endereço']['CEP']) # 4002-8922
# You must use [] because we are manipulating a list, string or dictionary. () should only be used when calling functions or methods, and when creating tuples.

# Accessing an item by key name raises an error if the key does not exist. To avoid this error first we have to check if a key exist or we can use the get method. The get method returns None, which is a NoneType object data type, if the key does not exist.
print(pessoa.get('primeiro_nome')) # Castiel
print(pessoa.get('cidade')) # None

# We can add new key and value pairs to a dictionary
dicionario['chave5'] = 'valor5'
print(dicionario) # {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3', 'chave4': 'valor4', 'chave5': 'valor5'}

pessoa['trabalho'] = 'contador'
print(pessoa) # {'primeiro_nome': 'Castiel', 'ultimo_nome': 'Lamonier', 'idade': 80, 'nacionalidade': 'Kazakhstan', 'casado': True, 'skills': ['Python', 'Flask', 'MySQL'], 'endereço': {'rua': 'Em algum lugar desse mundão', 'CEP': '4002-8922'}, 'trabalho': 'contador'}

# We can modify items in a dictionary
dicionario['chave1'] = 'valor_um'
print(dicionario) # {'chave1': 'valor_um', 'chave2': 'valor2', 'chave3': 'valor3', 'chave4': 'valor4', 'chave5': 'valor5'}

pessoa['primeiro_nome'] = 'Dicaprio'
print(pessoa) # {'primeiro_nome': 'Dicaprio', 'ultimo_nome': 'Lamonier', 'idade': 80, 'nacionalidade': 'Kazakhstan', 'casado': True, 'skills': ['Python', 'Flask', 'MySQL'], 'endereço': {'rua': 'Em algum lugar desse mundão', 'CEP': '4002-8922'}, 'trabalho': 'contador'}

# We use the "in" operator to check if a key exist in a dictionary
print('chave1' in dicionario) # True
print('chave6' in dicionario) # False

# pop(key): removes the item with the specified key name:
# popitem(): removes the last item
# del: removes an item with specified key name
dicionario.pop('chave1') #removes chave1 item
print(dicionario) # {'chave2': 'valor2', 'chave3': 'valor3', 'chave4': 'valor4', 'chave5': 'valor5'}

dicionario.popitem() # removes the last item
print(dicionario) # {'chave2': 'valor2', 'chave3': 'valor3', 'chave4': 'valor4'}

del dicionario['chave2'] # removes key2 item
print(dicionario)

# The items() method changes dictionary to a list of tuples.
print(dicionario.items()) # dict_items([('chave3', 'valor3'), ('chave4', 'valor4')])

# If we don't want the items in a dictionary we can clear them using clear() method
dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3', 'chave4': 'valor4'}
print(dicionario.clear()) # None

# If we do not use the dictionary we can delete it completely
del dicionario

# We can copy a dictionary using a copy() method. Using copy we can avoid mutation of the original dictionary.
dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3', 'chave4': 'valor4'}
copia_dicionario = dicionario.copy()
print(copia_dicionario) # {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3', 'chave4': 'valor4'}

# The "values" method gives us all the values of a a dictionary as a list.
values = dicionario.values()
print(values) # dict_values(['valor1', 'valor2', 'valor3', 'valor4'])

# End of python exercises on dictionaries