'# Вводим стороны треугольника'
a = float(input('Введите длину первой стороны: '))
b = float(input('Введите длину второй стороны: '))
c = float(input('Введите длину третьей стороны: '))

'# Проверяем возможность существования треугольника'
if (a <= b + c and b <= a + c and c <= a + b):
    print("такой треугольник существует")
else:
    print("такой треугольник не существует")
