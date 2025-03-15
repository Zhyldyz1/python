# What is the difference between print() and return
# print() -> to output the value
# return --> only used in function, the purpose is ---> return outputs data type back

# print(type(print("Hello")))

# NoneType- means nothing "pustyshka"
# Every time you use print, youa re just printing, nothing is being stored as data type
# When you use return, you output the data type

def my_func(num):
    if num % 2 == 0:
        print("This is an even number")
    else:
        print("This is an odd number")

print(my_func(4))
print(type(my_func(4)))

# my_func(4) # This is even number --> str
# my_func(9) # This is odd number --> str