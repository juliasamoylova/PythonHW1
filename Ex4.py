# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
Quater = int(input('Введите номер четверти (от 1 до 4): '))

if Quater == 1:
    print('Первая четверть: X > 0 and Y > 0')
if Quater == 2:
    print('Вторая четверть: X > 0 and Y < 0')
if Quater == 3:
    print('Третья четверть: X < 0 and Y < 0')
if Quater == 4:
    print('Четвертая четверть: X < 0 and Y > 0')
if Quater < 1 or Quater > 4:
    print('Номер четверти введен не верно')
