import calendar as c

"# Вводим год и отчищаем ввод"
year = input('Enter the year: ')
year = year.split()
year = ''.join(year)

"# Вводим месяц и отчищаем ввод"
month = input('Enter the month: ')
month = month.lower().split()
month = ''.join(month)

"# Словарь название месяца:номер месяца "
dict_month = {'january': 1, 'february': 2, 'march': 3,
              'april': 4, 'may': 5, 'june': 6,
              'july': 7, 'august': 8, 'september': 9,
              'october': 10, 'november': 11, 'december': 12}

"# Присваиваем номер, если строка в словаре"
if (month.isalpha and month in dict_month):
    month = dict_month[month]

"# Определяем количество дней"
num_days = c.monthrange(int(year), int(month))

"# Выводим количество дней"
print(num_days[-1])
