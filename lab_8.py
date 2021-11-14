# Написать программу, которая позволит с использованием меню обеспечить работу с
# целочисленными матрицами:
# 1. Ввести матрицу
# 2. Добавить строку
# 3. Удалить строку
# 4. Добавить столбец
# 5. Удалить столбец
# 6. Найти строку, имеющую определённое свойство по варианту
# 7. Переставить местами строки с наибольшим и наименьшим количеством
# отрицательных элементов
# 8. Найти столбец, имеющий Наибольшее количество чисел, являющихся степенями 2
# 9. Переставить местами столбцы с максимальной и минимальной суммой
# элементов
# 10. Вывести текущую матрицу
##
##
# Выполнил работу Вольняга Максим ИУ7-16Б
##

# Импортирую свой модуль для проверки целого натурального числа и проверки целого чиссла
from check import checker, matrix_check

arr = []


# Функция  ввода матрицы
def matrix_input(arr):
    n = checker(input("Введите кол-во строк: "))
    m = checker(input("Введите кол-во столбцов: "))
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
            arr_new = list(map(str, input(f'Введите строку №{i + 1} через пробел: ').split()))
        arr.append(arr_new)
    return arr


# Функция вывода матрицы
def matrix_print(arr):
    print('\n')
    print("Ваша матрица:")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print("{:^10d}".format(arr[i][j]), end=' ')
        print()


# Функция удаления строки
def del_string(arr, num):
    index = checker(input('Введите индекс удаляемой строки: '))
    index = int(index)
    if 0 <= index < len(arr):  # Проверка на некорректный индекс
        if num == 1:  # Алгоритмический способ
            for i in range(index, len(arr) - 1):  # Перебираем от индекса до предпоследней строки
                arr[i] = arr[i + 1]  # Перемещаем строку которую выбрали в конец
            del arr[-1]  # Удаляем последний
            return arr
        # метод питона
        elif num == 2:
            del arr[index]
            return arr
    else:
        print('Вы ввели не коректный индекс')


# Удаление столбца
def del_column(arr, num):
    index = checker(input('Введите индекс удаляемого столбца: '))
    index = int(index)
    if 0 <= index < len(arr):  # Проверка на некорректный индекс
        # Алгоритмический способ
        if num == 1:
            for i in range(len(arr)):
                for j in range(index, len(arr[0]) - 1):  # перебираем от индекса до предпоследнего элемента строки
                    arr[i][j] = arr[i][j + 1]  # Перемещаем нужный эл столбца в конец строки
                del arr[i][-1]  # Удаляем  последний элемент
            return arr
        # Метод питона
        elif num == 2:
            for i in range(len(arr)):
                del arr[i][index]
            return arr
    else:
        print('Вы ввели некоректный индекс')


# Функция проверки степеней двойки черрез бинарные операции
def check2rec(num):
    if num == 1:
        return True
    # Битовая операция И
    if num & 1:
        return False
    return check2rec(num >> 1)  # Сдвигаем вправо каждый бит на 1 поз вправо


# Функция меню
def menu():
    print('Меню команд:')
    print('0 - Выйти из программы')
    print('1 - Ввести матрицу')
    print('2 - Добавить строку')
    print('3 - Удалить строку')
    print('4 - Добавить столбец')
    print('5 - Удалить столбец')
    print('6 - Найти строку, имеющую Наибольшее среднее арифметическое')
    print('7 - Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов')
    print('8 - Найти столбец, имеющий Наибольшее количество чисел, являющихся степенями 2')
    print('9 - Переставить местами столбцы с максимальной и минимальной суммой элементов')
    print('10 - Вывести текущую матрицу')


counter = 0  # Счетчик введеных команд
# Первая инициализация списка
print('Введите список с клавиатуры')

