class Elevator:
    def __init__(self, bottom_floor, top_floor, current_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = current_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Going up. Floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Going down. Floor {self.current_floor}")

    def go_to_floor(self, move):
        if move < self.bottom_floor or move > self.top_floor:
            return
        while self.current_floor != move:
            if self.current_floor < move:
                self.floor_up()
            else:
                self.floor_down()
        print(f"You've arrived at floor {self.current_floor}.")


h = Elevator(1, 10, 0)
h.go_to_floor(5)
h.go_to_floor(1)
