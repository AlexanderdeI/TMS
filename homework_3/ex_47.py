import turtle
import time
from datetime import datetime

# Чертим круг
t = turtle.Turtle()
t.shape("circle")
t.penup()
t.goto(0, - 200)
t.pendown()
t.circle(200)
t.penup()
t.home()
t.speed(10)

# Чертим отметки часов
for _ in range(12):
	angle = 30
	t.penup()
	t.fd(170)
	t.pendown()
	t.fd(30)
	t.penup()
	t.goto(0, 0)
	t.right(angle)

# Чертим 5 минутные отметки 
for _ in range(60):
	angle = 6
	t.penup()
	t.fd(190)
	t.pendown()
	t.fd(10)
	t.penup()
	t.goto(0, 0)
	t.right(angle)

# Создаем отдельную черепашку для каждой стрелки
t_sec = turtle.Turtle()
t_min = turtle.Turtle()
t_hour = turtle.Turtle()

# Настраиваем отображение
t_sec.fillcolor("red")
t_min.fillcolor("brown")
t_hour.fillcolor("black")
t_sec.speed(10)
t_min.pensize(width=3)
t_min.hideturtle()
t_min.speed(10)
t_hour.pensize(width=6)
t_hour.hideturtle()
t_hour.speed(10)

# В цикле стрелки поворачиваются на угол, который высчитывается
# с учетом текущего времени (datetime.now().*). Часы показывают
# реальное время. 
while True:
	t_sec.clear()
	t_sec.hideturtle()
	t_sec.home()
	t_sec.right((6 * datetime.now().second) - 90)
	t_sec.penup()
	t_sec.fd(180)
	t_sec.showturtle()
	
	t_min.clear()
	t_min.home()
	t_min.right((6 * datetime.now().minute + datetime.now().second * 0.1) - 90)
	t_min.fd(170)
	
	t_hour.clear()
	t_hour.home()
	t_hour.right((30 * abs(datetime.now().hour - 12) + datetime.now().minute * 0.5)-90)
	t_hour.fd(150)
	time.sleep(0.5)
