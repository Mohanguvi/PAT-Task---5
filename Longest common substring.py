# Get the two strings from the user input
str1 = input("Enter the string 1: ")
str2 = input("Enter the string 2: ")

# Set operation used to find all possible ways to get the longest common sub-strings between two strings
sub_str1 = {str1[i:j] for i in range(len(str1)) for j in range(i + 1, len(str1) + 1)}
sub_str2 = {str2[i:j] for i in range(len(str2)) for j in range(i + 1, len(str2) + 1)}

# Using intersection to check the longest common sub-string in the two strings
substrings = sub_str1 & sub_str2


# Find the longest common substring value 
longest_common = max(len(substring) for substring in substrings) if substrings else 0

# Longest common sub-string value will be displayed 
print("Length of Longest Common Substring:", longest_common)
