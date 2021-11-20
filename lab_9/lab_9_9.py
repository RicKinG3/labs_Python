# -*- coding: utf-8 -*-
# 9. Ввести трёхмерный массив (массив матриц размера X*Y*Z), вывести из него i-й
# срез по второму индексу.
#
# Выполнил Вольняга Максим ИУ7-16Б
#

from check import *  # импортирую свой модуль для проверки на целочисленность и натуральность

# ВВод размерности 3-х мерного массива
X = checker(input('Введите размерность X: '))
Y = checker(input('Введите размерность Y: '))
Z = checker(input('Введите размерность Z: '))
I = checker(input('Введите i: '))
I = int(I)
X = int(X)
Y = int(Y)
Z = int(Z)
arr = [[[input('el ') for i in range(X)] for j in range(Z)] for k in range(Y)]


# Функция для повторного ввода   3-х мерного массива
def inp(X, Y, Z, arr, I):
    X = checker(input('Введите размерность X: '))
    Y = checker(input('Введите размерность Y: '))
    Z = checker(input('Введите размерность Z: '))
    X = int(X)
    Y = int(Y)
    Z = int(Z)
    I = int(I)

    arr = [[[input('el ') for i in range(X)] for j in range(Y)] for k in range(Z)]
    checkry(arr, X, Y, Z, I)
    return X, Y, Z, arr, I

cp = [ ]

def checkry(arr, X, Y, Z, I):
    # Проверка на нулевые значения размерности 3-х мерного массива
    if (X or Y or Z) == 0:
        print('Вы ввели нулевую размерность масива, введиите ее заново')
        inp(X, Y, Z, arr, I)
    if I < Y:
        for k in range(Y):
            cp.append(arr[k][I])

    else:
        print('размерность 3-х мерного массива не позволяет сделать разрез по второму индексу i')
        print('Введите массив заново ')
        inp(X, Y, Z, arr, I)
    return arr, X, Y, Z, I


checkry(arr, X, Y, Z, I)
print(arr)
print(cp)