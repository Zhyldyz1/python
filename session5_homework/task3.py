# Task 3
# Take an input of list of numbers, find and print the unique numbers.
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: 1, 3, 5

# numbers = input("Please enter your numbers: ").split()  
# print(numbers)
# new_list = []
# for i in numbers:
#     count = 0
#     for i2 in numbers:
#         if i == i2:
#             count +=1
#     if count == 1:
#        new_list.append(i)
# print(", ".join(new_list))


numbers = input("Please enter your numbers: ").split()  
print(numbers)
new_list = []
for i in numbers:
    if numbers.count(i) == 1:
       new_list.append(i)
print(", ".join(new_list))


