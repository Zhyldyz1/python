# Task 5: Number Type Identifier
# Take a single integer input and classify it as follows:
# If it’s positive and even, print "Positive Even"
# If it’s positive and odd, print "Positive Odd"
# If it’s negative and even, print "Negative Even"
# If it’s negative and odd, print "Negative Odd"
# If it’s zero, print "The number is zero"

number = int(input("Enter a number, please: "))

if number == 0:
    print("The number is zero")
elif number > 0:
    if number % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    if number % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")