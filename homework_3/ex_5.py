import turtle
import random as r

t = turtle.Turtle()
# Настраиваем отображение
t.fillcolor("green")
turtle.bgcolor("blue")
t.shape('turtle')
# Задаем шаг и диапозон возможных направлений
step = 100

# Если координаты превышают размер экрана, цикл прекращается
while (abs(t.xcor()) < turtle.window_width() // 2 and
        abs(t.ycor()) < turtle.window_height() // 2):
            t.xcor(), t.ycor()
            t.penup()
            angle = r.randint(0, 360)
            t.right(angle)
            t.fd(step)
else:
	exit
