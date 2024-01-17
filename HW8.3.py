# https://github.com/KaranoSoraa/Study_py_1/tree/master
weight = int(input("Введите вес, который может выдержать лодка: "))
fish = int(input("Введите количество рыбаков: "))
we_fish = [] # массив для веса рыбаков
for i in range(fish):
    weight_fish = int(input(f"Введите вес рыбака номер {i+1}: "))
    we_fish.append(weight_fish)
start = 0
que = 0
x = 0
long = len(we_fish)
for i in range(long-1):
    if we_fish[i] + we_fish[i+1] <= weight:
        print("Два рыбака смогли переправиться.")
        que += 1
    elif we_fish[i] <= weight:
        print("Один рыбак смог переправиться")
        que += 1
fin = "лодки" if que % 2 == 0 else "лодок"
print(f"Для переправки всех рыбаков было использовано {que} {fin}")

