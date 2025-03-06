#Task 3: Simple Calculator
#Create a calculator that takes two numbers and an operator (+, -, *, /, //, %, **) as input and performs the appropriate calculation.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
calculator = input("Enter an operator (+, -, *, /, //, %, **): ")


if calculator == '+':
    result = num1 + num2
elif calculator == '-':
    result = num1 - num2
elif calculator == '*':
    result = num1 * num2
elif calculator == '/':
    result = num1 / num2
elif calculator == '//':
    result = num1 // num2
elif calculator == '%':
    result = num1 % num2
elif calculator == '**':
    result = num1 ** num2
else:
    result = "Error!"

print("Result:", result)