# https://github.com/KaranoSoraa/Study_py_1/tree/master
n = int(input("Введите количество символов: "))
lis = list(map(int, input(f"Введите {n} символов через пробел: ").split()))[::n]
se = set(lis)
print(f"Количество уникальных чисел: {len(se)}")
