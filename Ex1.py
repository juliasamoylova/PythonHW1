# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# if (weekday <= 5 && weekday > 0)
# {
#   Console.WriteLine("Не выходной");
# }
# if (weekday >= 6 && weekday <= 7)
# {
#   Console.WriteLine("Выходной");
# }
# if (weekday < 0)
# {
#    Console.WriteLine("Ошибка");
# }
# if (weekday > 7)
# {
#   Console.WriteLine("Ошибка");

weekday = int(input('Введите число от 1 до 7 включительно: '))
if weekday == 7 or weekday == 6:
    print('Выходной')
if weekday > 7 or weekday <= 0:
    print('Ошибка')
if weekday > 0 and weekday < 6:
    print('Не выходной')
