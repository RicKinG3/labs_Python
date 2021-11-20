# -*- coding: utf-8 -*-
# 3. Транспонирование квадратной матрицы.
from check import *


def add_matrix_square():
    ni = checker(input("Введите размерность матрицы: "))
    ni = int(ni)
    if ni == 0:  # Если кол-во строк или столбцов = 0 выводим ошибку и возвращаем в начало
        return add_matrix_square()
    else:
        arr = [ ]
        for i in range(ni):  # Вводим строку
            arr_new = input(f'Введите строку №{i + 1} через пробел: ').split()
            while len(arr_new) != ni:  # Пока длина строки не равна кол-ву столбцов
                print('Длина строки не соответсвует порядку матрицы')
                arr_new = input(f'Введите строку №{i + 1} через пробел: ').split()
            arr.append(arr_new)
        for k in range(len(arr)):
            for h in range(len(arr[k])):
                if check_num_float(arr[k][h]):
                    arr[k][h] = float(arr[k][h])
                else:
                    print('Вы ввели не численую матрицу, введите заново')
                    arr.clear()
                    arr = add_matrix_square()
        return arr
a = add_matrix_square()
matrix_print(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        if j > i:
            a[i][j], a[j][i] = a[j][i], a[i][j]
matrix_print(a)
