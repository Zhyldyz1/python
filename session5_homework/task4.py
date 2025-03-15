# Task 4
# You are given two dictionaries where the keys represent item names and the values represent their respective counts
# Input: 
# dict1 = {"apple": 3, "banana": 5, "orange": 2}
# dict2 = {"banana": 2, "orange": 4, "grape": 6}

# Output: 
# {
#     "apple": 3,   # Only in dict1
#     "banana": 7,  # 5 (from dict1) + 2 (from dict2)
#     "orange": 6,  # 2 (from dict1) + 4 (from dict2)
#     "grape": 6    # Only in dict2
# }

inp1 = {"apple": 3, "banana": 5, "orange": 2}
inp2 = {"banana": 2, "orange": 4, "grape": 6}

new_inp = {}

for key, value in inp1.items():
    new_inp[key] = value
for key, value in inp2.items():
    if key in new_inp:
       new_inp[key] += value
    else:
       new_inp[key] = value

print(new_inp)


# print(inp1)