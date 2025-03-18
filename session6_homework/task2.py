# Task 2: Convert a Sentence to Abbreviations
# Write a function that takes a sentence as input and returns an abbreviation using the first letter of each word in uppercase.
# Example:
# print(abbreviate("Central Processing Unit"))

# Output:
# "CPU"

# Let's split string into words

def abbreviate(whole_sentence):
    each_word = whole_sentence.split()
# We should look into each word, so that it the first letter in upper case
    first_letter = ""
    for i in each_word: 
        abbreviation = i[0].upper()
        # upper_case = abbreviation
        first_letter += abbreviation
    return first_letter

whole_sentence = input("Please enter your sentence: ")
result = abbreviate(whole_sentence)
print(result)

# print(abbreviate("Enter your sentence: "))
