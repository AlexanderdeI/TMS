list1 = [1, 4, 6, 2, 8, 9]
list2 = [3, 4, 5, 8, 1, 2]

# Сортируем списки и преобразуем их в наборы
set1 = set(sorted(list1))
set2 = set(sorted(list2))

# Находим уникальные элементы наборов, что и будет являтся разностью
intersect = set1 ^ set2

print(intersect)
