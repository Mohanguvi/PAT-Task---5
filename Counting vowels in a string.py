# Get a input string
s = input("Enter a string: ")
print (s)
# Initiate variable value as 0 to count the vowel
A = 0
a = 0
E = 0
e = 0
I = 0
i = 0
O = 0
o = 0
U = 0
u = 0

# Iterate through the characters in the string, it will calculate and count the vowels
for char in s:
    if char == 'A':
        A += 1
    if char == 'a':
        a += 1
    elif char == 'E':
        E += 1
    elif char == 'e':
        e += 1
    elif char == 'I':
        I += 1
    elif char == 'i':
        i += 1
    elif char == 'O':
        O += 1
    elif char == 'o':
        o += 1
    elif char == 'U':
        U += 1
    elif char == 'u':
        u += 1
        
# Display the total number of vowels
print("Total number of vowels in the string: ", A+E+I+O+U+a+e+i+o+u)

# Display the counts of each vowel
print("Count of 'A':", A)
print("Count of 'a':", a)
print("Count of 'E':", E)
print("Count of 'e':", e)
print("Count of 'I':", I)
print("Count of 'i':", i)
print("Count of 'O':", O)
print("Count of 'o':", o)
print("Count of 'U':", U)
print("Count of 'u':", u)