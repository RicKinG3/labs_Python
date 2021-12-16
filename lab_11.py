# -*- coding: utf-8 -*-
# Написать программу для выполнения некоторых операций с текстом. Вводить текст не
# требуется, он должен быть задан в исходном тексте программы в виде списка строк
# (при выводе на экран каждый элемент этого списка должен начинаться с новой
# строки).
# Программа должна позволять с помощью меню выполнить следующие действия:
# 1. Выровнять текст по левому краю
# 2. Выровнять текст по правому краю
# 3. Выровнять текст по ширине
# 4. Удаление всех вхождений заданного слова
# 5. Замена одного слова другим во всём тексте
# 6. Вычисление арифметических выражений внутри текста (+-)
# 7. Отсортировать слова в лексикографическом порядке в самом длинном по
# количеству символов предложении.
#
# Выполнил Вольняга Максим ИУ7-16Б
from check import *

a = ['не жалею, не зову, не плачу, все пройдет,',
     'как с белых яблон 1 + 1+1 дым. пройдет золотом охваченный,',
     'я не буду больше молод5-5ым. Ты теперь не так уж будешь биться,',
     'сердце, тронутое холодком, и страна березового ситца.',
     'Не заманит шляться босиком. Дух бродяжий! ты все реже, реже',
     'расшевеливаешь пламень уст. О моя у траченная свежесть,',
     'буйство глаз и половодье чувств. Я теперь скупее стал в желаньях.',
     'Жизнь моя иль ты приснилась мне словно я весенней гулкой ранью.',
     'Проскакал на 7+8 розовом коне.']


def len_str(a):
    counter = 0
    counter_str = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            counter += 1
        counter_str.append(counter)
        counter = 0
    return counter_str


# Функция вывода текста
def print_str():
    for i in range(len(a)):
        print(a[i])
    return a


# Функция для удаления ненужных пробелов
def del_space(a):
    for i in range(len(a)):
        b = a[i].split()
        bi = " ".join(b)
        a[i] = bi
    return a


alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\
абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


# Функция для определения числа и операции
def symbol(line):
    t1, t2 = 0, 0
    for symbol1 in '0123456789':
        if line.find(symbol1) != -1:
            t1 = 1
            break
    for symbol2 in '+-':
        if line.find(symbol2) != -1:
            t2 = 1
            break
    return t1, t2


def letter(word):
    for i in range(len(word)):
        if word[i] in alphabet:
            return False
    return True


