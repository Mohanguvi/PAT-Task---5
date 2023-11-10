# Get the string from the user
x = input("Enter the string: ")

# User_input string displayed
print(x)

# initialize variable value in zero to initiate the character value
n = 0
for char in x: 
    if x.count(char) == 1:
        n += 1           # iterative through the character and count the unique character by for loop

print("Number of unique characters in the string: ",n)