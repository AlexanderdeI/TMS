user_input = input('Enter the number: ')

# Проверяем ввод пользователя.
# Если введено не число или больше одного числа,
# сообщаем и прекращаем программу.
if user_input.isnumeric() is not True:
    print("You haven't entered numbers, please restart")
    exit()
elif user_input.count(' ') > 0:
    print('You have entered more than one number, please restart')
    exit()
	
number = int(user_input)

# Проверяем число на четность или нечетность
if number % 2 == 0:
    print('Number {0} is even'.format(number))
else:
    print('Number {0} is uneven'.format(number))
