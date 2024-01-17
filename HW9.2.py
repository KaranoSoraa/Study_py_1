import random
# https://github.com/KaranoSoraa/Study_py_1/tree/master
li = []
li2 = []
for i in range(random.randint(0,1000000)):
    li.append((random.randint(0, 10)))
    li2.append((random.randint(0,10)))

print(f"Всего элементов в обоих списках:{len(li) + len(li2)}")