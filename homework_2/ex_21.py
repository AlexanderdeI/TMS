list1 = input("Введите через пробел элементы первого списка: ")
list2 = input("Введите через пробел элементы второго списка: ")

# Преобразуем строки в списки
list1 = list(list1.split())
list2 = list(list2.split())

# Сортируем списки и сравниваем их
if sorted(list1) == sorted(list2):
    print('Списки равны')
else:
    print('Списки не равны')
