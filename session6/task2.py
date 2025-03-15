# def checkEven(lst_inst):
#     even_lst = []
#     for i in lst_inst:
#         if i % 2 ==0:
#             even_lst.append(i)
#     return even_lst

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # for loop and if condition

# lst2 = [46, 12, 97, 56, 43, 1, 37]
# # for loop and if condition

# lst3 = [311, 56, 76, 89, 91, 93, 100]

# print(checkEven(lst))

# Take an input of a word and character and return an index of this character
# If no character is available return 'No such character"

# Input: my_func('akumosolutions', 'z')
# Output: "No such character "

def characterChecker(word, character):
    if character in word:
        return word.index(character)
    else:
        return("No such character")
print(characterChecker("akumosolutions", "l"))
print(characterChecker("akumosolutions", "z"))
