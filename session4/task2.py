# Task 2: Reverse a Word using for loop (please don't reverse a string using word[::-1])
# Input:
# Enter a word: Python
# Output:
# Reversed Word: nohtyP

# Task 4: Password Verification (Limited Attempts)
# secret password = Python123
# Input:

# Enter the password: hello
# Wrong password. Try again.

# Enter the password: python
# Wrong password. Try again.

# Enter the password: Python123
# Access Granted!


# Task 5
# Input:
# Enter a word: CODE

# Output:
# C
# CO
# COD
# CODE

# Task 2: Reverse a Word using for loop (please don't reverse a string using word[::-1])
# Enter a word: Python
# Reversed Word: nohtyP

# inp = input("Input: ")
# reversed_word = ""

# for i in range(len(inp), 0, -1):
#     print(inp[i - 1])
#     reversed_word = reversed_word + inp[i - 1]

# print(reversed_word)


# Task 5
# Input:
# Enter a word: CODES
# Output:
# C
# CO
# COD
# CODE
# CODES


# inp = input("Input: ")

# for char in range(len(inp)):
#     print(inp[: char + 1])


# Task 4: Password Verification (Limited Attempts)
# secret password = Python123
# Input:

# Enter the password: hello
# Wrong password. Try again.

# Enter the password: python
# Wrong password. Try again.

# Enter the password: Python123
# Access Granted!


# secret_password = "Python123"

# inp = input("Input: ")
# for attempts in range(2):
#     if inp == secret_password:
#         print("Access Granted")
#         break
#     else:
#         inp = input("Hey, Wrong Password. Please Try again: ")


# Agenda
# While Loop
# List
# Break, continue, pass

# for loops --> sequence ---> it has an start and end point "Hello"
#                        ---> it has an start and end point "range(10) {0, 1, -- 9}"
#                        ---> iterator

# while takes only boolean data type, which mean it will run until the condition is False

# Syntax
# while <condition>:
#    <code>


# secret_password = "Python123"

# inp = input("Input: ")
# max_attempts = 3
# attempts = 1

# while attempts < max_attempts:
#     if secret_password != inp:
#         attempts = attempts + 1
#         inp = input("Wrong Password. Please try again: ")
#     else:
#         print("Access Granted")
#         break


# max_attempts = 3
# attempts = 0

# while 4 <= max_attempts:  ## Runs infinetly until it turns to False
#     print(attempts)
#     attempts = attempts + 1

lst_names = [
    "Esen",
    "Beka",
    "Iana",
    "Erkin",
    "Aigerim",
    "Kostya",
    "Jyldyz",
    "Cuneyt",
    "Gulnaz",
    "Aibek",
]

#Ask for input of character, prin t names that contains this character
#Note: the program should be case insensitive)

#Inpit: r
#Output:
#Erkin
#Aigerim

char = input("Enter a character: ").lower()
print("Names containing the character:")
for name in lst_names:
    if char in name.lower():
        print(name)