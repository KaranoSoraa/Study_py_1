# https://github.com/KaranoSoraa/Study_py_1/tree/master
import random

x, y = map(int, input().split())
mat1 = [[0 for i in range(x)] for j in range(y)]
mat2 = [[0 for i in range(x)] for j in range(y)]

for i in range(x):
    for j in range(y):
        nums = random.randint(0, 10)
        nums2 = random.randint(0, 10)
        mat1[i][j] = nums
        mat2[i][j] = nums2

print(mat1 + mat2)
