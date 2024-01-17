# https://github.com/KaranoSoraa/Study_py_1/tree/master
word = input("Введите слово(на английском): ")
gl, so = 0, 0
a, b, c, d, e = 0, 0, 0, 0, 0
for i in word:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        gl += 1
        if i == 'a':
            a += 1
        elif i == 'e':
            b += 1
        elif i == 'i':
            c += 1
        elif i == 'o':
            d += 1
        elif i == 'u':
            e += 1
        else:
            print(False)
            break
    else:
        so += 1
print(f"Всего гласных: {gl}, всего согласных: {so}")
print(f"Всего 'a' - {a}, 'e' - {b}, 'i' - {c}, 'o' - {d}, 'u' - {e}")
