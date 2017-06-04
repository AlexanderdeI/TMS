dict1 = {'1': 'one', '2': 'two', 'hi': 'привет',
         'no': 'нет', 'yes': 'да'}

# Вводим ключ
key_input = input('Input key of dictionary: ')

# Выводим значение по ключу
print(dict1.get(key_input, "Empty"))
