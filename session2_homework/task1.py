#Write a program that takes two integer inputs and prints:
#"Both numbers are equal" if they are the same.
#"The first number is greater" if the first number is larger.
#"The second number is greater" if the second number is larger.

# Take integer inputs one and two from the user
num1 = int(input("Please input the integer 1: "))
num2 = int(input("Please input the integer 2: "))
if num1 == num2:
    print("Both numbers are equal")
elif num1 > num2:
    print("The first number is greater")
else:
    print("The second number is greater")