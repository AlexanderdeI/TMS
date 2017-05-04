import random as r

"# Определяем начало и конец интервала"
start = 1
end = 10

"# Генерируем случайное число от 0 до 1"
rand_fract = r.random()

"# Генерируем случайное в определенном промежутке"
"# Отнимаем единицу, чтобы не превысить значения интервала"
rand_int = r.randint(start, end - 1)

"# Складываем сгенерированные числа и округлям до 2-ух знаков"
rand_num = rand_int + rand_fract
rand_num = round(rand_num, 2)

print(rand_num)
