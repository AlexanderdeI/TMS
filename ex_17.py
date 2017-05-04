dict1 = {'1': 'one', '2': 'two', 'hi': 'привет',
         'no': 'нет', 'yes': 'да'}

"# Вводим ключ"
key_input = input('Input key of dictionary: ')

'''Если ключ в словаре присваиваем
   значение и выводим, в др.случае Пусто'''
if key_input in dict1:
    key_value = dict1[key_input]
    print(key_value)
else:
    print('Empty')
