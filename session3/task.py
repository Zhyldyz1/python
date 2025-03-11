# #Print  numbers from 0-100
# for num in range(101):
#     print(num)

# # range(100-->end; default =0)
# # range (-10- start, 20-end, 2-jump)

# # range (0, 10, 2) --> {0, 2, 4, 6, 8}
# for num in range(-10, 21):
#     print(num)


# #print only even number all the way to 10
# for num in range(10):
#     #range {0, 1, 2, 3, 4, 5, 6...10}
#     #iterable number =1
#     if num % 2 == 0:
#         print(num)

#class task 2:
#character counter

#take an input of the word/sentence
#calculate how many 'a' chacaters are in the word/sentence

#input: akumosolutions 
#output: 1

#Input: banana
#Output: 3

# # Take input from the user
# text = input("Enter a word or sentence: ")

# # Count occurrences of 'a'
# count_a = text.lower().count('a')

# # Print the result
# print("Number of 'a' characters:", count_a)

sentence =input("Input: ")
counter = 0
#n
for char in sentence:
    if char == "a":
        counter = counter + 1

print(counter)

#addition to this task
#istead of taking"a", let the user chose the letter
#sentence or character should be case insensitive (hint: use str.lower()or str.upper()

