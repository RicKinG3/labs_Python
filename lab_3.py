## Программа которая по введенным целочисленным координатам трех точек на плоскости вычисляет стороны
# образованного треугольника и длину биссектрисы,проведенной из наименьшего угла. Определяет является ли трехугольник остроугольным.
# (2)Далее по введенным координатам определить,находится ли точка внутри треугольника.Если да,то найдем расстояние от точки 
# до ближайшей стороны треугольника или ее продолжения
#
## Выполнил     Вольняга Максим ИУ7-16Б

#  Импортируем библиотеку math
import math as m

# Ввод координат точек А В С

def S(ab, bc, ac) -> float:
    p = (ab + bc + ac) / 2
    S = abs(p * (p - ab) * (p - bc) * (p - ac)) ** (1/2)
    return S

ax, ay = map(int, input('Введите координаты точки А \n').split())  # Координата точки А
bx, by = map(int, input('Введите координаты точки В \n').split())  # Координата точки B
cx, cy = map(int, input('Введите координаты точки С \n').split())  # Координата точки C

ab = 0  # Длина АВ
bc = 0  # Длина ВС
ac = 0  # Длина АС

ab = m.sqrt((bx-ax) ** 2 + (by-ay) ** 2)   # Длина АВ
bc = m.sqrt((cx-bx) ** 2 + (cy-by) ** 2)   # Длина ВС
ac = m.sqrt((cx-ax) ** 2 + (cy-ay) ** 2 )  # Длина АС
print('Длина АВ =  {0:.6f}\n\
Длина ВС = {1:.6f}\n\
Длина АС = {2:.6f}'.format(ab, bc, ac))


# Существование треугольника и  является ли трехугольник остроугольным
if S(ab, bc, ac) != 0:
    if (ab*ab + bc*bc < ac*ac) or (ab*ab + ac*ac < bc*bc) or (ac*ac + bc*bc < ab*ab):
        print("треугольник не остоугольный")
    else:
        print("остроугольный")
else:
    print("треугольник невозможен")
    exit(0) 
    
degreeA = m.degrees(m.acos((ab ** 2 + ac ** 2 -bc ** 2) / (2 * ab * ac))) # Угол при вершине А
degreeB = m.degrees(m.acos((ab ** 2 + bc ** 2 -ac ** 2) / (2 * ab * bc))) # Угол при вершине B
degreeC = m.degrees(m.acos((ac ** 2 + bc ** 2 -ab ** 2) / (2 * bc * ac))) # Угол при вершине C

# Найдем длину биссектрисы, проведенной из наименьшего угла
bis1 = (2*ab*ac*m.cos(m.radians(degreeA/2)) / (ab+ac))        # Из угла А
bis2 = (2*ab*bc*m.cos(m.radians(degreeB/2)) / (ab+bc))        # Из угла B                        
bis3 = (2*bc*ac*m.cos(m.radians(degreeC/2)) / (bc+ac))        # Из угла C 
print('Длина биссектрисы из наим. угла = {0:.6f}'.format(max(bis1, bis2, bis3)))

# Определим находится ли точка внутри треугольника, если да, то найдем ближайшее растояние до прямой или продолж.
tx, ty = map(float, input().split())      #ввод точки

# Вычислим  псевдоскалярное произведение.
p1 = (ax - tx) * (by - ay) - (bx - ax) * (ay - ty)
p2 = (bx - tx) * (cy - by) - (cx - bx) * (by - ty)
p3 = (cx - tx) * (ay - cy) - (ax - cx) * (cy - ty)

if (p1 > 0 and p2 > 0 and p3 > 0) or (p1 < 0 and p2 < 0 and p3 < 0 ):
    print('точка внутри')
elif p1 == 0 or p2 == 0 or p3 == 0:
    print("точка на триугольнике и расстояние = 0")
    (exit(0))
else:
    print("точка за пределом теугольника")
    (exit(0))
 
# Перемещяем треугольник точкой один в начало координат
bxRel = bx - ax
byRel = by - ay
cxRel = cx - ax
cyRel = cy - ay
txRel = tx - ax
tyRel =ty - ay

# Вычисляем расстояния от точки t до всех прямых
dist12 = abs(byRel * txRel - bxRel *tyRel) / m.sqrt(byRel ** 2 + bxRel ** 2)
dist23 = abs((cyRel - byRel) * txRel - (cxRel-bxRel) *tyRel - bxRel *
             (cyRel - byRel) + byRel * (cxRel - bxRel))/m.sqrt((cyRel - byRel) ** 2 + (cxRel-bxRel) ** 2)
dist31 = abs(cyRel * txRel - cxRel *tyRel) / m.sqrt(cyRel ** 2 + cxRel ** 2)
print('Минимальное расстояние от точки до прямой или ее продолжения = {0:.6f}'.format(min(dist12, dist23,dist31)))




