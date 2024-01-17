# https://github.com/KaranoSoraa/Study_py_1/tree/master
dig = 87532
a = dig % 10 # Единицы
b = (dig // 10) % 10 # Десятки
c = (dig // 100) % 10 # Сотни
d = (dig // 1000) % 10 # Тысячи
e = (dig // 10000) % 10 # Дес.тыс.
#print(a, b, c, d, e)
res = ((b ** a) * c) / (e - d)
print(res)