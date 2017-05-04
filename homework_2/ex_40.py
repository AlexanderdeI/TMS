import datetime as d

"# Вводим дату рождения"
year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

"# Сохраняем дату в date и определяем день недели"
date = d.datetime(year, month, day)
week_day = d.datetime.isoweekday(date)

"# Создаем словарь номер дня: название дня"
days_of_week = {1: "Понедельник", 2: "Вторник", 3: "Среда",
                4: "Пятница", 4: "Четверг",
                6: 'Суббота', 7: "Воскресенье"}

"# Выводим название дня по номеру(ключу)"
if week_day in days_of_week:
    week_day = days_of_week[week_day]
    print(week_day)
else:
    exit()
