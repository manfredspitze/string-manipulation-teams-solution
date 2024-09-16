# Abraham Lincoln
# 03 SEP 20XX
# String Methods in Python

first_name = 'Abraham'

# NOTE: Starting with a Python FUNCTION called len
# len is short for length
# Length function gets the number of characters in a string

print(f'The number of characters in the name {first_name} is: {len(first_name)}')


# Continuing with Python string methods

print(f'Instances of the lowercase letter o in the string Abraham: {first_name.find("o")}')
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


# Output
'''
The number of characters in the name Abraham is: 7
-1
Abraham
ABRAHAM
abraham

Using the isdigit( ) method...
False

Using the isalpha( ) method...
True
2
Abrxhxm
AbrahamAbrahamAbraham
user@user-office:~/Desktop/demos$ /bin/python3 /home/user/Desktop/demos/testing.py
The number of characters in the name Abraham is: 7
Instances of the lowercase letter o in the string Abraham: -1
Abraham
ABRAHAM
abraham

Using the isdigit( ) method...
False

Using the isalpha( ) method...
True
2
Abrxhxm
AbrahamAbrahamAbraham
'''
