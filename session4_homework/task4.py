# Task 4: Find the Second Largest Number in a List (No max() or sort())
# Ask the user to enter a list of numbers. Find and print the second largest number without using max() or sort().
# Example:
# Enter numbers: 10 45 78 23 89 56  
# Second largest number: 78

numbers = input("Please enter your numbers: ").split()
numbers = [int(num) for num in numbers]
largest = numbers[0]
second_largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num  
for num in numbers:
    if num > second_largest and num != largest:
        second_largest = num  
print("Your second largest number is: ", second_largest)