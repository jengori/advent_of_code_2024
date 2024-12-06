class Lab:
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename) as f:
            self.map = [[char for char in line] for line in f.read().splitlines()]
        self.pad_with_stars()

    def pad_with_stars(self):
        for row in self.map:
            row.insert(0, "*")
            row.append("*")

        lab_width = len(self.map[0])
        self.map.insert(0, ["*"] * lab_width)
        self.map.append(["*"] * lab_width)

    def mark_as_visited(self, position: tuple):
        self.map[position[0]][position[1]] = "X"

    def count_visited(self):
        count = 0
        for row in self.map:
            count += row.count("X")
        return count

    def squares_visited(self):
        squares = []
        for i, row in enumerate(self.map):
            for j, char in enumerate(row):
                if self.map[i][j] == "X":
                    squares.append((i, j))
        return squares

    @staticmethod
    def is_obstacle(square):
        if square == "#":
            return True
        else:
            return False

    @staticmethod
    def is_outside(square):
        if square == "*":
            return True
        else:
            return False

    def clear_visited(self):
        for i, row in enumerate(self.map):
            for j, char in enumerate(row):
                if self.map[i][j] == "X":
                    self.map[i][j] = "."


class Guard:
    def __init__(self, lab: Lab):
        self.lab = lab
        self.start_position = self.get_start_position()
        self.position = self.start_position
        self.direction = "N"
        self.lab.mark_as_visited(self.position)

    def get_start_position(self):
        for i, row in enumerate(self.lab.map):
            for j, _ in enumerate(row):
                if self.lab.map[i][j] == "^":
                    return i, j

    def turn_right(self):
        directions = ["N", "E", "S", "W"]
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def step_forward(self):
        if self.direction == "N":
            self.position = self.position[0] - 1, self.position[1]
        elif self.direction == "E":
            self.position = self.position[0], self.position[1] + 1
        elif self.direction == "S":
            self.position = self.position[0] + 1, self.position[1]
        else:
            self.position = self.position[0], self.position[1] - 1

    def square_in_front(self):
        if self.direction == "N":
            return self.lab.map[self.position[0] - 1][self.position[1]]
        elif self.direction == "E":
            return self.lab.map[self.position[0]][self.position[1] + 1]
        elif self.direction == "S":
            return self.lab.map[self.position[0] + 1][self.position[1]]
        else:
            return self.lab.map[self.position[0]][self.position[1] - 1]

    def reset(self):
        self.position = self.start_position
        self.direction = "N"
        self.lab.mark_as_visited(self.position)


guard = Guard(Lab("day_6.txt"))

while True:
    square_in_front_of_guard = guard.square_in_front()
    if guard.lab.is_obstacle(square_in_front_of_guard):
        guard.turn_right()
    elif guard.lab.is_outside(square_in_front_of_guard):
        break
    else:
        guard.step_forward()
        guard.lab.mark_as_visited(guard.position)

print(guard.lab.count_visited())


places_to_try_putting_obstacles = []
squares_visited = guard.lab.squares_visited()
for i, row in enumerate(guard.lab.map):
    for j, _ in enumerate(row):
        if not(guard.lab.is_obstacle(guard.lab.map[i][j])) and (i, j) in squares_visited and not(guard.start_position == (i, j)) :
            places_to_try_putting_obstacles.append((i, j))
places_to_try_putting_obstacles = set(places_to_try_putting_obstacles)

places_that_result_in_a_loop = []


for place in places_to_try_putting_obstacles:
    guard.reset()
    guard.lab.map[place[0]][place[1]] = '#'

    visited = {"N": [], "E": [], "S": [], "W": []}


    while True:

        if guard.position in visited[guard.direction]:
            places_that_result_in_a_loop.append(place)
            break

        visited[guard.direction].append(guard.position)
        square_in_front_of_guard = guard.square_in_front()

        if guard.lab.is_obstacle(square_in_front_of_guard):
            guard.turn_right()
        elif guard.lab.is_outside(square_in_front_of_guard):
            break
        else:
            guard.step_forward()
            guard.lab.mark_as_visited(guard.position)

    guard.lab.map[place[0]][place[1]] = '.'

print(len(places_that_result_in_a_loop))
