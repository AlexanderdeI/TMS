import turtle
import random as r

t = turtle.Turtle()
t.penup()
t.goto(0, 50)
# Устанавливаем шаг, угол, переменную для подсчета шагов
step = 1
n_steps = 0

while (abs(t.xcor()) < turtle.window_width() // 2 and
        abs(t.ycor()) < turtle.window_height() // 2):
        # Цикл рисует половину окружности
        while n_steps < 180:
                t.speed(10)
                t.pendown()
                t.forward(step)
                n_steps += 1
                t.right(1)
        # Увеличиваем шаг, обнуляем количесвто шагов, запускаем цикл еще
        step += 0.2
        n_steps = 0
