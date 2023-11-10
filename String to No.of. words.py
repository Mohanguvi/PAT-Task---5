string = input("Enter a sentence: ")  # Get the input sentence from the user

word= 0  # variable value to keep track of the word count

# Iterate through each character in the sentence
for char in string:
    # Check if the character is a having space
    if char == ' ':
        word += 1  # Increment the word count when a space is encountered

'''After intendentation it will add to the word count to account 
for the last word (if there is no space after it) '''
word += 1 

# Display the results of no of words in the user string.
print("Number of words in the sentence:", word)

