import datetime as d

# Вводим дату рождения
year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

# Сохраняем дату в date и определяем день недели
date = d.datetime(year, month, day)
week_day = d.datetime.isoweekday(date)

# Создаем словарь номер дня: название дня
days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг",
                "Пятница", 'Суббота', "Воскресенье"]

# Выводим название дня по номеру(ключу)
if 0 < week_day <= 7:
    week_day = days_of_week[(week_day - 1)]
    print(week_day)
else:
    exit()
