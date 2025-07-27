class GasStation:
    def __init__(self, v):
        self.max_v = v
        self.v = 0

    def fill(self, n):
        if self.max_v >= self.v + n:
            self.v += n
        else:
            raise Exception()

    def tank(self, n):
        if 0 <= self.v - n:
            self.v -= n
        else:
            raise Exception()

    def get_limit(self):
        return self.v


s = GasStation(1000)
s.fill(300)
print(s.get_limit())
s.tank(100)
s.fill(300)
print(s.get_limit())
for i in range(5):
    s.tank(50)
print(s.get_limit())
s.fill(1000)
for i in range(50):
    s.tank(100)
print(s.get_limit())
