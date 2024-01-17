# https://github.com/KaranoSoraa/Study_py_1/tree/master

st = "abbccbba"
que = 0
for i in range(len(st) // 2):
    if st[i] == st[-i-1]:
        que += 1
    else:
        print("No")
        break
    if que == (len(st) // 2):
        print("Yes")
