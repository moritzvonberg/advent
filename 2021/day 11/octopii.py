FLASH_THRESHOLD_OFFSET = 9
FIELD_SIZE = 10

# I implemented this by comparing ints to the amount of steps to avoid having to increment them

class OctopusGame():
    def __init__(self, field) -> None:
        self.field = field
        self.flashed_coords = set()
        self.step_index = 0
        self.flashes = 0

    def get_neighbor_coords(self, coord, size=FIELD_SIZE):
        res = []
        x, y = coord
        for x_coord in range(max(0, x - 1), min(size, x + 2)):
            for y_coord in range(max(0, y - 1), min(size, y + 2)):
                if x != x_coord or y != y_coord:
                    res.append((x_coord, y_coord))
        return res

    def step(self, count=1):
        for _ in range(count):
            self.step_index += 1

            for y, row in enumerate(self.field):
                for x, energy_val in enumerate(row):
                    if energy_val > FLASH_THRESHOLD_OFFSET - self.step_index:
                        self.flash((x, y))

            for x, y in self.flashed_coords:
                self.field[y][x] = -self.step_index
            self.flashed_coords.clear()

    def flash(self, coord):
        if coord in self.flashed_coords:
            return

        self.flashed_coords.add(coord)
        self.flashes += 1
        
        for x, y in self.get_neighbor_coords(coord):
            self.field[y][x] += 1
            if self.field[y][x] > FLASH_THRESHOLD_OFFSET - self.step_index:
                self.flash((x, y))

    def is_synced(self):
        initial_val = self.field[0][0]
        for line in self.field:
            for num in line:
                if num != initial_val:
                    return False
        return True

    
    def __str__(self):
        res = list()
        res.append(f"Game@Turn{self.step_index}\n")
        for line in self.field:
            res.append(str([x + self.step_index for x in line]) + '\n')
        return "".join(res)

game = None
tester = None

with open("2021/day 11/input.txt", 'r') as infile:
    field = [[int(num) for num in line if num in "0123456789"] for line in infile.readlines()]
    game = OctopusGame(field)

game.step(100)
print(game.flashes) # solution 1
while not game.is_synced():
    game.step()
print(game.step_index) # solution 2 (assuming solution is not less than 100 steps)



