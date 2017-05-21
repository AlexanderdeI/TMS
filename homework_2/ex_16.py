dict1 = {1: 'one', 2: 'two', 3: 'three'}
dict2 = {4: 'four', 5: 'five', 6: 'six'}

# Первый способ
# Присоединяем элементы dict2 в dict1
dict1.update(dict2)
print(dict1)

# Второй способ
new_dict = dict(list(dict1.items()) + list(dict2.items()))
print(new_dict)
