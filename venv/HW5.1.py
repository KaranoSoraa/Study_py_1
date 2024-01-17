# https://github.com/KaranoSoraa/Study_py_1/tree/master
x = int(input("Введите число: "))

if x > 0 and x % 2 == 0:
    print(f"Число {x} четное положительное")
elif x < 0 and x % 2 == 0:
    print(f"Число {x} четное отрицательное")
elif x == 0:
    print(f"Число {x} четное нулевое")
elif x > 0 and x % 2 != 0:
    print(f"Число {x} нечетное положительное.")
elif x < 0 and x % 2 != 0:
    print(f"Число {x} нечетное отрицательное.")
else:
    print("Ошибка.")