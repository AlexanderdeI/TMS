user_input = input('Enter the year: ')

'# Проверяем ввод пользователя.'
'# Если введено не число или больше одного числа,'
'# сообщаем и прекращаем программу.'

if user_input.isnumeric() is not True:
    print("You haven't entered numbers, please restart")
    exit()
elif user_input.count(' ') > 0:
    print('You have entered incorectly number of the year')
    exit()

year = int(user_input)

'# Проверяем год на високосность в соответсвии с уловиями'

if (year % 4 == 0 or
    year % 400 == 0 and
    year % 100 != 0):
    print('Year {0} is leap year'.format(year))
else:
    print('Year {0} is not leap year'.format(year))
