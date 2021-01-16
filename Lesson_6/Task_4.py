class Car:
    """Базовый класс"""
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('The car ride.')

    def stop(self):
        print('The car stop.')

    def turn(self, direction):
        if direction == 'left':
            print('The car turn left.')
        elif direction == 'right':
            print('The car turn right.')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    """Проверка скорости автомобилей"""
    def show_speed(self):
        if self.speed > 60:
            print('Slow down. Limitation 60 km/h. You are driving at speed ' + str(self.speed) + ' km/h.')
        else:
            print(self.speed)


class SportCar(Car):
    """Добавил спорт-режим к этому клссу"""
    def sport_mode(self, on_off):
        if on_off == 'on':
            print('Switched to sport mode!')
        elif on_off == 'off':
            print('Switched to town mode!')


class WorkCar(Car):
    """Проверка скорости автомобилей"""
    def show_speed(self):
        if self.speed > 40:
            print('Slow down. Limitation 60 km/h. You are driving at speed ' + str(self.speed) + ' km/h.')
        else:
            print(self.speed)


class PoliceCar(Car):
    """Добавил включение и выключение сирен"""
    def turn_the_siren(self, on_off):
        if on_off == 'on':
            print('Siren is on!')
        elif on_off == 'off':
            print('Siren is off!')


town_car_1 = TownCar(70, 'Black', 'Seat', True)
town_car_2 = TownCar(50, 'Yellow', 'Pegout', False)
sport_car_1 = SportCar(80, 'Black', 'BMW', False)
sport_car_2 = SportCar(100, 'White', 'Mercedes', True)
work_car_1 = WorkCar(40, 'Red', 'Alfa Romeo', True)
work_car_2 = WorkCar(50, 'Violet', 'Skoda', False)
police_car_1 = PoliceCar(50, 'Black-White', 'Toyota', True)