# Функция  для вычисления арифметических выражений внутри текста
def arithmetic_operation(a):
    for i in range(len(a)):
        line = a[i].split()
        if len(line) != 0:
            t1, t2 = symbol(a[i])
            if t1 == 1 and t2 == 1:
                flag = True
                j = 1
                stroka = line[0]
                t = 0
                mass = []
                k = 0
                count = 0
                while True:
                    while k < len(a[i]) and a[i][k] != ' ':
                        k += 1
                    while k < len(a[i]) and a[i][k] == ' ':
                        count += 1
                        k += 1
                    mass.append(count)
                    count = 0
                    if k == len(a[i]):
                        break
                while j < len(line) - 1:
                    if not flag:
                        t = j
                        j += 1
                        flag = True
                        stroka += ' ' * mass[t - 1] + line[t]
                        continue
                    if t == 0:
                        if line[t][-1] in '0123456789' and line[j][0] in '+-' and letter(line[j]) and letter(
                                line[t]) and \
                                (len(line[j]) > 1 and line[j][1] in '0123456789' or len(line[j]) == 1 and
                                 line[j + 1][0] in '0123456789'):
                            stroka += line[j]
                            flag = True
                        elif line[t][-1] in '+-' and line[j][0] in '0123456789' and letter(line[j]) and letter(
                                line[t]) and \
                                (len(line[t]) > 1 and line[t][-2] in '0123456789'):
                            stroka += line[j]
                            flag = True
                        else:
                            flag = False
                            stroka += ' ' * mass[j - 1] + line[j]
                    else:
                        if line[t][-1] in '0123456789' and line[j][0] in '+-' and letter(line[j]) and letter(
                                line[t]) and \
                                (len(line[j]) > 1 and line[j][1] in '0123456789' or len(line[j]) == 1 and
                                 line[j + 1][0] in '0123456789'):
                            stroka += line[j]
                            flag = True
                        elif line[t][-1] in '+-' and line[j][0] in '0123456789' and letter(line[j]) and letter(
                                line[t]) and \
                                (len(line[t]) > 1 and line[t][-2] in '0123456789' or len(line[t]) == 1 and
                                 line[t - 1][-1] in '0123456789'):
                            stroka += line[j]
                            flag = True
                        else:
                            flag = False
                            stroka += ' ' * mass[j - 1] + line[j]
                    j += 1
                    t += 1
                if not flag:
                    t = j
                    j += 1
                    stroka += ' ' * mass[t - 1] + line[t]
                else:
                    if line[t][-1] in '0123456789' and line[j][0] in '+-' and letter(line[j]) and letter(line[t]) and \
                            (len(line[j]) > 1 and line[j][1] in '0123456789'):
                        stroka += line[j]
                    elif line[t][-1] in '+-' and line[j][0] in '0123456789' and letter(line[j]) and letter(line[t]) and \
                            (len(line[t]) > 1 and line[t][-2] in '0123456789' or len(line[t]) == 1 and
                             line[t - 1][-1] in '0123456789'):
                        stroka += line[j]
                a[i] = stroka
    for i in range(len(a)):
        if '+' in a[i] or '-' in a[i]:
            b = a[i].split()
            if len(b) != 0:
                for j in range(len(b)):
                    if (b[j].count('-') + b[j].count('+')) > 0 and len(b[j]) >= 3:
                        start = 0
                        q = 0
                        temp = ''
                        s = 0
                        flag = False
                        flagm = False
                        flagp = False
                        first = False
                        while q < len(b[j]) - 2:
                            if q == len(b[j]) - 3:
                                if b[j][q] in '0123456789':
                                    if b[j][q + 1] == '-':
                                        if b[j][q + 2] in '0123456789':
                                            temp += b[j][q]
                                            if first:
                                                if flagp:
                                                    s += int(temp)
                                                if flagm:
                                                    s -= int(temp)
                                            else:
                                                s = int(temp)
                                            s -= int(b[j][q + 2])
                                            temp_word = b[j][start:]
                                            b[j] = b[j].replace(temp_word, str(s))
                                        else:
                                            if flag:
                                                temp += b[j][q]
                                                if flagp:
                                                    s += int(temp)
                                                    temp_word = b[j][start:(q + 1)]
                                                    b[j] = b[j].replace(temp_word, str(s))
                                                if flagm:
                                                    s -= int(temp)
                                                    temp_word = b[j][start:(q + 1)]
                                                    b[j] = b[j].replace(temp_word, str(s))
                                    elif b[j][q + 1] == '+':
                                        if b[j][q + 2] in '0123456789':
                                            temp += b[j][q]
                                            if first:
                                                if flagp:
                                                    s += int(temp)
                                                if flagm:
                                                    s -= int(temp)
                                            else:
                                                s = int(temp)
                                            s += int(b[j][q + 2])
                                            temp_word = b[j][start:]
                                            b[j] = b[j].replace(temp_word, str(s))
                                        else:
                                            if flag:
                                                temp += b[j][q]
                                                if flagp:
                                                    s += int(temp)
                                                    temp_word = b[j][start:(q + 1)]
                                                    b[j] = b[j].replace(temp_word, str(s))
                                                if flagm:
                                                    s -= int(temp)
                                                    temp_word = b[j][start:(q + 1)]
                                                    b[j] = b[j].replace(temp_word, str(s))
                                    elif b[j][q + 1] in '0123456789':
                                        if flag:
                                            temp += b[j][q]
                                            temp += b[j][q + 1]
                                            if b[j][q + 2] in '0123456789':
                                                temp += b[j][q + 2]
                                                if flagp:
                                                    s += int(temp)
                                                    temp_word = b[j][start:]
                                                    b[j] = b[j].replace(temp_word, str(s))
                                                if flagm:
                                                    s -= int(temp)
                                                    temp_word = b[j][start:]
                                                    b[j] = b[j].replace(temp_word, str(s))
                                            else:
                                                if flagp:
                                                    s += int(temp)
                                                    temp_word = b[j][start:(q + 2)]
                                                    b[j] = b[j].replace(temp_word, str(s))
                                                if flagm:
                                                    s -= int(temp)
                                                    temp_word = b[j][start:(q + 2)]
                                                    b[j] = b[j].replace(temp_word, str(s))
                                elif b[j][q] in '+-' and first:
                                    s += int(temp)
                                    if b[j][q + 1] in '0123456789':
                                        if b[j][q + 2] in '0123456789':
                                            temp = b[j][q + 1:]
                                            if b[j][q] == '+':
                                                s += int(temp)
                                                temp_word = b[j][start:]
                                                b[j] = b[j].replace(temp_word, str(s))
                                            elif b[j][q] == '-':
                                                s -= int(temp)
                                                temp_word = b[j][start:]
                                                b[j] = b[j].replace(temp_word, str(s))
                                        else:
                                            temp = b[j][q + 1]
                                            if b[j][q] == '+':
                                                s += int(temp)
                                                temp_word = b[j][start:(q + 2)]
                                                b[j] = b[j].replace(temp_word, str(s))
                                            elif b[j][q] == '-':
                                                s -= int(temp)
                                                temp_word = b[j][start:(q + 2)]
                                                b[j] = b[j].replace(temp_word, str(s))
                                break
                            elif b[j][q] in '0123456789':
                                if b[j][q + 1] not in '0123456789+-':
                                    if flag:
                                        temp += b[j][q]
                                        if flagp:
                                            s += int(temp)
                                        if flagm:
                                            s -= int(temp)
                                        temp_word = b[j][start:(q + 1)]
                                        b[j] = b[j].replace(temp_word, str(s))
                                        first = False
                                        temp = ''
                                        s = 0
                                else:
                                    if not first:
                                        start = q
                                        first = True
                                    temp += b[j][q]
                            elif b[j][q] == '+' and b[j][q + 1] in '0123456789' and first:
                                if flag:
                                    if flagp:
                                        s += int(temp)
                                    if flagm:
                                        s -= int(temp)
                                else:
                                    s += int(temp)
                                flag = True
                                flagp = True
                                flagm = False
                                temp = ''
                            elif b[j][q] == '-' and b[j][q + 1] in '0123456789' and first:
                                if flag:
                                    if flagp:
                                        s += int(temp)
                                    if flagm:
                                        s -= int(temp)
                                else:
                                    s += int(temp)
                                flag = True
                                flagm = True
                                flagp = False
                                temp = ''
                            else:
                                temp = ''
                            q += 1
                a[i] = ' '.join(b)
    return a


