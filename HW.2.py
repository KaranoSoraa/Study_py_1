# 1 - Австралопитек, 2 - Человек умелый (homo habilis), 3 - Человек прямоходящий (homo erectus), 4 - Палеоантропы
# 5 - Неандерталец, 6 - Неоантропы
# https://github.com/KaranoSoraa/Study_py_1/tree/master
print("Здравствуйте. Укажите все этапы развития человека, как вида(6 этапов):")

q1, q2, q3, q4 = input("Первый этап: "),input("Второй этап: "),input("Третий этап: "),input("Четвертый этап: ")
q5, q6 = input("Пятый этап: "), input("Шестой этап: ")
print("Идет проверка данных")
if q1 == "Австралопитек" and q2 == "Человек умелый" and q3 == "Человек прямоходящий" and q4 == "Палеоантроп" and q5 == "Неандерталец" and q6 == "Неоантроп":
    print("Вы ответили верно! Этапы развития человека следующие: ")
    print(q1, q2, q3, q4, q5, q6, sep=" = > ")
else:
    print("Вы допустили ошибку.")

if q1 != "Австралопитек":
    print(f"Вы ошиблись с первым эпатом. Ваш вариант: {q1}. Верный вариант: Австралопитек")
if q2 != "Человек умелый":
    print(f"Вы ошиблись с первым эпатом. Ваш вариант: {q2}. Верный вариант: Человек умелый")
if q3 != "Человек прямоходящий":
    print(f"Вы ошиблись с первым эпатом. Ваш вариант: {q3}. Верный вариант: Человек прямоходящий")
if q4 != "Палеоантроп":
    print(f"Вы ошиблись с первым эпатом. Ваш вариант: {q4}. Верный вариант: Палеоантроп")
if q5 != "Неандерталец":
    print(f"Вы ошиблись с первым эпатом. Ваш вариант: {q5}. Верный вариант: Неандерталец")
if q6 != "Неоантроп":
    print(f"Вы ошиблись с первым эпатом. Ваш вариант: {q6}. Верный вариант: Неоантроп")