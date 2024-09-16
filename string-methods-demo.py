# Abraham Lincoln
# 03 SEP 20XX
# String Methods in Python

first_name = 'Abraham'

# NOTE: Starting with a Python FUNCTION called len
# len is short for length
# Length function gets the number of characters in a string

print(f'The number of characters in the name {first_name} is: {len(first_name)}')


# Continuing with Python string methods

print(first_name.find("o"))
print(first_name.capitalize())
print(first_name.upper())
print(first_name.lower())
print()
print('Using the isdigit( ) method...')
print(first_name.isdigit())
print()
print('Using the isalpha( ) method...')
print(first_name.isalpha())
print(first_name.count("a"))
print(first_name.replace("a","x"))
print(first_name*3)
