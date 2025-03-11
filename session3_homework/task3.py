# Input:
# Enter a number: 5

# Output:
# Factorial of 5 is 120

num = int(input("Please enter any number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"The factorial of {num} is {fact}")