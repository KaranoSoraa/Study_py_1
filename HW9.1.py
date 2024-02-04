# https://github.com/KaranoSoraa/Study_py_1/tree/master
n = int(input("Введите количество символов: "))
res = set(list(map(int, input(f"Введите {n} символов через пробел: ").split()))[:n:])

print(f"Количество уникальных чисел: {len(res)}")
