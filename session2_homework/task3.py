#Task 3: Three-Number Maximum
#Take three integer inputs and print the largest one using only if-elif-else conditions.
num1 = int(input("Please input the integer 1: "))
num2 = int(input("Please input the integer 2: "))
num3 = int(input("Print input the integer 3: "))

if num1 > num2 and num1 > num3:
    print("The largest number is:", num1)
elif num2 > num1 and num2 > num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)