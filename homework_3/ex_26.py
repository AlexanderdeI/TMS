import random as r

# Список сторон
dice = ['one', 'two', 'three', 'four', 'five', 'six']
# Число бросков
n = 100000
# Словарь для результатов
results = {}

for throw in range(n):
    side = r.choice(dice)
    # Определяем количество выпадения стороны
    if side not in results:
        results[side] = 0
    results[side] += 1

print(results)
