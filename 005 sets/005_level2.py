# Given sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Join A and B
C = A.union(B)
print(C)
# Why use union instead of + to join elements?
# When it comes to sets, using + will result in an error because + is used to join lists, dictionaries that have an order and remember that sets do not have an order, so to correct this gap Python has the union function that can be used in sets.

# Find A intersection B
C = A.intersection(B)
print(C)