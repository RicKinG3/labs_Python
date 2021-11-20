# -*- coding: utf-8 -*-
# 8. Сформировать матрицу C путём построчного перемножения матриц A и B
# одинаковой размерности (элементы в i-й строке матрицы A умножаются на
# соответствующие элементы в i-й строке матрицы B), потом сложить все
# элементы в столбцах матрицы C и записать их в массив V.
from check import *


def matrix_input(arr):
    n = checker(input("Введите кол-во строк A : "))
    m = checker(input("Введите кол-во столбцов A : "))
    n = int(n)
    m = int(m)
    if n == 0 or m == 0:  # Если кол-во строк или столбцов = 0 выводим ошибку и возвращаем в начало
        print('Вы ввели нулевые значения')
        return matrix_input(arr)
    arr.clear()
    for i in range(n):  # Вводим строку
        arr_new = list(map(str, input(f'Введите строку A №{i + 1} через пробел: ').split()))
        while len(arr_new) != m:  # Пока длина строки не равна кол-ву столбцов
            print('Длина строки не соответсвует порядку матрицы')
            arr_new = list(map(str, input(f'Введите строку A №{i + 1} через пробел: ').split()))
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


A = []
B = []
h = 0
A = matrix_input(A)

for i in range(len(B)):
    for j in range(len(B[i])):
        h += 1
def matrix_input1(arr):
    n = checker(input("Введите кол-во строк B : "))
    m = checker(input("Введите кол-во столбцов B : "))
    n = int(n)
    m = int(m)
    if n == 0 or m == 0:  # Если кол-во строк или столбцов = 0 выводим ошибку и возвращаем в начало
        print('Вы ввели нулевые значения')
        return matrix_input1(arr)
    arr.clear()
    for i in range(n):  # Вводим строку
        arr_new = list(map(str, input(f'Введите строку B №{i + 1} через пробел: ').split()))
        while len(arr_new) != m:  # Пока длина строки не равна кол-ву столбцов
            print('Длина строки не соответсвует порядку матрицы')
            arr_new = list(map(str, input(f'Введите строку B №{i + 1} через пробел: ').split()))
        arr.append(arr_new)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if check_num_float(arr[i][j]):

                arr[i][j] = float(arr[i][j])
            else:
                print('\n')
                print('Вы ввели не целочисленную матрицу, введите заново')
                return matrix_input1(arr)
    return arr

f = 0
B = matrix_input1(B)
for i in range(len(B)):
    for j in range(len(B[i])):
        f += 1

if len(A)!=len(B) and f!=h:
    print('Вы ввели разномерные матрицы А и В')
    A = matrix_input(A)
    B = matrix_input1(B)

k = int(f/len(B))
C = [ ]
print(len(B))
for i in range(len(B)):
    C.append([0]*k)
for i in range(len(B)):
    for j in range(len(B[i])):
        C[i][j] = float(A[i][j]*B[i][j])

V = []  # Список хранящий суммы столбцов С
for x in range(len(C[0])):
    s = 0
    for j in range(len(C)):
        s += C[j][x]

    V.append(s)
print('Матрица А ')
matrix_print(A)
print('\n')
print('Матрица В ')
matrix_print(B)
print('\n')
print('Матрица С ')
matrix_print(C)
print('\n')
print('Массив V ')
for i in range(len(V)):
    print("{:<10g}".format(V[i]), end=' ')
