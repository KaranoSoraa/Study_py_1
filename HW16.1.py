#  https://github.com/KaranoSoraa/Study_py_1/tree/master
class Cassa(object):
    cash = 50000
    def top_up(self, x):
        self.cash += x
    def count_1000(self):
        res = self.cash // 1000
        print(f"В кассе {res} тысяч рублей.")
    def take_away(self,x):
        if x <= self.cash:
            self.cash -= x
        else:
            print("Ошибка. В кассе недостаточно денег.")

