import random


class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.cur_speed = 0
        self.trav_dist = 0

    def intro(self):
        print(f'\nRegistration number: {self.reg_number}\n'
              f'Maximum speed: {self.max_speed} km/h\n'
              f'Current speed: {self.cur_speed} km/h\n'
              f'Traveled distance: {self.trav_dist} km')

    def accelerate(self, change):
        self.cur_speed += change
        if self.cur_speed > self.max_speed:
            self.cur_speed = self.max_speed
        elif self.cur_speed < 0:
            self.cur_speed = 0

    def drive(self, hours):
        change = hours * self.cur_speed
        self.trav_dist += change


class ElectricCar(Car):
    def __init__(self, reg_number, max_speed, battery_cap):
        super().__init__(reg_number, max_speed)
        self.battery_cap = battery_cap


class GasolineCar(Car):
    def __init__(self, reg_number, max_speed, vol_tank):
        super().__init__(reg_number, max_speed)
        self.vol_tank = vol_tank


e_car = ElectricCar("ABC-15", 180, 52.5)
normal_car = GasolineCar("ACD-123", 165, 32.3)

e_car.accelerate(random.randint(10, 200))
normal_car.accelerate(random.randint(10, 200))

e_car.drive(3)
e_car.intro()

normal_car.drive(3)
normal_car.intro()
