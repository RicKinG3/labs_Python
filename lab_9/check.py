def checker(num):
    while True:
        if num.isdigit(): return num
        num = input("Введите целое натуральное число заново: ")

def matrix_check(num):
    if num.isdigit() or (num[0] =='-' and num[1::].isdigit()) or (num[0] =='+' and num[1::].isdigit()):
        return True
    else:
        return False

def check_num_float(n):
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
            print("{:<15}".format(a[i][j]), end=' ')
        print()