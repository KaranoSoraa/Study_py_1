# https://github.com/KaranoSoraa/Study_py_1/tree/master
class Transport(object):
   def __init__(self, name, max_speed, mileage):
       self.name = name
       self.max_speed = max_speed
       self.mileage = mileage

   def seating_capacity(self, capacity):
       return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"

class Autobus(Transport):
    capacity = 50
    def __init__(self,name, max_speed, mileage, s_c):
        super().__init__(name, max_speed, mileage)
        self.capacity = s_c
    def seating_capacity(self):
        return f"Вместимость одного автобуса {self.name}:  {self.capacity} пассажиров"


