# lst = ["Hello", 2, 10, True]

# print(lst.index(True))

# # 0- False
# # 1- True



# List Comprehensions --> generate a list of elements using a single line
# Create me a list of even number until 10

# lst = []
# for num in range(1, 11):
#     if num % 2 == 0:
#      lst.append(num)
# print (lst)

# lst_of_num = [char for char in range(0, 11, 2) if char % 2 == 0]
# print(lst_of_num)

# # "aKumoSolutions"---> ['a', 'K', ... 's']
# lst = [char for char in "aKumoSolutions"]
# print(lst)

# task:
# Create a list of square numbers from 1-10 using list comprehension
# num * num
# output
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# squares = [num * num for num in range(1, 11)]
# print(squares)

# for num in range(1, 11):
#     print(num * num)


# tpl = (1, 2, True, 10.10, "Hello", 1)
# print(tpl)
# print(type(tpl))
# print(tpl[-2])

# tpl = (1, 0, -10, 8, 7)
# ans = sorted(tpl)
# print(tuple(ans))


# # tpl = (1, 0, -10, 8, 7)
# tpl = [i for i in range(1, 10)]
# print(tpl)

# jan_class = {
#     "beka": "prius",
#     "iana": "cake",
#     "erkin": "coffee",
#     "kostya": "massage",
#     "aibek": "english teacher",
#     "aigerim": "ten years",
#     "cuneyt": "homeworks",
#     "jyldyz": "uni student",
#     "gulnaz": "roses"
# }

# print((jan_class.items()))


