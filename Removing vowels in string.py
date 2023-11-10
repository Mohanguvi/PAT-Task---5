# Getting the string from the user
x = input("Enter s string: ")

vowels = "AEIOUaeiou"  # variable with a value of containing vowel letters

newstring = " "

# iterative through the characters in the string and remove the vowel words only
for char in x:
    if char not in vowels:
        newstring += char

# display the new string without the vowels
print("New string without vowels: ",newstring)
