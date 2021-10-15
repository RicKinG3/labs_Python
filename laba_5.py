# Вычислить сумму бесконечного ряда с точностью до ерс
# Выполнил работу Вольняга Максим ИУ7-16Б

def func(n) -> float:
    return (1 / ((2 * n - 1) * (2 * n + 1)))


# Вввод входных данных
EPS = float(input('Введите эпсилон: '))
step = float(input('Введите итерационный шаг: '))
end = float(input('Введите конечное количество итераций: '))
sum = 0             # Сумма
current = 1         # Текущая итерация

# Проверка входных данных
exit('Вы ввели неверные данные') if step != int(step) or step == 0 or int(end) != end or end == 0 else print()

# Шапка таблицы
print('-' * 46 + '\n|{0:^18}|{1:^11}|{2:^13}|\n|'.format("№ Итерации", 't', 'Sum ') + '-' * 44 + '|')

# Пока текущая итерация меньше или рав конечной заданной
while current <= end:
    new_x = func(current)           # Считаем член ряда
    sum += new_x                    # Добавляем к сумме
    if (current - 1) % step == 0:   # Выводим на заданный шаг
        print(f'|{current:^18}|{new_x:>11.4g}|{sum:>13.4g}|')
    if abs(new_x) <= EPS:           # Сверяем точность
        print('-' * 46)
        print(f'Сумма бесконечного ряда - {sum:.5f}. Всего итераций: {current}')
        exit(-1)
    current += 1  # Добавляем 1 к итерации
print('-' * 46)
print(f'Не удалось достичь нужной точности. Всего итераций: {end}')
Loading complete
