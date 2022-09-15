# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# если одно из утверждений верно, значит ложь

from re import X


X = input('Введите X: ')
Y = input('Введите Y: ')
Z = input('Введите Z: ')

A = (not (X or Y or Z))
B = ((not X) and (not Y) and (not Z))
if A == B:
    print('Yes')
else:
    print('no')
