# create a function that takes an integer input and prints if it's Odd or Even
# my_func(10) --> This is even number
# my_func(5) --> This is odd number 

def my_func(num):
    if num % 2 == 0:
        print("This is an even number")
    else:
        print("This is an odd number")

my_func(4)
my_func(9)

