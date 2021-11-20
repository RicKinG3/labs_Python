# -*- coding: utf-8 -*-

# 4. Поворот квадратной матрицы на 90 градусов по часовой стрелке, затем на 90
# градусов против часовой стрелки. Вывести промежуточную и итоговую матрицу.
from check import *


def add_matrix_square():
    ni = checker(input("Введите размерность матрицы: "))
    ni = int(ni)
    if ni == 0:  # Если кол-во строк или столбцов = 0 выводим ошибку и возвращаем в начало
        print('Вы ввели нулевую матрицу, введите заново')
        return add_matrix_square()
    else:
        arr = []
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


a1 = []
a2 = []
a = add_matrix_square()
matrix_print(a)
print('\n')

print('Поворот квадратной матрицы на 90 градусов по часовой стрелке')
for i in range(len(a)):
    a1.append([])
    for j in range(len(a)):
        a1[i].append(a[- j - 1][i])
    # print("{:<10}".format(a[- j - 1][i]), end=' ')
for i in a1:
    for j in i:
        print("{:<10}".format(j), end=' ')
    print()
print('\n')
print('Поворот квадратной матрицы на 90 градусов против часовой стрелке')
for i in range(len(a)):
    a2.append([])
    for j in range(len(a)):
        a2[i].append(a1[j][- i - 1])
    # print("{:<10}".format(a[j][- i - 1]), end=' ')
for i in a2:
    for j in i:
        print("{:<10}".format(j), end=' ')
    print()
