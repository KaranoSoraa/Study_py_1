# https://github.com/KaranoSoraa/Study_py_1/tree/master
Mike = 12000
Ivan = 20000
cash = 30000

if Mike >= cash and Ivan >= cash:
    print(2)
elif Mike >= cash:
    print("Mike")
elif Ivan >= cash:
    print("Ivan")
elif (Mike + Ivan) >= cash:
    print(1)
else:
    print("0")