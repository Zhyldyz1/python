# Task 2:
# Take an input and count the occurrences of each character.
# Input: programming
# Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}

inp = input("Please enter your word: ")  

#create a list with condition
list = {}  

for char in inp:  
    if char in list:  
        list[char] += 1 
    else:  
        list[char] = 1 

print(list) 