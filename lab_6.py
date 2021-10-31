# Написать программу, которая позволит с использованием меню:
# 1. Проинициализировать список первыми N элементами заданного в л/р 5 ряда
# 2. Очистить список и ввести его с клавиатуры
# 3. Добавить элемент в произвольное место списка
# 4. Удалить произвольный элемент из списка (по номеру)
# 5. Очистить список
# 6. Найти значение K-го экстремума в списке
# 7. найти наиб. длину последовательности  в которой все начиная с 3-го являются суммой двух предыдущих
##
# Вольняга Максим ИУ7-16Б
##

#Проверка на правильность ввода чисел

def Fn1(n):
    if n.isdigit():
        return True
    elif '.' in n or 'e-' in n or 'e+' in n or '-' in n:
        if "." in n and n[0:n.index(".")].isdigit() and n[n.index(".")+1:].isdigit():
            return True
        elif n[0] == "-" and "." in n and n[1:n.index(".")].isdigit() and n[n.index(".")+1::].isdigit():
            return True
        elif n[0] == "-" and n[1::].isdigit():
            return True
        elif ("e-" in n or "e+" in n) and n[n.index("e")+2::].isdigit():
            return True
        else:
            return False
    else:
        return False

#Проверка на правильность ввода номера команды
def Fn(number):
    if number.isdigit():
        if 0 < int(number) < 8:
            return True
        else:
            return False
    else:
        return False

#Проинициализировать список первыми N элементами заданного в л/р 5 ряда
def F1(spisok, n):
    n = int(n)
    k = 0
    x = 1
    while k < n:
        spisok.append(1 / ((2 * n - 1) * (2 * n + 1)))
        k += 1
        x += 1
    return spisok

#Очистить список и ввести его с клавиатуры
def F2(spisok):
    n = True
    while n:
        n = input("Введите элемент: ")
        if Fn1(n) == True:
            spisok.append(n)
        else:
            break
    return spisok

#Найти значение K-го экстремума в списке 
def F6(spisok):
    extremas = []
    for i in range(1, len(spisok) - 1):
        if spisok[i - 1] < spisok[i] > spisok[i + 1]:
            extremas.append(spisok[i])
        elif spisok[i - 1] > spisok[i] < spisok[i + 1]:
            extremas.append(spisok[i])
    return extremas

#найти наиб. длину последовательности  в которой все начиная с 3-го являются суммой двух предыдущих
       
while True:
    print("Выберите номер команды:")
    print("1)Проинициализировать список первыми N элементамии бесконенчого ряда")
    print("2)Очистить список и ввести его с клавиатуры")
    print("3)Добавить элемент в произвольное место списка")
    print("4)Удалить произвольный элемент из списка(по номеру)")
    print("5)Очистить список")
    print("6)Найти значеник К-го экстремума в списке")
    print("7)Найти найти наиб. длину последовательности  в которой все начиная с 3-го являются суммой двух предыдущих")
    print()
    number = input("Введите номер команды:")


    #Проверка на правильность ввода номера команды
    if Fn(number) == True:
        number = int(number)

        #Проинициализировать список первыми N элементами
        if number == 1:
            spisok = []
            n = input("Введите количество элементов списка: ")
            if Fn1(n) == True:
                print(F1(spisok, n))
                print()
            else:
                print("Ошибка ввода количества элементов")
                print()
                
        #Очистить список и ввести его с клавиатуры
        if number == 2:
            spisok = []
            print(F2(spisok))
            print()
            
        #Добавить элемент в произвольное место списка
        if number == 3:
            n = input("Введите элемент: ")
            k = input("Введите место в списке: ")
            if Fn1(n) == True and Fn1(k) == True and 0 <= int(k) <= len(spisok):
                k = int(k)
                spisok.insert(k, n)
                print(spisok)
                print()

            else:
                print("Неверно введен элемент или номер места в списке")
                print()
                
        #Удалить произвольный элемент из списка (по номеру)
        if number == 4:
            k = input("Введите место в списке: ")
            if Fn1(k) == True and 0 <= int(k) <= len(spisok) and k.isdigit():
                spisok.pop(int(k))
                print(spisok)
                print()

            else:
                print("Неправильно введен номер элемента")
                print()
                
        #Очистить список
        if number == 5:
            spisok.clear()
            print("Список очищен")
            print()
            
        #Поиск экстремумов
        if number == 6:
            print(F6(spisok))

        ##найти наиб. длину последовательности  в которой все начиная с 3-го являются суммой двух предыдущих 7
        m = 0
        k = 1
        if number == 7:
            for i in range(3, len(spisok)):
                if int(spisok[i]) == int(spisok[i-1]) + int(spisok[i-2]) and k > m:
                        k +=1
            m =k    
                
            print(k)
            
    else:
        print("Номер команды введен некорректно")
        print()
