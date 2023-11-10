# Get the string value in the variable of s
s = input ("Enter the string:")


l = [] # empty list used to keep the track of unique characters

# iterate through each character in the input string
for char in s:
    if char not in l:
        l.append(char) # append will add the unique character to the list l
        print(char, "occured", s.count(char), "times") # prints the unique characters with the counts


