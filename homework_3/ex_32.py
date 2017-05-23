from math import pi, sin, cos
import turtle

t = turtle.Turtle()

# Создаем списки для значений косинуса, синуса и значений по Х
list_siny = []
list_cosy = []
list_x = []
# Определяем размер экрана
size_x = turtle.window_width() // 2 -10
size_y = turtle.window_height() // 2 - 10

# Считаем значение У от -pi до pi 
# Первое значение Х равно крайней левой точке графика
n = -180
x = -size_x

# Высчитываем значения Х, косинуса и синуса,
# добавяем их в соответсвующие списки
while n < 180:
	x += 2 / 360 * size_x
	list_x.append(x)
	y = round((n * pi / 180), 4)
	siny = sin(y) * size_y
	list_siny.append(siny)
	cosy = cos(y) * size_y
	list_cosy.append(cosy)
	n += 1

# Перемещаем черепашку в начальную точку графика
t.penup()	
t.goto(list_x[0], 0)
t.pendown()
t.pencolor("red")

# Чертим график синуса итерируясь по двум спискам
for x, y in zip(list_x, list_siny):
	t.goto(x, y)

# Аналогично для графика косинуса	
t.penup()	
t.goto(list_x[0], list_cosy[0])
t.pendown()
t.pencolor("blue")

for x, y in zip(list_x, list_cosy):
	t.goto(x, y)
	
input()
