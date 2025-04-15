# Concatenando a string "Trinta", "Dias", "De", "Python" em uma unica string, "Trinda Dias de Python".
_trinta = "Trinta"
_dias = "Dias"
_de = "De"
_python = "Python"
espaco = " "
print(_trinta + espaco + _dias + espaco+ _de + espaco + _python)
# Resultado: "Trinta Dias De Python"


# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
_coding = "Coding"
_for = "For"
_all = "All"
_espaco = " "
print(_coding + _espaco + _for + _espaco + _all)
# Resultado: Coding For All


# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding for All"


# Print the variable company using print().
print(company)
# Resultado: Resultado: Coding For All


# Print the length of the company string using len() method and print().
print(len(company))
# Resultado: 14 caracteres


# Change all the characters to uppercase letters using upper() method.
print(company.upper())
# Resultado: CODING FOR ALL


# Change all the characters to lowercase letters using lower() method.
print(company.lower())
# Resultado: coding for all


# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())


# Cut(slice) out the first word of Coding For All string.
_primeiro = company.split(" ")[0]
print(_primeiro)
# Resultado: Coding


# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(True) if (company.index("Coding") > -1 ) else print(False)
print(True) if (company.find("Coding") > -1 ) else print(False)
print(True) if (company.isnumeric()) else print(False)
print(True) if (company.isspace()) else print(False)
print(True) if (company.isalpha()) else print(False)
# Resultados: True,
# True,
# False,
# False,
# False


# Replace the word coding in the string 'Coding For All' to Python.
company =  company.replace("Coding","Python")
print(company)
# Resultado: Python for All


# Change Python for All to Python for Everyone using the replace method or other methods.
replace = company.replace("All","Everyone")
print(replace)
# Resultado: Python for Everyone


# Split the string 'Coding for All' using space as the separator (split()) .
string = "Coding for All"
print(string.split(" "))
# Resultado: ['Coding', 'for', 'All']


# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string.split(","))
# Resultado: ['Facebook', ' Google', ' Microsoft', ' Apple', ' IBM', ' Oracle', ' Amazon']


# What is the character at index 0 in the string Coding For All.
string = "Coding for All"
print(string[0])
# Resultado: C


# What is the last index of the string Coding For All.
print(len(string)-1)
# Resultado: 13


# What character is at index 10 in "Coding For All" string.
print(string[10])
# Resultado: " " (sim, o décimo caractere da string é um espaço)


# Create an acronym or an abbreviation for the name 'Python For Everyone'.
string = "Python For Everyone"
abreviacao = " "
for s in string.split(" "):
    abreviacao = abreviacao + s[0]
print(abreviacao)
# Resultado: PFE


# Use index to determine the position of the first occurrence of F in Coding For All.
string = "Coding For All"
index = string.index("F")
print(index)
# Resultado: 7


# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(string.rfind("1"))
# Resultado: -1


# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
print(string.rfind("because")) # Ultimo because
print(string.index("because")) # Primeiro because
# Resultados: 47,
# 31


# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
slice = string.split()
string_slice =  " ".join(slice[6:9])
print(string_slice)
# Resultado: because because because


# Does 'Coding For All' start with a substring Coding?
string = "Coding For All"
print(string.startswith("Coding"))
# Resultado: True


# Does 'Coding For All' end with a substring coding?
string = "Coding For All"
print(string.endswith("Coding"))
# Resultado: False


# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
string = '   Coding For All      '
print(string.strip())
# Resultado: Coding For All


# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
string =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" ".join(string))
# Resultado: Django Flask Bottle Pyramid Falcon


# Use the string formatting method to display the following:
raio = 10
area = 3.14 * raio ** 2
print(f"A area de um circulo com raio de {raio} é {area} métros quadrados")
# Resultado: A area de um circulo com raio de 10 é 314.0 métros quadrados