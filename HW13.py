# https://github.com/KaranoSoraa/Study_py_1/tree/master
from random import randint as rint

x, y = rint(1, 10), rint(1, 10)
mat1 = [[rint(0, 10) for i in range(x)] for j in range(y)]
mat2 = [[rint(1, 10) for i2 in range(x)] for j2 in range(y)]




mat3 = [[0 for i3 in range(x)] for j3 in range(y)]
print(mat1)
print(mat2)

for i in range(y):
    for j in range(x):
         mat3[i][j] = mat1[i][j] + mat2[i][j]


print(mat3)
