import datetime as d
import time as t

"# Определяем местные дату и время, и оставляем только время"
user_time = d.datetime.now()
user_time = d.datetime.strftime(user_time, "%H:%M:%S")

"# Определяем Гринвичское и время, и оставляем только время"
utc_time = d.datetime.utcnow()
utc_time = d.datetime.strftime(utc_time, "%H:%M:%S")

"# Находим временную зону"
user_TZ = t.tzname

"# Находим разницу между местным и Гринвечским временем в часах"
delta_user_UTC = (t.timezone) / (-3600)

"# Выводим результат"
print("User time: {0}".format(user_time))
print("UTC time: {0}".format(utc_time))
print("User time zone: {0}".format(user_TZ))
print("Local time - UTC = {0}".format(delta_user_UTC))
