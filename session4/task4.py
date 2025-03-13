
#lst = ["banana", True, False, "apple", 10, "pineapple", "cherry", "apple", 1, 10.3, True]
#With the above list filter to have only string data types
#output: ["banana", "apple", "pineapple", "cherry", "apple", "class"]

lst = ["banana", True, False, "apple", 10, "pineapple", "cherry", "apple", 1, 10.3, True]
# filtered_lst = [item for item in lst if isinstance(item, str)]
# print(filtered_lst)
for element in lst:
    if isinstance(element, str):
        filtered_elements.append(element)
print(filtered_elements)