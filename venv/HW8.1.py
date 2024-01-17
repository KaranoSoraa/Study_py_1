# https://github.com/KaranoSoraa/Study_py_1/tree/master
start = int(input("Задайте количество строк: "))
mid = []
for i in range(start):
    a = int(input("Введите число:"))
    mid.append(a)
# mid.reverse()
# print(mid)

print(mid[::-1])
