import random

class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def drive(self, hours):
        self.distance += self.speed * hours

    def __str__(self):
        return f"{self.name}: {self.distance:.2f} km"

class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance  # in kilometres
        self.car_list = car_list

    def hour_passes(self):
        for car in self.car_list:
            car.drive(1)
            car.speed += random.uniform(-5, 5)

    def print_status(self):
        print(f"Race: {self.name}")
        print(f"Distance: {self.distance} km.")
        for car in self.car_list:
            print(car)
        print()

    def race_finished(self):
        for car in self.car_list:
            if car.distance >= self.distance:
                return True
        return False

cars = [Car(f"Car {i}", random.uniform(150, 200)) for i in range(1, 11)]

grand_derby = Race("Grand Demolition Derby", 8000, cars)

hours = 0
while not grand_derby.race_finished():
    if hours % 10 == 0:
        grand_derby.print_status()
    grand_derby.hour_passes()
    hours += 1

# Print the final status of the race
grand_derby.print_status()
print("The race has finished!")
