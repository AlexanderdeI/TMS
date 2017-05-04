import string

'''#Создаем строки с которыми будем искать пересечения
    для определения наличия символов'''
up_lett = set(string.ascii_uppercase)
low_lett = set(string.ascii_lowercase)
special = set(string.punctuation)

password = input('Введите пароль: ')

'''# Создаем пустой список, в который
     будем добавлять информацию об ошибках'''
errors = []

"# Проверяем пароль на соответствиое условиям"
if len(password) < 6 or len(password) > 16:
    d = 'пароль не подходит по размеру'
    errors.append(d)
if not set(password) & up_lett:
    d1 = 'пароль не содержит больших букв'
    errors.append(d1)
if not set(password) & low_lett:
    d2 = 'пароль не содержит маленьких букв'
    errors.append(d2)
if not set(password) & special:
    d3 = 'нет специальных символов'
    errors.append(d3)

"# Выводим ошибки"
print(errors)
