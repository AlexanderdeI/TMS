# Создаем пустой список куда будем добавлять счет участников
score = []

# Выводим имя участников и их счет. Счет добавляем в score
name_1 = (input("Имя первого участника: ")).title()
points_1 = int(input("Счет первого участника: "))
score.append(points_1)

name_2 = (input("Имя второго участника: ")).title()
points_2 = int(input("Счет второго участника: "))
score.append(points_2)

name_3 = (input("Имя третьего участника: ")).title()
points_3 = int(input("Счет третьего участника: "))
score.append(points_3)

# Если счет игрока максимальный в score, выводим соотв. поздарвление
if points_1 == max(score):
    print(f"Поздравляю {name_1}! Вы победили. Ваш счет:{points_1}")
elif points_2 == max(score):
    print(f"Поздравляю {name_2}! Вы победили. Ваш счет:{points_2}")
else:
    print(f"Поздравляю {name_3}! Вы победили. Ваш счет:{points_3}")
