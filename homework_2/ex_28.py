# Оценки за четверть
marks = [4, 5, 5]

# Считаем средний балл
a = float(sum(marks) / len(marks))

# Определяем диапозон и выводим результат
if a >= 3.0 and a < 3.5:
    print('Wii')
elif a >= 3.5 and a <= 4.0:
    print('XBOX 360')
elif a > 4.0:
    print('PS 4')
else:
    print('nothing')
