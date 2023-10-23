class Car():
    def __init__(self, reg_number, max_speed, cur_speed, trav_dist):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.cur_speed = cur_speed
        self.trav_dist = trav_dist


    def intro(self):
        print(f'Registration number of this car is: {uusi_auto.reg_number}\n'
              f'Maxmimum speed: {uusi_auto.max_speed}\n'
              f'Current speed: {uusi_auto.cur_speed}\n'
              f'Travelled distance: {uusi_auto.trav_dist}')


    def kiihdyta(self, cur_speed):
        if self.cur_speed < 0:
            return

uusi_auto = Car('ABC-123', 142, 0, 0)
uusi_auto.intro()

