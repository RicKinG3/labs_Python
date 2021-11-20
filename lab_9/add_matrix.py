# -*- coding: utf-8 -*-

from check import *


# функция для фомирования кваадратной матрицы
def add_matrix_square():
    ni = checker(input("Введите размерность матрицы: "))
    ni = int(ni)
    if ni == 0:  # Если кол-во строк или столбцов = 0 выводим ошибку и возвращаем в начало
        add_matrix_square()
    else:
        arr = [ ]
        for i in range(ni):  # Вводим строку
            arr_new = input(f'Введите строку №{i + 1} через пробел: ').split()
            while len(arr_new) != ni:  # Пока длина строки не равна кол-ву столбцов
                print('Длина строки не соответсвует порядку матрицы')
                arr_new = input(f'Введите строку №{i + 1} через пробел: ').split()
            arr.append(arr_new)
        # for k in range(len(arr)):
        #     for h in range(len(arr[k])):
        #         if check_num_float(arr[k][h]):
        #             arr[k][h] = float(arr[k][h])
        #         else:
        #             print('Вы ввели не численую матрицу, введите заново')
        #             arr.clear()
        #             arr = add_matrix_square()
        print(arr)
        return arr


# Функция вывода матрицы
def matrix_print(a):
    print('\n')
    print("Ваша матрица:")
    for i in range(len(a)):
        for j in range(len(a[i])):
            print("{:<10g}".format(a[i][j]), end=' ')
        print()
def matrix_print_f(a):
    print('\n')
    print("Ваша матрица:")
    for i in range(len(a)):
        for j in range(len(a[i])):
            print("{:<10}".format(a[i][j]), end=' ')
        print()