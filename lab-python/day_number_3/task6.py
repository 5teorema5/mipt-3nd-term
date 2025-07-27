class Garage:
    def __init__(self):
        self.array = []

    def park(self, v):
        self.array.append(v)

    def count(self, t):
        c = 0
        # t_str = str(t).split('.')[-1][:-2]
        # class_ = globals()[t_str]
        # subclass_ = class_.__subclasses__()
        for x in self.array:
            if isinstance(x, t):
                c += 1
        return c

    def get_fastest_of_type(self, t):
        car, max_speed = None, 0
        # t_str = str(t).split('.')[-1][:-2]
        # class_ = globals()[t_str]
        # subclass_ = class_.__subclasses__()
        for x in self.array:
            # if type(x) == t or x.__class__ in subclass_:
            #     if x.speed > max_speed:
            #         max_speed = x.speed
            #         car = x
            if isinstance(x, t):
                if x.speed > max_speed:
                    max_speed = x.speed
                    car = x
        return car


class Car:
    def __init__(self, c, s, n):
        self.capacity = int(c)
        self.speed = int(s)
        self.number = n


class Truck(Car):
    pass


class Bus(Car):
    pass


g = Garage()
g.park(Car(1, 100, "abc"))
g.park(Truck(1000, 150, "zzz"))
g.park(Bus(100, 50, "QWE"))
g.park(Bus(100, 80, "ASD"))
g.park(Bus(100, 20, "ZXC"))

# Сколько всего машин? Ожидаем 5, потому что грузовик и автобус - тоже машины.
print(g.count(Car))
# Сколько всего грузовиков? Ожидаем 1.
print(g.count(Truck))
# Сколько всего автобусов? Ожидаем 3.
print(g.count(Bus))
# Получим самую быструю машину и выведем её номер. Ожидаем zzz, потому что грузовик внезапно самый быстрый.
print(g.get_fastest_of_type(Car).number)
# Получим самый быстрый грузовик и выведем его номер. Ожидаем zzz.
print(g.get_fastest_of_type(Truck).number)
# Получим самый быстрый автобус и выведем его номер. Ожидаем ASD.
print(g.get_fastest_of_type(Bus).number)
