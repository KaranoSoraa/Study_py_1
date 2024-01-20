# https://github.com/KaranoSoraa/Study_py_1/tree/master
pets = dict()
x = int(input("Введите количество операций:"))
for i in range(x):
    name = input("Введите имя питомца: ")
    pets[name] = {"Вид питомца:": input("Введите вид питомца: "),
                  "Возраст питомца:": int(input("Введите возраст питомца: ")),
                  "Хозяин питомца:": input("Введите имя хозяина питомца: ")}
print(f"Это {pets[name]["Вид питомца:"]} по кличке {pets.keys()}, возрастом {pets[name]["Возраст питомца:"]} "
      f". Имя хозяина {pets[name]["Хозяин питомца:"]}")

#Еще под вопросом.