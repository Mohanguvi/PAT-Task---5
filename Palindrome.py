# Get the input string from the user
s = input ("Enter the string: ")

# Given string will be printed
print(s)

# Palindrome condition, Given string is reversed and it should same as the given string

if s == s[::-1]: #using for and range input_string will be reversed and it will check the input string is equal or not.
    print("True") # If it is equal it will print as "True"
else:
    print("False") # If it is not equal it will print as "False"