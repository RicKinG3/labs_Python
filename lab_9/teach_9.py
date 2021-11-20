# def double(x):
#     return x * x
#
#
# my_list = [1, 2, 3, 4, 5, 6]
# new_list = list(map(double, my_list))
# print(new_list)  #[1, 4, 9, 16, 25, 36]
#
# new_list1 = list(map(lambda x: x*x, my_list))
# print(new_list1)  #[1, 4, 9, 16, 25, 36]

from math import sin
#
# d = [1, 2, 3, 4, 5]
#
# f = [11, 22, 33, 44, 55]
#
# a = [[sin(j + k) for j in d] for k in f]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j])
#     print()


# av = [sum(j for j in i if j > 0) / len(i) for i in a]
# l = [len(list(filter(lambda x: x < av[i], v))) for i, v in enumerate(a)]
# for i in range(len(a)):
#     print(a[i], av[i], l[i], sep='\t')

#[[-0.5365729180004349, 0.4201670368266409, 0.9906073556948704, 0.6502878401571168], [-0.8462204041751706, -0.9055783620066238, -0.13235175009777303, 0.7625584504796027], [0.5290826861200238, -0.428182669496151, -0.9917788534431158, -0.6435381333569995], [0.8509035245341184, 0.9017883476488092, 0.123573122745224, -0.7682546613236668]]
#
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# new_matrix = [[[0] for i in range(n)] for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         new_matrix[i][j]=matrix[j][i]
# for i in range(n):
#     print(*new_matrix[i][::-1])
a = [list(map(int, input().split())) for _ in range(int(input()))]
[print(*(a[- j - 1][i] for j in range(len(a)))) for i in range(len(a))]