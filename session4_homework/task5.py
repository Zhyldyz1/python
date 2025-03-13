# Task 5: Create a Diamond Pattern
# Ask the user for a number and print a diamond shape using *.
# Example:
# Enter a number: 5  
#     *  
#    ***  
#   *****  
#  *******  
# *********  
#  *******  
#   *****  
#    ***  
#     *  

h = int(input("Please enter diamond's height:"))
for i in range(h):
    print(" "*(h-i), "*"*(i*2+1))
for i in range(h-2, -1, -1):
    print(" "*(h-i), "*"*(i*2+1))