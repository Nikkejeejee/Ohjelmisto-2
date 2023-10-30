class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Going up. Floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Going down. Floor {self.current_floor}")

    def go_to_floor(self, move):
        while self.current_floor != move:
            if self.current_floor < move:
                self.floor_up()
            else:
                self.floor_down()
        print(f"You've arrived at floor {self.current_floor}.")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            elevator = self.elevators[elevator_number]
            elevator.go_to_floor(destination_floor)
        else:
            print("Invalid elevator number. Please select a valid elevator.")


building = Building(bottom_floor=1, top_floor=10, num_elevators=2)

building.run_elevator(0, 5)
building.run_elevator(1, 8)
