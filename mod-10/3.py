class Elevator:
    def __init__(self, bottom_floor, top_floor, elevator_id):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
        self.elevator_id = elevator_id

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator {self.elevator_id}: Going up. Floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator {self.elevator_id}: Going down. Floor {self.current_floor}")

    def go_to_floor(self, move):
        if move < self.bottom_floor or move > self.top_floor:
            return
        while self.current_floor != move:
            if self.current_floor < move:
                self.floor_up()
            else:
                self.floor_down()
        print(f"Elevator {self.elevator_id} has arrived at floor {self.current_floor}.")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor, i + 1) for i in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if 1 <= elevator_number <= len(self.elevators):
            elevator = self.elevators[elevator_number - 1]
            elevator.go_to_floor(destination_floor)
        else:
            print("Invalid elevator number. Please select a valid elevator.")

    def firealarm(self):
        print("\nThis is an emergency. Elevators are set to the bottom floor.")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)


building = Building(bottom_floor=1, top_floor=17, num_elevators=3)

building.firealarm()
