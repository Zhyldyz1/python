#Task 2: Number Swapper
#Write a Python program that takes two numbers as input from the user and swaps their values.

num1 = input("Enter the 1st number: ")
num2 = input ("Enter the 2nd number: ")

num1, num2 = num2, num1

print("\nAfter swapping:")
print("1st number:", num1)
print("2nd number:", num2)