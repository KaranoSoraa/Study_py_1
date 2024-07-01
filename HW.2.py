# 1 - Австралопитек, 2 - Человек умелый (homo habilis), 3 - Человек прямоходящий (homo erectus), 4 - Палеоантропы
# 5 - Неандерталец, 6 - Неоантропы
# https://github.com/KaranoSoraa/Study_py_1/tree/master
print("Здравствуйте. Укажите все этапы развития человека, как вида(6 этапов):")
ans1 = []
ans2 = ["Австралопитек", "Человек умелый", "Человек прямоходящий", "Палеоантроп", "Неандерталец", "Неоантроп"]
fl = False
for i in range(6):
    x = input(f"Введите {i + 1} этап: ")
    ans1.append(x)
    if ans1[i].title() == ans2[i].title():
        fl = True
    else:
        print(f"Вы ошиблись в ответе номер {i + 1}. Ответ {ans2[i]}")
        print(f"Ваш ответ: {ans1[i]}")
        exit()

print("Вы ответили верно!")
for i in ans2:
    print(i, end=" => ")