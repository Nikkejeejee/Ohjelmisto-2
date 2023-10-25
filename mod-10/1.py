class Elevator:
    def __init__(self, bottom_floor, top_floor, current_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = current_floor

    def go_to_floor(self):
        move = int(input("Press a floor button:  "))
        if move == self.current_floor:
            print("\nPlease press a floor button. You are at the same floor.")
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
            print(f"Going up. Floor {self.current_floor}\n")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"\nGoing down. Floor {self.current_floor}")


h = Elevator(0, 10, 0)
h.go_to_floor()
