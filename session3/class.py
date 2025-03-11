#Tasks: 3HW 2

#What is the control flow--> part of flow is (if, else, for loops, )while loops, functions)
# Task 4: Password Strength Checker
# Ask the user for a password input. Check and print:
# "Strong password" if the length is at least 8 characters and contains both letters and numbers.
# "Weak password" otherwise.

password = input("Enter your password, please: ")

if len(password) <= 8:
    print("Weak password")
elif password.isalpha() or password.isdigit():
    print("Weak password")
else:
    print("Strong password")