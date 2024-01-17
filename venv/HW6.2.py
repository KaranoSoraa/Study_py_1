# https://github.com/KaranoSoraa/Study_py_1/tree/master
def div(x):
    div = 0
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            div += 1
            if i != x // i:
                div += 1
    return div

x = int(input("Введите натуральное число: "))
print(f"Количество натуральных делителей числа {x}: ", div(x))