# Get two string from the user 
s_1 = input("Enter the first string: ")
s_2 = input("Enter the second string: ")


# Check if the sorted character sequences of both strings are the same
anagram = sorted(s_1) == sorted(s_2)

if anagram:
    print(anagram) # print result if the anagram is True
else:              
    print(anagram) # print the result as false if the anagram is not
