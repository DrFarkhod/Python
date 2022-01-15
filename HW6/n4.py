#4

class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала.'

    def stop(self):
        return f'\n {self.name} остановилась.'

    def turn(self, direction):
        return f'\n {self.name} повернула {direction}'

    def show_speed(self):
        return f'\n Ваша скорость составляет: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        def __init__(self, speed, color, name, is_police):
             super().__init__(speed, color, name, is_police)
        if self.speed > 60:
            return f'\nВаша скорость выше допустимой! Ваша скорость составляет: {self.speed}'
        else:
            return f'{self.name} - cкорость в норме!'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\n Ваша скорость выше допустимой! Ваша скорость составляет: {self.speed}'
        else:
            return f'{self.name} - cкорость в норме!'


class PoliceCar(Car):
    pass


town = TownCar('Audi', 70, 'blue', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())

sport = SportCar('AudiRS', 170, 'red', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = WorkCar('WAZ', 90, 'red', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())

police = PoliceCar('Kia', 100, 'yellow', False)
print('4:\n' + police.go(), police.show_speed(), police.turn('right'), police.stop())