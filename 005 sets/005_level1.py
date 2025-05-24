# Given sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set  it_companies
print("Lenght of set is :", len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Infosys', 'Firmonyx'])
print(it_companies)

# obs: Why can't you use 'add' to add more than one element to the set, and use update instead?
# sets are sets in random order in which their elements do not repeat, so in a set it is not possible to repeat the same value twice, in the case of add, you can only add one element at a time in a set because add serves to be faster and ensure that only 1 item will be added, unlike update which allows you to add several at once.

# Remove one of the companies from the set it_companies
it_companies.remove('Apple')
print(it_companies)