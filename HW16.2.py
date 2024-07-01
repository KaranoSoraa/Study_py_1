#  https://github.com/KaranoSoraa/Study_py_1/tree/master
class Turtle(object):
    pos_x = 10
    pos_y = 10
    step = 1

    def go_up(self):
        self.pos_y += self.step

    def go_down(self):
        self.pos_y -= self.step

    def go_left(self):
        self.pos_x -= self.step

    def go_right(self):
        self.pos_x += self.step

    def evolve(self):
        self.step += 1

    def degrade(self):
        if self.step >= 1:
            self.step -= 1
        else:
            print("Черепашка не может остановиться. Она движется только вперед, в мир IT!")
            print("У ее есть мечта! Найти работу в этой сфере и стать хорошим сотрудником! Она не остановится!!!")

    def count_moves(self, x2, y2):

        resx = (self.pos_x - x2) / self.step
        resy = (self.pos_y - y2) / self.step
        if resx > 0 and resy > 0:
            return print(f"Вам нужно совершить {int(resx + resy)} действий.")
        else:
            if resx < 0:
                resx *= -1
            if resy < 0:
                resy *= -1
            return print(f"Вам нужно совершить {int(resx + resy)} действий.")
       
