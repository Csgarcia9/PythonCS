my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_lists = []

for i in range(len(my_list)):
    if my_list[i] not in new_lists:
        new_lists.append(my_list[i])

print("La lista con elementos únicos:")
print(my_list)
print(new_lists)

