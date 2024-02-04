import random
# https://github.com/KaranoSoraa/Study_py_1/tree/master
li = []
li2 = []
for i in range(random.randint(1, 10)):
    li.append((random.randint(0, 10)))
    li2.append((random.randint(0, 10)))
print(set(li))
print(set(li2))

print(f"Всего общих элементов в обоих списках:{len(set(li) & (set(li2)))}")
