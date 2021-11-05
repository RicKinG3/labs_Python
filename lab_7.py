# Написать программу, которая позволит с использованием меню обеспечить работу со
# строковыми массивами:
# 1. Очистить список и ввести его с клавиатуры
# 2. Добавить элемент в произвольное место списка
# 3. Удалить элемент из списка
# 4. Очистить список
# 5. Поиск элемента с наибольшим числом английских гласных букв
# 6. Замена всех цифр на пробелы
##
##
# Выполнил работу Вольняга Максим ИУ7-16Б
##

from check import checker


# 1 Функция очистки списока и ввода его с клавиатуры
def clear_add() -> list:
    spisok = []
    n = (checker(input("Введите кол-во элементов: ")))
    n = int(n)
    for i in range(1, n + 1):
        inp = str(input(f'Ввведите {i} элемент списка: '))
        spisok.append(inp)
    print('Теперь список: ' + str(spisok))
    return spisok


# 2. Функция для добавления элемента в произвольное место списка
def add_place(stroka, index, spisok) -> list:
    spisok_len = len(spisok)
    spisok += [0]
    for i in range(spisok_len, index, -1):
        spisok[i], spisok[i - 1] = spisok[i - 1], spisok[i]
    spisok[index] = stroka
    return spisok


# 3 Фуннкция для удаления элемента по индексу
def delit(index, spisok) -> list:
    spisok_len = len(spisok)
    for i in range(index, spisok_len - 1):
        spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]
        print(spisok[i], spisok[i + 1])
    del spisok[-1]
    return spisok


# 5 Функция поиска элемента с наибольшим числом английских гласных букв
def max_vowels(spisok) -> list:
    k = 0
    mi = 0
    for i in spisok:
        for j in i:
            if j in 'aeiouAEIOU':
                k += 1
        m = k
        if m > mi:
            mi = m
        k = 0
    print(mi)
    return spisok


# Меню
def menu() -> None:
    print('Меню команд:')
    print('0 - Выйти из программы')
    print('1 - Очистить список и ввести его с клавиатуры')
    print('2 - Добавить элемент в произвольное место списка')
    print('3 - Удалить элемент из списка')
    print('4 - Очистить список')
    print('5 - Поиск элемента с наибольшим числом английских гласных букв')
    print('6 - Замена всех заглавных гласных английских букв на строчные в элементе')


counter = 0  # Счетчик введеных команд
# Первая инициализация списка
print('Введите список с клавиатуры')
spisok = clear_add()

while True:
    if counter % 3 == 0:
        menu()
    counter += 1
    command = (checker(input("Введите номер меню: ")))
    command = int(command)

    if 0 <= command <= 7:
        # Выход из программы
        if command == 0:
            exit("Программа завершила работу")
        # Очистить список и ввести его с клавиатуры
        elif command == 1:
            spisok.clear()
            spisok = clear_add()
        # Добавление элемента в произвольное место списка
        elif command == 2:
            print('Ваш список: ' + str(spisok))
            stroka = str(input('Введите строку: '))
            index = (checker(input("Введите индекс элемнта: ")))
            index = int(index)
            if 0 <= index <= len(spisok):  # Проверка на некорректный индекс
                spisok = add_place(stroka, index, spisok)
                print('Теперь список: ' + str(spisok))
            else:
                print('Ошибка: Некорректный индекс')
        # Удаление элемента по индексу
        elif command == 3:
            print("Ваш список: " + str(spisok))
            index = (checker(input("Введите индекс элемнта: ")))
            index = int(index)
            if 0 <= index <= len(spisok):
                spisok = delit(index, spisok)
                print('Теперь список: ' + str(spisok))
            else:
                print('Ошибка: Некорректный индекс')
        # Очистка списка
        elif command == 4:
            spisok.clear()
            print('Теперь список: ' + str(spisok))
        # Поиск элемента с наибольшим числом английских гласных букв
        elif command == 5:
            print('Ваш список: ' + str(spisok))
            print('Элемент с наибольшим числом английских гласных букв: ', max_vowels(spisok))
        # k = 0
        # mi = 0
        # for i in spisok:
        #     for j in i:
        #         if j in 'aeiouAEIOU':
        #             k += 1
        #     m = k
        #     if m > mi:
        #         mi = m
        #     k = 0
        # print('Элемент с наибольшим числом английских гласных букв: ', mi)
        # Немного гольф кодинга
        # for i in spisok:
        #     k = ([sum(1 for j in i if j in 'aeiouAEIOU')])
        # print('Элемент с наибольшим числом английских гласных букв: ', max(k))
        # print(len(max([[j for j in i if j in 'aeiouAEIOU'] for i in spisok], key=len)))

        # 6. Замена всех цифр на пробелы
        elif command == 6:
            spisok = [''.join([j if j not in '1234567890' else ' ' for j in i]) for i in spisok]
            print(spisok)