# Функция для выравнивания текста по центру
def align_to_width(a):
    max_len = 0  # Максимальная длина строки
    for s in a:
        if len(s) > max_len:
            max_len = len(s)
    for i in range(len(a)):
        b = a[i].split()
        dif = max_len - len(a[i])
        if dif != 0:
            if len(b) == 0:
                a[i] = ' ' * max_len
            elif len(b) == 1:
                if dif % 2 == 0:
                    a[i] = ' ' * (dif // 2) + a[i] + ' ' * (dif // 2)
                else:
                    a[i] = ' ' * (dif // 2) + a[i] + ' ' * (dif // 2 + 1)
            elif len(b) == 2:
                a[i] = b[0] + ' ' * (dif + 1) + b[1]

            else:
                if dif % (len(b) - 1) == 0:
                    a[i] = b[0]
                    for j in range(1, len(b)):
                        a[i] += ' ' * ((dif // (len(b) - 1)) + 1) + b[j]
                else:
                    a[i] = b[0]
                    for j in range(1, (dif % (len(b) - 1)) + 1):
                        a[i] += ' ' * (dif // (len(b) - 1) + 2) + b[j]
                    for k in range((dif % (len(b) - 1)) + 1, len(b)):
                        a[i] += ' ' * (dif // (len(b) - 1) + 1) + b[k]
    return a


# Функция меню
def menu():
    print('Меню команд:')
    print('1 - Выровнять текст по левому краю')
    print('2 - Выровнять текст по правому краю')
    print('3 - Выровнять текст по ширине')
    print('4 - Удаление всех вхождений заданного слова')
    print('5 - Замена одного слова другим во всём тексте')
    print('6 - Вычисление арифметических выражений внутри текста (+-)')
    print('7 - Отсортировать слова в лексикографическом порядке в самом длинном по количеству символов предложении.')


#  Меню
while True:
    print()
    menu()
    print()
    command = (checker(input("Введите номер меню: ")))
    command = int(command)

    if 0 < command < 8:
        # 1. Выровнять текст по левому краю
        if command == 1:
            a = del_space(a)
            for i in range(len(a)):
                a[i] = a[i].lstrip()
            print()
            print_str()
        # 2. Выровнять текст по правому краю
        if command == 2:
            a = del_space(a)
            counter_str = len_str(a)
            max_str = max(counter_str)
            for i in range(len(a)):
                if len(a[i]) < max_str:
                    a[i] = ' ' * (max_str - counter_str[i]) + a[i]
            print()
            print_str()
        # 3. Выровнять текст по ширине
        if command == 3:
            for i in range(len(a)):
                a[i] = a[i].lstrip()
            align_to_width(a)
            print()
            print_str()
        # 4. Удаление всех вхождений заданного слова
        if command == 4:
            word = input('Введите слово для удаления: ')
            word = ',' + '.' + word + ',' + '.'
            a = [' '.join(w for w in i.split() if w not in word) for i in a]
            print()
            print_str()
        # 5. Замена одного слова другим во всём тексте
        if command == 5:
            word1 = input('Введите слово для замены: ')
            word_replaceable = input('Введите заменяемое слово: ')
            a = [i.replace(word_replaceable, word1) for i in a]
            print()
            print_str()
        if command == 6:
            a = arithmetic_operation(a)
            print_str()
        # 7. Отсортировать слова в лексикографическом порядке в самом длинном по
        if command == 7:
            line = ''
            counter = 0
            mas_counter = []
            for i in range(len(a)):
                line += ' ' + a[i] + ' \n '
            line_point = line.split('.')
            for i in range(len(line_point)):
                for j in range(len(line_point[i])):
                    counter += 1
                mas_counter.append(counter)
                counter = 0
            maxx = line_point[mas_counter.index(max(mas_counter))]
            w = maxx.split()
            new_max_str = ""
            for r in sorted(w):
                new_max_str = new_max_str + " " + r
            c, m = 0, 0
            f = 0
            for i in line_point[mas_counter.index(max(mas_counter))]:
                c += 1
                if i == '\n' and f == 0:
                    m = c
                    f = 1
            new_max_str = new_max_str[:m] + ' \n ' + new_max_str[m:len(new_max_str) - 1]
            line_point[mas_counter.index(max(mas_counter))] = new_max_str
            a.clear()
            s = ''
            for i in line_point:
                f = 0
                for j in i:
                    if j.isupper() and f == 0:
                        s += '.'
                        f = 1
                s += i
            s = s.split('\n')
            a = s
            a = del_space(a)
            print_str()
