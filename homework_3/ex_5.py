import turtle
import random  as r

turtle.bgcolor("blue")
t = turtle.Turtle()
t.fillcolor("green")
t.shape('turtle')
w_width = turtle.window_width()
h_hight = turtle.window_height()
step = 10
angle_min = 0
angle_max = 360 


while (t.xcor() < (w_width // 2) and
       t.xcor() > (w_width // -2) and
       t.ycor() < (h_hight // 2) and
       t.ycor() > (h_hight // -2)):
           t.xcor()
           t.ycor()
           t.penup()
           angle = r.randint(angle_min, angle_max)
           t.right(angle)
           t.fd(step)
           t.xcor()
           t.ycor()
           print(f'{t.xcor()} | {t.ycor()}')
           
