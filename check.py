def checker(num):
    while True:
        if num.isdigit(): return num
        num = input("Введите целое натуральное число заново: ")

def matrix_check(num):
    if num.isdigit() or (num[0] =='-' and num[1::].isdigit()) or (num[0] =='+' and num[1::].isdigit()):
        return True
    else:
        return False
