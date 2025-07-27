class Ball:
    def __init__(self, x, y, m):
        self.x = x
        self.y = y
        if m > 0:
            self.m = m
        else:
            raise Exception()

    # Переместить шарик на dx вдоль оси OX и на dy вдоль оси OY
    def move(self, dx, dy):
        self.x += dx
        self.y += dy


b = Ball(0.0, 0.0, 1.0)
print(b.x, b.y, b.m)
b.move(1.0, -1.0)
print(b.x, b.y, b.m)
