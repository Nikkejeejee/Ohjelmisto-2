class Elevator:
    def __init__(self, bottom_floor, top_floor, current_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = current_floor

    def go_to_floor(self, move):
        if move == self.current_floor:
            return
        if move < self.bottom_floor or move > self.top_floor:
            return
        if move > self.current_floor:
            while move > self.current_floor:
                self.floor_up()
        else:
            while move < self.current_floor:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Going up. You've arrived at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Going down. You've arrived at floor {self.current_floor}")


h = Elevator(0, 5, 0)
h.go_to_floor(5)
h.go_to_floor(0)
