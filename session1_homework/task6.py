# Task 6: Palindrome Checker
# Ask the user to enter a word and check whether it reads the same forward and backward (e.g., "madam" is a palindrome).
#The answer should return True or False

word = input("Enter a word: ")

reversed_word = word[::-1]

palindrome = word == reversed_word

print(palindrome)