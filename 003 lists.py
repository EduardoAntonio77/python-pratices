# Declare an empty list
list = []

# Declare a list with more than 5 items
mylist = ['Maçã', 'Cebola', 'Beterraba', 'Mamão', 'Uva']


# Find the length of your list
print(len(mylist))
# Resultado: 5


# Get the first item, the middle item and the last item of the list
print(mylist[0])
print(mylist[len(mylist)-1])
print(mylist[3])
# Resultado: Maçã,
# Uva
# Mamão


# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_list = ['Eduardo', 18, 75, 'Solteiro', 'Na Casa do caralho']
print(mixed_list)
# Resultado: ['Eduardo', 18, 75, 'Solteiro', 'Na Casa do caralho']


# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']


# Print the list using print()
print(empresas)
# Resultado: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']


# Print the number of companies in the list
print(len(empresas))
# Resultado: 7


# Print the first, middle and last company
print(empresas[0])
print(empresas[len(empresas)-1])
print(empresas[int(len(empresas)/2)])
# Resultado: Facebook,
# Amazon,
# Apple


# Print the list after modifying one of the companies
empresas[0] = 'Sony'
print(empresas)
# Resultado: ['Sony', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']


# Add an IT company to it_companies
empresas.append("TCS")
print(empresas)
# Resultado: ['Sony', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'TCS']


# Insert an IT company in the middle of the companies list
empresas.insert(int(len(empresas)/2)-1, "Infosys")
print(empresas)
# Resultado: ['Sony', 'Google', 'Microsoft', 'Infosys', 'Apple', 'IBM', 'Oracle', 'Amazon', 'TCS']


# Change one of the it_companies names to uppercase (IBM excluded!)
print(empresas[0].upper())
# Resultado: SONY


# Check if a certain company exists in the it_companies list
if "Microsoft" in empresas:
    print(True)
else:
    print(False)
# Resultado: True


# Sort the list using sort() method
empresas.sort()
print(empresas)
# Resultado: ['Amazon', 'Apple', 'Google', 'IBM', 'Infosys', 'Microsoft', 'Oracle', 'Sony', 'TCS']


# Reverse the list in descending order using reverse() method
empresas.reverse()
print(empresas)
# Resultado: ['TCS', 'Sony', 'Oracle', 'Microsoft', 'Infosys', 'IBM', 'Google', 'Apple', 'Amazon']


# Slice out the first 3 companies from the list
print(empresas[:3])
# Resultado: ['TCS', 'Sony', 'Oracle']


# Slice out the last 3 companies from the list
print(empresas[-3:])
# Resultado: ['Google', 'Apple', 'Amazon']


# Slice out the middle IT company or companies from the list
num_of_elements = 3
start = (len(empresas) // 2) - (num_of_elements // 2)
end = (len(empresas) // 2) + (num_of_elements // 2)
print(empresas[start: end + 1])
# Resultado: ['Microsoft', 'Infosys', 'IBM']


# Remove the first IT company from the list
empresas.pop(0)
print(empresas)
# Resultado: ['Sony', 'Oracle', 'Microsoft', 'Infosys', 'IBM', 'Google', 'Apple', 'Amazon']


# Remove the last IT company from the list
empresas.pop(-1)
print(empresas)
# Resultado: ['Sony', 'Oracle', 'Microsoft', 'Infosys', 'IBM', 'Google', 'Apple']


# Remove all IT companies from the list
empresas.clear()
print(empresas)
# Resultado: []


# Destroy the IT companies list
del(empresas)


# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
# Resultado: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']


# # After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack.append('Python')
full_stack.append('SQL')
print(full_stack)
# Resultado: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB', 'Python', 'SQL']