# https://github.com/KaranoSoraa/Study_py_1/tree/master
def suf(age):
    if age == 1:
        return "год"
    elif (age > 1) and (age < 5) or (age > 21) and (age < 25):
        return "года"
    else:
        return "лет"


pets = dict()
x = int(input("Введите количество операций:"))
for i in range(x):
    name = input("Введите имя питомца: ")
    pets[name] = {"Вид питомца:": input("Введите вид питомца: "),
                  "Возраст питомца:": int(input("Введите возраст питомца: ")),
                  "Хозяин питомца:": input("Введите имя хозяина питомца: ")}
    print(f"Это {pets[name]["Вид питомца:"]} по кличке {name}, возрастом {pets[name]["Возраст питомца:"]} {suf(pets[name]["Возраст питомца:"])}. "
        f"Имя хозяина {pets[name]["Хозяин питомца:"]}")
    print()