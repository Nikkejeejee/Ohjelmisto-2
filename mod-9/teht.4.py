import random
from colorama import Fore, Style

class Car:
    def __init__(self, reg_number, max_speed, cur_speed, trav_dist):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.cur_speed = cur_speed
        self.trav_dist = trav_dist

    def intro(self):
        print(f'Registration number: {Fore.CYAN}{self.reg_number}{Style.RESET_ALL}\n'
              f'Maximum speed: {Fore.GREEN}{self.max_speed} km/h{Style.RESET_ALL}\n'
              f'Current speed: {Fore.YELLOW}{self.cur_speed} km/h{Style.RESET_ALL}\n'
              f'Traveled distance: {Fore.MAGENTA}{self.trav_dist} km{Style.RESET_ALL}')

    def accelerate(self, change):
        self.cur_speed += change
        if self.cur_speed > self.max_speed:
            self.cur_speed = self.max_speed
        elif self.cur_speed < 0:
            self.cur_speed = 0

    def new_speed(self):
        print(f"The current speed is {Fore.YELLOW}{self.cur_speed} km/h{Style.RESET_ALL}")

    def drive(self, hours):
        change = hours * self.cur_speed
        self.trav_dist += change

# Create a list of cars
cars = []
for i in range(10):
    race_car = Car("ABC-" + str(i + 1), random.randint(100, 200), 0, 0)
    cars.append(race_car)

rounds = 0
while True:
    rounds += 1
    if race_car.trav_dist >= 10000:
        break
    for race_car in cars:
        race_car.accelerate(random.randint(-10, 15))
        race_car.drive(1)

leaderboard = [(car.reg_number, car.max_speed, car.cur_speed, car.trav_dist) for car in cars]
leaderboard.sort(key=lambda x: x[3], reverse=True)

print("Race Leaderboard:")
for i, (reg_number, max_speed, cur_speed, trav_dist) in enumerate(leaderboard, start=1):
    print(f"Position {Fore.RED}{i}{Style.RESET_ALL}:\n"
          f" {Fore.CYAN}{reg_number}{Style.RESET_ALL},"
          f" Max speed: {Fore.GREEN}{max_speed} km/h{Style.RESET_ALL},"
          f" Current speed: {Fore.YELLOW}{cur_speed} km/h{Style.RESET_ALL},"
          f" Traveled distance: {Fore.MAGENTA}{trav_dist} km{Style.RESET_ALL}")
