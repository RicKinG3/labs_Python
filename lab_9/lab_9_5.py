# -*- coding: utf-8 -*-
# 5. Подсчитать в каждой строке матрицы D количество элементов, превышающих
# суммы элементов соответствующих строк матрицы Z. Разместить эти
# количества в массиве G, умножить матрицу D на максимальный элемент
# массива G. Напечатать матрицу D до и после преобразования, а также массив G
from check import *

def matrix_input(arr):
    n = checker(input("Введите кол-во строк D : "))
    m = checker(input("Введите кол-во столбцов D : "))
    n = int(n)
    m = int(m)
    arr.clear()
    if n == 0 or m == 0:  # Если кол-во строк или столбцов = 0 выводим ошибку и возвращаем в начало
        print('Вы ввели нулевые значения')
        matrix_input(arr)

    for i in range(n):  # Вводим строку
        arr_new = list(map(str, input(f'Введите строку D №{i + 1} через пробел: ').split()))
        while len(arr_new) != m:  # Пока длина строки не равна кол-ву столбцов
            print('Длина строки не соответсвует порядку матрицы')
            arr_new = list(map(str, input(f'Введите строку D №{i + 1} через пробел: ').split()))
        arr.append(arr_new)
    return arr
D = [ ]
Z = [ ]
D = matrix_input(D)
for i in range(len(D)):
    for j in range(len(D[i])):
        if check_num_float(D[i][j]):
            D[i][j] = float(D[i][j])
        else:
            print('Вы ввели не целочисленную матрицу, введите заново')
            D = matrix_input(D)
def matrix_input1(arr):
    n = checker(input("Введите кол-во строк Z : "))
    m = checker(input("Введите кол-во столбцов Z : "))
    n = int(n)
    m = int(m)
    if n == 0 or m == 0:  # Если кол-во строк или столбцов = 0 выводим ошибку и возвращаем в начало
        print('Вы ввели нулевые значения')
        return arr
    arr.clear()
    for i in range(n):  # Вводим строку
        arr_new = list(map(str, input(f'Введите строку Z №{i + 1} через пробел: ').split()))
        while len(arr_new) != m:  # Пока длина строки не равна кол-ву столбцов
            print('Длина строки не соответсвует порядку матрицы')
            arr_new = list(map(str, input(f'Введите строку Z №{i + 1} через пробел: ').split()))
        arr.append(arr_new)
    return arr

Z = matrix_input1(Z)
for i in range(len(Z)):
    for j in range(len(Z[i])):
        if check_num_float(Z[i][j]):
            Z[i][j] = float(Z[i][j])
        else:
            print('Вы ввели не целочисленную матрицу, введите заново')
            Z = matrix_input1(Z)
print('\n')
print('Матрица  D ')
f = 0
for i in range(len(D)):
    f += 1
    for j in range(len(D[i])):
        print("{:<10g}".format(D[i][j]), end=' ')
    print()
print('\n')
print('Матрица  Z ')
for i in range(len(Z)):
    for j in range(len(Z[i])):
        print("{:<10g}".format(Z[i][j]), end=' ')
    print()


sum_Z= [ ]
G = [ ]
for x in Z:
    summa = 0
    for j in x:
        summa += j
    sum_Z.append(summa)

if len(sum_Z)!=f:
    sum_Z.clear()
    G.clear()
    f = 0
    print('\n')
    print('кол-во строк Z и D должны быть равними, введите заново D и Z')
    D = matrix_input(D)
    for i in range(len(D)):
        for j in range(len(D[i])):
            if check_num_float(D[i][j]):
                D[i][j] = float(D[i][j])
            else:
                print('Вы ввели не целочисленную матрицу, введите заново')
                D = matrix_input(D)
    Z = matrix_input1(Z)
    for i in range(len(Z)):
        for j in range(len(Z[i])):
            if check_num_float(Z[i][j]):
                Z[i][j] = float(Z[i][j])
            else:
                print('Вы ввели не целочисленную матрицу, введите заново')
                Z = matrix_input1(Z)
    print('\n')
    print('Матрица  D ')
    matrix_print(D)
    print('\n')
    print('Матрица  Z ')
    matrix_print(Z)
    for x in Z:
        summa = 0
        for j in x:
            summa += j
        sum_Z.append(summa)

for i in range(len(D)):
    k = 0
    for j in range(len(D[i])):
        if D[i][j]>sum_Z[i]:
            k += 1
    G.append(k)

for i in range(len(D)):
    for j in range(len(D[i])):
        D[i][j] = D[i][j] * max(G)
print('\n')
print('Матрица D теперь')
for i in range(len(D)):
    for j in range(len(D[i])):
        print("{:<10g}".format(D[i][j]), end=' ')
    print()
print('\n')
print('Массив G  ', G)
