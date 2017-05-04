import datetime as d

"# Ввожим исходные данные"
inp_year = int(input('Year: '))
inp_month = int(input('Month: '))
inp_day = int(input('Day: '))

"# Определяем дату"
t1 = d.datetime(year=inp_year, month=inp_month, day=inp_day)

"# Создаем объект разницы дат в 1 день"
t2 = d.timedelta(days=1)

"# Добавляем разницу в дате"
t3 = t1 + t2

"# Выводим число следущего дня"
print(t3.day)
