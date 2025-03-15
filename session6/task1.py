

lst_of_num = [1, 2, 2, 3, 4, 4, 5]
counter = 0
filtered_lst = []

for i in lst_of_num:
    if i not in filtered_lst and counter == 0:
        filtered_lst.append(i)
        counter = counter + 1
    else: filtered_lst.pop()

print(filtered_lst)