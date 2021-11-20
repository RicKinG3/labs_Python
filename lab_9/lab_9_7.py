# -*- coding: utf-8 -*-
# 7. Дана матрица символов. Заменить в ней все гласные английские буквы на
# точки.
from check import *


def matrix_input(arr):
    n = checker(input("Введите кол-во строк  : "))
    m = checker(input("Введите кол-во столбцов : "))
    n = int(n)
    m = int(m)
    if n == 0 or m == 0:  # Если кол-во строк или столбцов = 0 выводим ошибку и возвращаем в начало
        print('Вы ввели нулевые значения')
        return arr
    arr.clear()
    for i in range(n):  # Вводим строку
        arr_new = list(map(str, input(f'Введите строку №{i + 1} через пробел: ').split()))
        while len(arr_new) != m:  # Пока длина строки не равна кол-ву столбцов
            print('Длина строки не соответсвует порядку матрицы')
            arr_new = list(map(str, input(f'Введите строку  №{i + 1} через пробел: ').split()))
        arr.append(arr_new)
    return arr


D = []
D = matrix_input(D)
matrix_print_f(D)
for i in range(len(D)):
    l = 0
    p = 0
    for j in range(len(D[i])):
        s = ''
        for k in D[i][j]:
            if k in "aeuioAEYUIO":
                s += '.'
            else:
                s += k
        D[i][j] = s
matrix_print_f(D)
