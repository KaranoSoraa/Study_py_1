# https://github.com/KaranoSoraa/Study_py_1/tree/master
a, b = map(int, input().split()) # a <= b

for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=' ')