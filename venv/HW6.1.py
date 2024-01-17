# https://github.com/KaranoSoraa/Study_py_1/tree/master
n = int(input("Введите количество чисел: "))
qua = 0
for i in range(n):
    a = int(input())
    if a == 0:
        qua += 1
print(f"Количество чисел, равных нулю: {qua}")