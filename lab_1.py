## Программа для вычисления геометрических характеристик(площадь, объем, высоты) сектора сферы
#
## Сделал Вольняга Максим ИУ7-16Б

# Импортируем библиотеку math, sys
import math as m
import sys

# Ввод радиуса сферы 
R = float(input('Введите радиус сферы: '))
# Радиус сектора
r = float(input('Введите радиус сектора: '))

# Проверка на отрицательные значения
if R < 0 or r<0:
    print('Величины имеют отрицательные значения')
    sys.exit(0)
# Проверка на нулевые значения
if R == 0 or r == 0:
    print('Величины имеют нулевые значения')
    sys.exit(0)
#Проверка радиусов: R>r
if R<r:
    print('Радиус сектора больше радиуса сферы ')
    sys.exit(0)

# Площадь полной поверхности шарового сектора  
S = m.pi*R*(2*(R - m.sqrt(R**2 - r**2)) + r)
# Высота конуса
H = m.sqrt(R**2 - r**2)
# Высота сегмета
h = R - m.sqrt(R**2 - r**2)
# Объем шарового сектора
V = 2/3*m.pi*R**2*h

# Вывод (пощади полной поверхности шарового сектора,  Объем шарового сектора,
                #высота конуса, высота конуса) с округлением до 6 знаков после запятой
print('Площадь полной поверхности шарового сектора: {0:.6f}\n\
Объем шарового сектора:  {1:.6f}\n\
Высота конуса:  {2:.6f}\n\
Высота сегмета: {3:.6f}'.format(S, V, H, h))                     
