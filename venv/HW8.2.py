# https://github.com/KaranoSoraa/Study_py_1/tree/master
def rev(li):
    long = len(li)
    last = li[-1]
    for i in range(long-1, 0, -1):
        li[i] = li[i-1]
    li[0] = last
    return li

num = int(input("Введите число: "))
list = list(map(int, input("Введите числа через пробел: ").split()))

res = rev(list)
for i in range(num):
    print(f"Элемент измененного массива: {res[i]}")