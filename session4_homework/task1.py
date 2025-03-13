#Task 1: Reverse a List
# Write a program that reverses a list using a for loop.
# Example:
# # Input:
# Enter numbers separated by space: 1 2 3 4 5
# # Output:
# Reversed List: [5, 4, 3, 2, 1]

number = input("Please input your numbers: ").split()
reversed_numbers = []
for i in range(len(number)):
    reversed_numbers.append(number[-(i+1)])
print("Reversed List: ", reversed_numbers)