
# Лабораторная работа №12 “База данных в текстовом файле”
# Требуется написать программу, которая позволит с помощью меню выполнить
# следующие действия:
#
# 1. Выбрать файл для работы
# 2. Инициализировать базу данных
# 3. Вывести содержимое базы данных
# 4. Добавить запись в базу данных
# 5. Поиск по одному полю
# 6. Поиск по двум полям
#
# Вольняга Максим ИУ7-16Б
#
import os.path
from check import *


def isDigit(t):
    if t == '': return False
    if t[0] == '-':
        t = t[1:]
    if t.find('.') != 0:
        t = t.replace('.', '')
    return t.isdigit()


def digit_input(stroke):
    while True:
        n = input(stroke).strip()
        if isDigit(n) == True and float(n) >= 0:
            return int(float(n))
        print('Введенный символ не является числом или является числом не положительным. Повторите ввод')


database = open('lab12.txt', 'w+')
file = None
size = 90
types = ('int', 'str')


# Функция меню
def menu():
    print('Меню команд:')
    print('1 - Выбрать файл для работы')
    print('2 - Инициализировать базу данных')
    print('3 - Вывести содержимое базы данных')
    print('4 - Добавить запись в базу данных')
    print('5 - Поиск по одному полю')
    print('6 - Поиск по двум полям')


#  Меню
while True:
    print()
    menu()
    print()
    command = (checker(input("Введите номер меню: ")))
    command = int(command)

    if 0 < command < 7:
        # 1. Выбрать файл для работы
        if command == 1:
            while True:
                file = input('Введите полный или относительный путь к файлу: ')
                if os.path.isfile(file): break
                print('Такого файла не существует. Повторите ввод')
        if command == 2:
            if file is None:
                print('Не выбран файл для инициализации БД')
                continue
            database = open(file, 'w+')
            fields = []
            whole_row = ''
            for i in range(digit_input('Введите количество полей: ')):
                while True:
                    row = input('Введите имя {}-ого поля и его тип данных через пробел: '.format(i + 1)).split()
                    if len(row) != 2:
                        print('Данные введены неверно. Повторите ввод')
                        continue
                    if row[1] in types:
                        break
                    print('Неверный тип данных. Повторите ввод')
                fields.append(row)
            print(fields)
        if command == 3:
            if file is None:
                print('Не выбран файл для инициализации БД')
                continue
            database.seek(0)
            row = database.readline()
            if row == '':
                print('В БД нет содержимого')
                continue
            while row:
                print(row.rstrip('\n').replace(' | ', ' '))
                row = database.readline()
        if command == 4:
            if file is None:
                print('Не выбран файл для инициализации БД')
                continue
            while True:
                flag = True
                row = input('Введите содержимое записи через пробел: ')
                row_split = row.split()
                if len(row_split) != len(fields):
                    print('Количество элементов не совпадает. Повторите ввод')
                    continue
                for i in range(len(row_split)):
                    if fields[i][1] == 'int' and isDigit(row[i]) != True:
                        print(
                            'Ошибка. Тип данных {}-ого элемента не совпадает с типом данных поля. Повторите ввод'.format(
                                i + 1))
                        flag = False
                        break
                if flag:
                    break
                continue
            row = row.replace(' ', ' | ')
            row += '\n'
            database.seek(0, 2)
            database.write(row)
            database.flush()
        if command == 5:
            if file is None:
                print('Не выбран файл для инициализации БД')
                continue
            database.seek(0)
            search1 = input('Введите название поля для поиска и шаблон имени через пробел: ').split()
            flag1 = False
            flag2 = False
            for i in range(len(fields)):
                if search1[0] == fields[i][0]:
                    flag1 = True
                    row = database.readline()
                    while row:
                        if row.rstrip('\n').split(' | ')[i] == search1[1]:
                            flag2 = True
                            print(row.rstrip('\n').replace(' | ', ' '))
                        row = database.readline()
            if not flag1:
                print('Введенное название не совпадает ни с одним из столбцов')
            if not flag2:
                print('Не найдено ни одного совпадения')
        if command == 6:
            if file is None:
                print('Не выбран файл для инициализации БД')
                continue
            database.seek(0)

            search1 = input('Введите первое название поля для поиска и шаблон имени через пробел: ').split()
            search2 = input('Введите второе название поля для поиска и шаблон имени через пробел: ').split()
            flag1 = False
            flag2 = False

            for i in range(len(fields) - 1):
                for j in range(i + 1, len(fields)):
                    if search1[0] == fields[i][0] and search2[0] == fields[j][0]:
                        flag1 = True
                        row = database.readline()
                        while row:
                            row_split = row.rstrip('\n').split(' | ')
                            if row_split[i] == search1[1] and row_split[j] == search2[1]:
                                flag2 = True
                                print(row.rstrip('\n').replace(' | ', ' '))
                            row = database.readline()
            if flag1 == False:
                print('Одно или несколько введенных названий не совпадают ни с одним из столбцов')
            if flag2 == False:
                print('Не найдено ни одного совпадения')
