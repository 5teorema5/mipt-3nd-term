class MoneyBox:
    # Конструктор и деструктор, если нужны
    def __init__(self):
        self.money = 0
        self.coin = 0

    # Добавить монетку достоинством value
    def add_coin(self, value):
        self.money += value
        self.coin += 1

    # Получить текущее количество монеток в копилке
    def get_coins_number(self):
        return self.coin

    # Получить текущее общее достоинство всех монеток
    def get_coins_value(self):
        return self.money


m = MoneyBox()
# Добавили монетку достоинством 10
m.add_coin(10)
# Добавили монетку достоинством 5
m.add_coin(5)

# Ожидаем, что монеток внутри 2 штуки
print(m.get_coins_number())
# Ожидаем, что общее достоинство всех монеток 15
print(m.get_coins_value())
