# https://github.com/KaranoSoraa/Study_py_1/tree/master
def fact(x):
    num = x
    for i in range(1, x,):
        num *= i
    return num

x = int(input("Введите число, факториал которого будет взят за основу: "))
res1 = fact(x)
list_fact = []

for i in range(res1, 0, -1):
    list_fact.append(fact(i))
print(list_fact)