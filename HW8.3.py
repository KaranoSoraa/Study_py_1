# https://github.com/KaranoSoraa/Study_py_1/tree/master
weight = int(input("Введите вес, который может выдержать лодка: "))
fish = int(input("Введите количество рыбаков: "))
we_fish = []

for i in range(fish):
    weight_fish = int(input(f"Введите вес рыбака номер {i + 1}: "))
    we_fish.append(weight_fish)

que = 0

for i in range(len(we_fish)):
    if len(we_fish) - i > 1:
        if we_fish[i] + we_fish[i + 1] <= weight:
            print("Два рыбака смогли переправиться.")
            que += 1
            we_fish.pop(i + 1)
        elif we_fish[i] <= weight:
            print("Один рыбак смог переправиться")
            que += 1
        elif we_fish[i] > weight:
            print("Кому-то пора худеть.")
    elif len(we_fish) - i == 1:
        if we_fish[i] <= weight:
            print("Один рыбак смог переправиться")
            que += 1
        elif we_fish[i] > weight:
            print("Кому-то пора худеть.")

fin = ''
if que == 1:
    fin = "лодка"
elif (que >= 2) and (que < 5):
    fin = "лодки"
elif que >= 5:
    fin = "лодок"

print(f"Для переправки всех рыбаков было использовано {que} {fin}")

