# Two strings
str1 = input("Enter the string 1: ")
str2 = input("Enter the string 2: ")

# Generate all substrings for each string
sub_str1 = {str1[i:j] for i in range(len(str1)) for j in range(i + 1, len(str1) + 1)}
sub_str2 = {str2[i:j] for i in range(len(str2)) for j in range(i + 1, len(str2) + 1)}

# Find the common substrings using set intersection
substrings = sub_str1 & sub_str2

# Initialize a counter for common substring occurrences
count = 0

# Count the occurrences of common substrings in both strings
for common_substring in substrings:
    count1 = str1.count(common_substring)
    count2 = str2.count(common_substring)
    count += min(count1, count2)

# Output the result
print("Common substrings count:", count)