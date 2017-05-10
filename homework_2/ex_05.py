import random as r

print('Hello! I guessed the number from 1 to 5.')
print('Try to guess it.')

start = 1
end = 5
random_num = r.randrange(start, end)

user_num = input('Enter the number from 1 to 5: ')

"""Проверяем ввод пользователя.
   Если введено не число,
   больше одного числа или задан неверный диапозон
   сообщаем и прекращаем программу."""

if user_num.isnumeric() is False:
    print("You haven't entered numbers, please restart")
    exit()
elif user_num.count(' ') > 0:
    print('You have entered more than one number, please restart')
    exit()
elif (int(user_num) < 1 or
      int(user_num) > 5):
        print('The number in the wrong range')
        exit()

'# Сравниваем числа и выводим результат'
if random_num == int(user_num):
    print('You win! I guessed the number {0}.'.format(random_num))
else:
    print('You lose. I guessed the number {0}.'.format(random_num))
