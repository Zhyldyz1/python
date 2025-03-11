# Input:
# Enter a word: CODE

# Output:
# C
# CO
# COD
# CODE

word = input("Please enter your word: ")

for i in range(len(word)):
    print(word[:i+1])