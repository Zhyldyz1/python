# Input:
# Enter a word: Python
# Output:
# Reversed Word: nohtyP
# Take input from the user
word = input("Enter a word: ")
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word 
print("Reversed Word:", reversed_word)