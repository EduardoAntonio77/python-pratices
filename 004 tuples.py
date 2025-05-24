# Create an empty tuple
tuple = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
irmas = ('Helloa', 'Liz', 'Maria')
irmaos = ('Guilherme', 'Andreas')

# Join brothers and sisters tuples and assign it to siblings
parentes = irmas + irmaos

print(parentes)

# How many siblings do you have?
print("Eu tenho %d irmãos" %(len(parentes)))
# obs: Why use 2 %? The first % inside the string is a space marker, while the % outside the string is a formatting marker (it would be something like the more modern and easy to use F format with the first % being compared to the {} inside the string and the last one being compared to the "f" itself before the string.
# %s → string
# %d → integer
# %f → decimal

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
pai = ('Eduardo',)
mae = ('Viviane',)

parentes = parentes + pai, mae

membros_da_familia = parentes

print(membros_da_familia)




