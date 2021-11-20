# -*- coding: utf-8 -*-

# 2. Найти максимальное значение над главной диагональю и минимальное - под
# побочной диагональю.
#
# Выполнил: Вольняга Максим ИУ7-16Б
#
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
max_val = 0
# максимальное значение над главной диагональю


min_val = 0
if len(a) == 0:
    a = add_matrix_square()
if len(a)==1:
    min_val = a[0][0]
    max_val = a[0][0]
else:
    min_val = a[1][len(a)-1]   # минимальное значение под побочной диагональю
    max_val = a[0][1]

for i in range(len(a)):
    for j in range(len(a[i])):
        # Если индекс строки i > j индекса столбца => выбираем эл, которые выше главной диагонали
        if j > i:
            # Ищем максимум
            if a[i][j] > max_val:
                max_val = a[i][j]

        if i > (len(a) - j - 1):
            # Ищем минимум
            if min_val > a[i][j]:
                min_val = a[i][j]


print('максимальное значение над главной диагональю = ', max_val)
print('минимальное значение под побочной диагональю = ', min_val)
matrix_print(a)
