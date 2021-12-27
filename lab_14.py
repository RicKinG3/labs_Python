# -*- coding: utf-8 -*-

# Написать программу для демонстрации работы метода сортировки пузырек с флагом на
# примере массива целых чисел.
# Программа должна состоять из двух частей и выполнять два действия
# последовательно: сначала отсортировать заданный пользователем массив, затем
# составить таблицу замеров времени сортировки списков трёх различных (заданных
# пользователем) размерностей. Для каждой размерности списка необходимо
# исследовать:
# ● случайный список,
# ● отсортированный список,
# ● список, отсортированный в обратном порядке.
#
# Выполнил Вольняга Максим ИУ7-16Б
#


from check import *
from random import randint
import timeit

N0 = checker(input("Введите размерность массива для ввода: "))
N0 = int(N0)
N1 = checker(input("Введите размерность массива для N1: "))
N1 = int(N1)
N2 = checker(input("Введите размерность массива для N2: "))
N2 = int(N2)
N3 = checker(input("Введите размерность массива для N3: "))
N3 = int(N3)
arr_input = []

while N0 == 0:
    print("Вы ввели нулевые значения, пожалуйста введите заново")
    N0 = checker(input("Введите размерность массива для ввода: "))
    N0 = int(N0)

while N1 == 0 or N2 == 0 or N3 == 0:
    print("Вы ввели нулевые значения, пожалуйста введите заново")
    N1 = checker(input("Введите размерность массива для N1: "))
    N1 = int(N1)
    N2 = checker(input("Введите размерность массива для N2: "))
    N2 = int(N2)
    N3 = checker(input("Введите размерность массива для N3: "))
    N3 = int(N3)


def bubble_sort_with_flag(arr):
    n = len(arr)
    for i in range(n - 1):
        flag = True
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        if flag:
            break
    return arr


def input_mas():
    for i in range(N0):
        elem = input(f"Введите {i + 1} элемент: ")
        if matrix_check(elem):
            arr_input.append(elem)
        else:
            print("Вы ввели стоку или  вещественное число, в массив этот элемент не записался")
    return arr_input


arr_input = input_mas()
if len(arr_input) == 0:
    print("Массив заполненый пользователем = 0")
    print("Заполните массив заново")
    arr_input = input_mas()

arr = [randint(1, 10000) for i in range(N1)]
arr_1 = [randint(1, 10000) for i in range(N2)]
arr_2 = [randint(1, 10000) for i in range(N3)]

print("Ваш массив до сортировки: ")
print(*arr_input)
print("\nВаш массив до сортировки: ")
arr_input_sorted = bubble_sort_with_flag(arr_input)
print(*arr_input_sorted)

time_arr = timeit.timeit('bubble_sort_with_flag(arr)', globals=globals(), number=10000)
time_arr_1 = timeit.timeit('bubble_sort_with_flag(arr_1)', globals=globals(), number=10000)
time_arr_2 = timeit.timeit('bubble_sort_with_flag(arr_2)', globals=globals(), number=10000)

arr_sorted = bubble_sort_with_flag(arr)
arr_sorted_1 = bubble_sort_with_flag(arr_1)
arr_sorted_2 = bubble_sort_with_flag(arr_2)


time_arr_sorted = timeit.timeit('bubble_sort_with_flag(arr_sorted)', globals=globals(), number=10000)
time_arr_sorted_1 = timeit.timeit('bubble_sort_with_flag(arr_sorted_1)', globals=globals(), number=10000)
time_arr_sorted_2 = timeit.timeit('bubble_sort_with_flag(arr_sorted_2)', globals=globals(), number=10000)

arr_rever = sorted(arr_sorted, reverse=True)
arr_rever_1 = sorted(arr_sorted_1, reverse=True)
arr_rever_2 = sorted(arr_sorted_2, reverse=True)


time_arr_revers = timeit.timeit('bubble_sort_with_flag(arr_rever)', globals=globals(), number=10000)
time_arr_revers_1 = timeit.timeit('bubble_sort_with_flag(arr_rever_1)', globals=globals(), number=10000)
time_arr_revers_2 = timeit.timeit('bubble_sort_with_flag(arr_rever_2)', globals=globals(), number=10000)

# Табличка
print('\nN1, N2, N3:                         |', '{}'.format(N1).center(20), '|', '{}'.format(N2).center(20), '|',
      '{}'.format(N3).center(20) + '\n' + '-' * 100)
print('Упорядоченный список:               |', '{:^20.4f}'.format(time_arr_sorted), '|',
      '{:^20.4f}'.format(time_arr_sorted_1),
      '|', '{:^20.4f}'.format(time_arr_sorted_2))
print('Случайный список :                  |', '{:^20.4f}'.format(time_arr), '|', '{:^20.4f}'.format(time_arr_1), '|',
      '{:^20.4f}'.format(time_arr_2))
print('Упорядоченный в обратном порядке :  |', '{:^20.4f}'.format(time_arr_revers), '|',
      '{:^20.4f}'.format(time_arr_revers_1), '|',
      '{:^20.4f}'.format(time_arr_revers_2))
