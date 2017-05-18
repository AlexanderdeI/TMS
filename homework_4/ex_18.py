def factorial(num):
    while num != 0:
        fact = 1
        # Считаем факториал числа
        for n in range(1, num):
            fact *= n
            result = num * fact
        print(result)
        # Уменьшаем исходное число и считаем факториал снова
        num -= 1
    else:
        exit()

print(factorial(50))
