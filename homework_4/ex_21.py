# -*- coding: utf-8 -*-
import tkinter
from random import randint

step = 20
speed = 300
speed_level = 7
speed_step = 25
width, height = 640, 480
x_coef = int(width / step) - 1
y_coef = int(height / step) - 1

border = int(step / 10)
sneak_body = [(12, 16), (12, 17), (12, 18)]
x_a, y_a = 1, 0
x_head, y_head = sneak_body[0]
pressed = False
apple = (randint(0, x_coef), randint(0, y_coef))

master = tkinter.Tk()
canvas = tkinter.Canvas(width=width, height=height, background='black')
canvas.grid()
score = 0


def convert(x, y):
    x, y = x * step, y * step
    return x, y, x + step, y + step


def update(x_start, y_start, x_end, y_end):
    x_start, y_start = x_start + border, y_start + border
    x_end, y_end = x_end - border, y_end - border
    return x_start, y_start, x_end, y_end


def pixel(x, y, fill_color='green'):
    coordinates = convert(x, y)
    for color in ['white', fill_color]:
        canvas.create_rectangle(*coordinates, fill=color)
        coordinates = update(*coordinates)


# Смерть
def death():
    for x, y in sneak_body[1:]:
        if (x_head, y_head) == (x, y):
            print('GAME OVER!!!')
            exit()


# Счет
def score_plus():
    global score
    but_score.pack_forget()
    but_score['text'] = f"Счет: {score}"
    but_score.grid()


# Движение через границы экрана
def move_forever():
    global x_head, y_head, width, height, step
    if x_head >= int(width / step):
        x_head = 0
    elif x_head <= -1:
        x_head = int(width / step)
    if y_head >= int(height / step):
        y_head = -1
    elif y_head <= -1:
        y_head = int(height / step)


def game():
    global x_head, y_head, pressed, apple, speed, score, speed_range, speed_level
    pressed = False
    canvas.delete('all')
    move_forever()
    death()
    x_head += x_a
    y_head += y_a
    if (x_head, y_head) == apple:
        apple = (randint(0, x_coef), randint(0, y_coef))
        if apple in sneak_body:
            while apple in sneak_body:
                apple = (randint(0, x_coef), randint(0, y_coef))                
        score += 1
        score_plus()
    else:
        sneak_body.pop()

    if len(sneak_body) >= speed_level:
        speed -= speed_step
        speed_level += 5

    sneak_body.insert(0, (x_head, y_head))
    for x, y in sneak_body:
        pixel(x, y)
    pixel(*apple, fill_color='red')

    master.after(speed, game)


def move_up():
    global y_a, x_a
    if y_a != 1:
        y_a = -1
        x_a = 0


def move_down():
    global y_a, x_a
    if y_a != -1:
        y_a = 1
        x_a = 0


def move_left():
    global y_a, x_a
    if x_a != 1:
        x_a = -1
        y_a = 0


def move_right():
    global y_a, x_a
    if x_a != -1:
        x_a = 1
        y_a = 0

movement = {
    'Up': move_up, 'Down': move_down,
    'Left': move_left, 'Right': move_right
    }


def move(event):
    global pressed
    if not pressed:
        pressed = True
        movement[event.keysym]()


master.bind('<Up>', move)
master.bind('<Down>', move)
master.bind('<Left>', move)
master.bind('<Right>', move)


# Запустить игру
def button_game():
    game()


# Выйти
def button_exit():
    global master
    master.quit()

Butt_game = tkinter.Button(
    master, text=u"Начать игру", width=90, height=1,
    bg='black', fg='white', font="Arial 9", command=button_game
    )
Butt_game.grid(row=11, column=0)


Butt_exit = tkinter.Button(
    master, text=u"Выйти", width=90, height=1,
    bg='black', fg='white', font="Arial 9", command=button_exit
    )
Butt_exit.grid(row=12, column=0)


but_score = tkinter.Button(
    master, text=f"Счет: {score}", width=90, height=1,
    bg='black', fg='white', font="Arial 9", command=score_plus
    )
but_score.grid(row=10, column=0)

master.mainloop()
