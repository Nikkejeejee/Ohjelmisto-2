import random
from colorama import Fore, Style


class Car:
    def __init__(self, reg_number, max_speed, cur_speed, trav_dist):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.cur_speed = cur_speed
        self.trav_dist = trav_dist

    def intro(self):
        print(f'Registration number: {self.reg_number}\n'
              f'Maximum speed: {self.max_speed} km/h\n'
              f'Current speed: {self.cur_speed} km/h\n'
              f'Traveled distance: {self.trav_dist} km')

    def accelerate(self, change):
        self.cur_speed += change
        if self.cur_speed > self.max_speed:
            self.cur_speed = self.max_speed
        elif self.cur_speed < 0:
            self.cur_speed = 0

    def new_speed(self):
        print(f"Current speed is {self.cur_speed} km/h")

    def drive(self, hours):
        change = hours * self.cur_speed
        self.trav_dist += change


cars = []
for car_num in range(1, 11):
    race_car = Car("ABC-" + str(car_num), random.randint(100, 200), 0, 0)
    cars.append(race_car)

race_going_on = True

while race_going_on:
    for race_car in cars:
        race_car.accelerate(random.randint(-10, 15))
        race_car.drive(1)
        if race_car.trav_dist >= 10000:
            race_going_on = False
            break

leaderboard = [(car.reg_number, car.max_speed, car.cur_speed, car.trav_dist) for car in cars]
sorted_leaderboard = []
while leaderboard:
    max_dist = 0
    winning_car = None
    for car_in_leaderboard in leaderboard:
        if car_in_leaderboard[3] > max_dist:
            max_dist = car_in_leaderboard[3]
            winning_car = car_in_leaderboard
    sorted_leaderboard.append(winning_car)
    leaderboard.remove(winning_car)

print("\nRACE LEADERBOARD:\n")
for car_num, (reg_number, max_speed, cur_speed, trav_dist) in enumerate(sorted_leaderboard, start=1):
    print(f"Position {Fore.RED}{car_num}{Style.RESET_ALL}:\n"
          f" {Fore.CYAN}{reg_number}{Style.RESET_ALL},"
          f" Max speed: {Fore.GREEN}{max_speed} km/h{Style.RESET_ALL},"
          f" Current speed: {Fore.YELLOW}{cur_speed} km/h{Style.RESET_ALL},"
          f" Traveled distance: {Fore.MAGENTA}{trav_dist} km{Style.RESET_ALL}")
