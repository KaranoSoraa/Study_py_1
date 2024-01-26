# https://github.com/KaranoSoraa/Study_py_1/tree/master
n = int(input("Введите число: "))
st1 = set()

for i in range(n):
    x = int(input("Введите число для первого массива: "))
    st1.add(x)
st2 = set(map(int, input("Вводите числа для второго массива через пробел: ").split()))

print(len(st1.union(st2)))

