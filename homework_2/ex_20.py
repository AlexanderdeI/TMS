dict1 = {1: 'one', 2: 'two', 3: 'three',
         4: 'four', 5: 'five'}

"# Извлекаем значения словаря и форматируем их в строку"
values = list(dict1.values())
values = ", ".join(values)

print(values)
