import collections

pets = {
    1:
        {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел"
            },
        },
    2:
        {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша"
            },
        },
}
def create(name, typ, age, name_masters):
    last = collections.deque(pets, maxlen=1)[0]
    last += 1
    pets[last] = {
        name: {
            "Вид питомца": typ,
            "Возраст питомца": age,
            "Имя владельца": name_masters
        }
    }

def delete():
    pets.clear()
    print("Словарь чист.")
def update(id, name, oper):
    if oper == "Возраст":
        y = input("Введите новый возраст: ")
        pets[id][name]["Возраст питомца"] = y
    elif oper == "Вид":
        y = input("Введите новый вид: ")
        pets[id][name]["Вид питомца"] = y
    elif oper == "Имя владельца":
        y = input("Введите новое имя владельца: ")
        pets[id][name]["Имя владельца"] = y

def get_all(id, name):
    print(f"Это {pets[id][name]["Вид питомца"]} по кличке {name}. Возраст питомца {get_suffix(pets[id][name]["Возраст питомца"])}"
          f". Имя владельца {pets[id][name]["Имя владельца"]}")

def get_pet(ID):
   return print(pets[ID]) if ID in pets.keys() else print(False)

def get_suffix(age):
    if age >= 5 or age == 0:
        return f"{age} лет"
    elif age <= 4 and age > 1:
        return f"{age} года"
    else:
        return f"{age} год"

def pets_list():
    for i in pets.values():
        print("Кличка животного:", *i)

print("Доступные команды: создать, удалить, обновить, прочитать, найти, лист, стоп.")
command = input("Введите желаемое действие: ")
if ord(command[0]) >= 1072:
    command = command.capitalize()
while command != "Стоп":
    if command == "Создать":
        name = input("Введите кличку питомца: ")
        typ = input("Введите вид питомца: ")
        age = int(input("Введите возраст питомца:"))
        name_masters = input("Введите имя владельца: ")
        create(name, typ, age, name_masters)
    elif command == "Удалить":
        delete()
    elif command == "Обновить":
        print("Вы можете обновить: возраст, вид, имя владельца")
        oper = input("Что вы хотите обновить? : ")
        oper = oper.capitalize()
        id = int(input("Введите индекс питомца: "))
        name = input("Введите имя питомца: ")
        update(id, name, oper)
    elif command == "Прочитать":
        id = (int(input("Введите индекс питомца: ")))
        name = input("Введите имя питомца: ")
        get_all(id, name)
    elif command == "Найти":
        get_pet(int(input("Введите ID искомого питомца: ")))
    elif command == "Лист":
        pets_list()
    elif command == "Стоп":
        break
    else:
        print("Неверно введена команда. Попробуйте еще раз. .")
    print("Доступные команды: создать, удалить, обновить, прочитать, найти, лист, стоп.")
    command = input("Введите желаемое действие: ")
    if ord(command[0]) >= 1072:
        command = command.capitalize()