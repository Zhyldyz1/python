#Task 2: Character Type Identifier
#Ask the user to input a single character. Determine and print:
#"It's a digit" if the character is a number (0-9).
#"It's a letter" if the character is a letter (a-z, A-Z).
#"It's a special character" otherwise.

character = input ("Enter a single character, please: ")

if character.isnumeric():
    print("It's a digit")
elif character.isalpha():
     print("It's a letter")
else:
     print("It is a special character")