while True:
    # Ввод матрицы при запуске программы
    if counter == 0:
        arr = matrix_input(arr)  # Проверка на целочисленность матрицы
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if matrix_check(arr[i][j]):
                    arr[i][j] = int(arr[i][j])
                else:
                    print('Вы ввели не целочисленную матрицу, введите заново')
                    arr = matrix_input(arr)
        matrix_print(arr)
    if counter % 3 == 0:  # Вывод меню
        menu()
    counter += 1
    command = (checker(input("Введите номер меню: ")))
    command = int(command)

    if 0 <= command <= 10:

        # Выход из программы
        if command == 0:
            exit("Программа завершила работу")
        # Ввод матрицы
        elif command == 1:
            arr = matrix_input(arr)
            for i in range(len(arr)):  # Провека на целочисленность матрицы
                for j in range(len(arr[i])):
                    if matrix_check(arr[i][j]):
                        arr[i][j] = int(arr[i][j])
                    else:
                        print('Вы ввели не целочисленную матрицу, введите заново')
                        arr = matrix_input(arr)
            matrix_print(arr)
        # Добавление строки
        elif command == 2:
            while True:
                index_2 = checker(input("Введите индекс вставки строки: "))
                index_2 = int(index_2)
                if index_2 > len(arr):  # Если индекс больше длины ставим элемент в последнюю позицию
                    index_2 = len(arr)
                else:
                    row_new = input("Введите строку матрицы: ")
                    if all(map(matrix_check, row_new.split())):  # Проверка новой строки на целочисленность
                        if arr and len(row_new.split()) == len(arr[0]):  # Провека длины строки
                            cur_row = list(map(int, row_new.split()))  # Текующая строка, которую нужно вставить
                            print('1 - Алгоритмическая реализация')
                            print('2 - Реализация средствами языка')
                            num = checker(input('>>> '))
                            if num == '1':
                                arr.append(cur_row)
                                for i in range(len(arr) - 1, index_2, -1):  # Перебираем от пердпоследнего эл до индекса
                                    arr[i], arr[i - 1] = arr[i - 1], arr[i]  # Свапаем
                            # Метод питона
                            elif num == '2':
                                arr.insert(index_2, cur_row)
                            matrix_print(arr)
                            break
                        else:
                            print("Длина строки не соответсвует порядку матрицы")
                    else:
                        print("Вы ввели не целый элемент в строку")
        # Удаление строки
        elif command == 3:
            print('1 - Алгоритмическая реализация')
            print('2 - Реализация средствами языка')
            num = checker(input('>>> '))
            num = int(num)
            if 0 < num <= 2:
                del_string(arr, num)
                matrix_print(arr)

        # Добавление столбца
        elif command == 4:
            while True:
                index_4 = checker(input("Введите индекс вставки столбца: "))
                index_4 = int(index_4)
                if arr:  # Если индекс вставки больше длины вставляем столбец в конец
                    if index_4 > len(arr[0]):
                        index_4 = len(arr[0])
                if index_4 < 0:
                    print("Введите положительное число: ")
                else:
                    col_new = input("Введите столбец матрицы: ")
                    if all(map(matrix_check, col_new.split())):  # Проверка нового столбца на целочисленность
                        if arr and len(col_new.split()) == len(arr):  # Провека длины столбца
                            cur_col = list(map(int, col_new.split()))  # Столбец который прошел
                            # проверки и его необходимо вставить
                            if arr:
                                print('1 - Алгоритмическая реализация')
                                print('2 - Реализация средствами языка')
                                num = checker(input('>>> '))
                                if num == '1':
                                    for i in range(len(cur_col)):
                                        # В каждую строку вставляем соответствующий элемент из столбца
                                        arr[i].append(cur_col[i])
                                        # Перемещаем его на нужную позицию от последнего до индекса
                                        for j in range(len(arr[i]) - 1, index_4, -1):
                                            arr[i][j], arr[i][j - 1] = arr[i][j - 1], arr[i][j]  # swap
                                # Метод питона
                                elif num == '2':
                                    for i in range(len(cur_col)):
                                        arr[i].insert(index_4, cur_col[i])
                                else:
                                    print("Выбран не верный режим")
                            matrix_print(arr)
                            break
                        else:
                            print("Длина толбца не соответсвует порядку матрицы")
                    else:
                        print("Вы ввели не целый элемент в столбец")
        # Удаление столбца
        elif command == 5:
            print('1 - Алгоритмическая реализация')
            print('2 - Реализация средствами языка')
            num = checker(input('>>> '))
            num = int(num)
            if 0 < num <= 2:
                del_column(arr, num)
                matrix_print(arr)
            else:
                print('Вы ввели не верный вариант')
        # Поиска строки с максимальным средне арифметическим
        elif command == 6:
            arith_mean = []  # Список хранит среднее арифметическое всех строк
            for x in arr:
                summa = 0
                for j in x:
                    summa += j
                arith_mean.append(summa / len(arr[0]))
            print("\n\n")
            print("Строка {0}, имеет наибольшее среднее арифметическое {1:.6g}".format(
                arr[arith_mean.index(max(arith_mean))],
                max(arith_mean)))
        # Свап строк с максимальным и минимальным количеством отриц. элементов
        elif command == 7:
            neg = []  # Список хранящий количество отрицательных элементов в каждой строке
            for x in arr:
                neg_count = 0
                for j in x:
                    if j < 0:
                        neg_count += 1
                neg.append(neg_count)
            # Cвап  строк
            arr[neg.index(min(neg))], arr[neg.index(max(neg))] = arr[neg.index(max(neg))], arr[neg.index(min(neg))]
            matrix_print(arr)
        # 8 - Найти столбец, имеющий Наибольшее количество чисел, являющихся степенями 2
        elif command == 8:
            maxi_degrees = []  # Список хранящий количество степеней двойки в каждом столбце
            print(len(arr[0]))
            for x in range(len(arr[0])):
                count = 0
                for j in range(len(arr)):
                    if check2rec(arr[j][x]):
                        count += 1

                maxi_degrees.append(count)
            if sum(maxi_degrees) == 0:
                print("матрица не имеет степений 2-ки")
                print('Введите 1 если хотите ввести ')
                arr = matrix_input(arr)


            nes_col = []  # Список хранящий столбец с максимальным количеством степеней 2
            for x in arr:
                nes_col.append(x[maxi_degrees.index(max(maxi_degrees))])
            print("Столбец {0}, имеет наибольшее количество степеней двойки {1}".format(nes_col, max(maxi_degrees)))
        # 9. Переставить местами столбцы с максимальной и минимальной суммой
        elif command == 9:
            summ = []  # Список хранящий сумму всех столбцов
            for x in range(len(arr[0])):
                count = 0
                for j in range(len(arr)):
                    count += arr[j][x]
                summ.append(count)
            for x in arr:
            # Меняем местами столбцы
                x[summ.index(min(summ))], x[summ.index(max(summ))] = x[summ.index(max(summ))], x[summ.index(min(summ))]
            matrix_print(arr)

        # Вывод матрицы
        else:
            matrix_print(arr)
