# https://github.com/KaranoSoraa/Study_py_1/tree/master
def li(x, num = 0):
    two_list = x
    end = len(two_list)
    if num == end:
        return print("Выводить больше нечего.")
    print(two_list[num])
    num += 1
    li(x, num)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
li(my_list)
