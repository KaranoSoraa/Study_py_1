# https://github.com/KaranoSoraa/Study_py_1/tree/master
a = input("Здравствуйте. Введите тип используемыех данны(int, float): ")
if a == "int":
    a, b, c = map(int, input("Введите значения сторон треугольника через пробел: ").split())
    P = a + b + c
    p = P / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("Периметр треугольника равен:", P)
    print("Площадь треугольника равна: ", S)
elif a == "float":
    a, b, c = map(float, input("Введите значения сторон треугольника через пробел: ").split())
    P = a + b + c
    p = P / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("Периметр треугольника равен:", P)
    print("Площадь треугольника равна: ", S)
else:
    print("Вы ввели не верный тип данных.")