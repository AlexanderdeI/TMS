list_nums = [2, 4, 5, 6, 4, 3, 5, 6, 7, 3, 5, 6, 3, 2, 1]
list_without_dubl = []

for el in list_nums:
    # Если элемент уже в списке, то он не добавляется
    if el not in list_without_dubl:
        list_without_dubl.append(el)

print(list_without_dubl)
