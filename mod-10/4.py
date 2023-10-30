import random
from tabulate import tabulate

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.random_speed_change()
            car.drive()

    def print_status(self, hours):
        if hours > 0:
            print(f"\nRace Status after {hours} hours:")
        else:
            print("\nInitial Race Status:")
        print("{:<15}{:<15}{:<15}".format("---Car---", "Distance (km)", "Speed (km/h)"))
        for car in self.cars:
            print("{:<15}{:<15.2f}{:<15.2f}".format(car.name, car.distance, car.speed))

    def leaderboard(self):
        winning_cars = sorted(self.cars, key=lambda car: car.distance, reverse=True)

        leaderboard_data = []
        for i, car in enumerate(winning_cars, start=1):
            leaderboard_data.append([i, car.name, f'{car.distance:.2f}', f'{car.speed:.2f}'])

        print("\nRACE LEADERBOARD:")
        table_headers = ["Position", "Car", "Distance (km)", "Speed (km/h)"]
        table = tabulate(leaderboard_data, headers=table_headers, tablefmt="pretty", numalign="right")
        print(table)

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False

class Car:
    def __init__(self, name):
        self.name = name
        self.distance = 0
        self.speed = random.uniform(60, 120)

    def random_speed_change(self):
        self.speed += random.uniform(-5, 5)

    def drive(self):
        self.distance += self.speed

def main():
    car_names = ["Tesla", "Ferrari", "BMW", "Audi", "Mercedes",
                 "Lamborghini", "Porsche", "Jaguar", "Maserati", "Lexus"]

    cars = [Car(name) for name in car_names]
    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0
    while not race.race_finished():
        if hours % 10 == 0:
            race.print_status(hours if hours > 0 else 0)
        race.hour_passes()
        hours += 1

    print("\n\U0001F6D1 RACE FINISHED!🏎️💨")
    race.leaderboard()

if __name__ == "__main__":
    main()
