# https://github.com/KaranoSoraa/Study_py_1/tree/master
import random

Mike = random.randint(0, 900000)
Ivan = random.randint(0, 900000)
cash = random.randint(100000, 900000)

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