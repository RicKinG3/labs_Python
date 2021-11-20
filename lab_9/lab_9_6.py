# -*- coding: utf-8 -*-
# 6. Задана матрица D и массив I, содержащий номера строк, для которых
# необходимо определить максимальный элемент. Значения максимальных
# элементов запомнить в массиве R. Определить среднее арифметическое
# вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
# среднее арифметическое значение
from check import *


def matrix_input(arr):
    n = checker(input("Введите кол-во строк D : "))
    m = checker(input("Введите кол-во столбцов D : "))
    n = int(n)
    m = int(m)
    if n == 0 or m == 0:  # Если кол-во строк или столбцов = 0 выводим ошибку и возвращаем в начало
        print('Вы ввели нулевые значения')
        return arr
    arr.clear()
    for i in range(n):  # Вводим строку
        arr_new = list(map(str, input(f'Введите строку D №{i + 1} через пробел: ').split()))
        while len(arr_new) != m:  # Пока длина строки не равна кол-ву столбцов
            print('Длина строки не соответсвует порядку матрицы')
            arr_new = list(map(str, input(f'Введите строку D №{i + 1} через пробел: ').split()))
        arr.append(arr_new)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if check_num_float(arr[i][j]):

                arr[i][j] = float(arr[i][j])
            else:
                print('\n')
                print('Вы ввели не целочисленную матрицу, введите заново')
                return matrix_input(arr)

    return arr


D = []
I = []
D = matrix_input(D)


def I_input(I):
    print('\n')
    print('Матрица  D ')
    f = 0
    for i in range(len(D)):
        f += 1
        for j in range(len(D[i])):
            print("{:<10g}".format(D[i][j]), end=' ')
        print()
    print('\n')
    n = checker(input('Введите кол-во элементов I: '))
    n = int(n)
    if (n > f) or n == 0:
        print('\n')
        print('Кол-во элементов I не соответствуют кол-ву строк матрицы или равно 0, введите заново  ')
        I.clear()
        return I_input(I)
    else:
        for i in range(n):
            print('\n')
            k = checker(input('введите элемент массива I: '))
            k = int(k)
            if k <= f:
                I.append(k)
            else:
                print('\n')
                print(' Элемент I не соответствуют кол-ву строк матрицы, введите заново  ')
                I.clear()
                return I_input(I)
        return I
I = I_input(I)

I = [I[i] for i in range(len(I)) if i == I.index(I[i])]

mi = D[0][0]
Ri = []

for x in D:
    mi = D[0][0]
    for y in x:
        if mi < y:
            mi = y
    Ri.append(mi)
R = []

for i in range(len(I)):
    R.append((Ri[I[i] - 1]))

cp = (sum(R) / len(R))
print('\n')
print('Матрица  D ')
matrix_print(D)
print('\n')
print('Массив I', I)
print('Массив R', R)
print('среднее арифметическое значение = ', cp)
