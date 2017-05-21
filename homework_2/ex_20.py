dict1 = {2: 'two', 2: 'two', 4: 'four',
         4: 'four', 5: 'five'}

# Извлекаем уникальные значения словаря
values = ", ".join(set(dict1.values()))

print(values)
