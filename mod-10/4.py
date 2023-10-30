import random
from tabulate import tabulate

class Race:
    def __init__(self, name, distance, cars):
        """Initialize a race with a name, distance, and a list of cars."""
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        """Simulate one hour of the race, updating car speeds and distances."""
        for car in self.cars:
            car.random_speed_change()
            car.drive()

    def print_status(self):
        """Print the status of the race including car distances and speeds."""
        print("\nRace Status:")
        print("{:<15}{:<15}{:<15}".format("Car", "Distance (km)", "Speed (km/h)"))
        for car in self.cars:
            print("{:<15}{:<15.2f}{:<15.2f}".format(car.name, car.distance, car.speed))

    def leaderboard(self):
        """Print the race leaderboard sorted by distance traveled."""
        winning_cars = sorted(self.cars, key=lambda car: car.distance, reverse=True)

        leaderboard_data = []
        for i, car in enumerate(winning_cars, start=1):
            leaderboard_data.append([i, car.name, car.distance, car.speed])

        print("\nRACE LEADERBOARD:")
        table_headers = ["Position", "Car", "Distance (km)", "Speed (km/h)"]
        table = tabulate(leaderboard_data, headers=table_headers, tablefmt="pretty", numalign="right")
        print(table)

    def race_finished(self):
        """Check if the race has finished for all cars."""
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False

class Car:
    def __init__(self, name):
        """Initialize a car with a name, starting at 0 distance and a random speed between 60 and 120 km/h."""
        self.name = name
        self.distance = 0
        self.speed = random.uniform(60, 120)

    def random_speed_change(self):
        """Introduce random speed changes for the car."""
        self.speed += random.uniform(-5, 5)

    def drive(self):
        """Simulate the car's movement in one hour."""
        self.distance += self.speed

def main():
    car_names = ["Tesla", "Ferrari", "BMW", "Audi", "Mercedes",
                 "Lamborghini", "Porsche", "Jaguar", "Maserati", "Lexus"]

    cars = [Car(name) for name in car_names]
    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0
    while not race.race_finished():
        race.hour_passes()
        if hours % 10 == 0:
            race.print_status()
        hours += 1

    print("\nRACE FINISHED!")
    race.leaderboard()

if __name__ == "__main__":
    main()
