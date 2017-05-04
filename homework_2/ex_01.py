import math

'# Определяем радиус окружности с центром в точке (20;20)'
radius = 10

'# Вводим координаты в формате float'
x_inp = float(input('Coord X: '))
y_inp = float(input('Coord Y: '))

'# Вычисляем гипотенузу треугольника с катетами X и Y'
gipot = math.sqrt(x_inp**2 + y_inp**2)


'''# Определяем попадают ли координаты
     в диапозон значаний координат круга.
     Если попадают и  гипотенуза меньше
     или равна радиусу - точка в круге'''
if (10 <= x_inp <= 30 and
    10 <= y_inp <= 30 and
    gipot <= radius + 20):
    print('Point is within the circle')
else:
    print('Point is outside the circle')

'''# Определяем попадает ли точка в
     квадрат с верхней левой координатой
          в точке (-5, 10) и длинной 8'''
if (-5 <= x_inp <= 3 and
    2 <= y_inp <= 10):
    print('Point is within the square')
else:
    print('Point is outside the square')
