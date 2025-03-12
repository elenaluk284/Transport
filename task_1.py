class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Autobus(Transport):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    def display_info(self):
        print(f"Название автомобиля: {self.name}")
        print(f"Скорость: {self.max_speed}")
        print(f"Пробег: {self.mileage}")


# Создаем объект Autobus
autobus = Autobus("Renaul Logan", 180, 12)

# Выводим информацию об объекте
autobus.display_info()
