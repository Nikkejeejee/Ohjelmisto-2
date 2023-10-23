class Car():
    def __init__(self, name, reg_number, max_speed, cur_speed, trav_dist):
        self.name = name
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.cur_speed = cur_speed
        self.trav_dist = trav_dist


    def intro(self):
        print(f'Name: {self.name}\n'
              f'Registration number: {self.reg_number}\n'
              f'Maximum speed: {self.max_speed} km/h\n'
              f'Current speed: {self.cur_speed} km/h\n'
              f'Traveled distance: {self.trav_dist} km')


car = Car('Porsche', 'ABC-123', 142, 0, 0)
car.intro()
