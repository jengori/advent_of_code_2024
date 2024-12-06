import pygame

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


    def square_in_front(self):
        if self.direction == "N":
            return self.lab.map[self.position[0] - 1][self.position[1]]
        elif self.direction == "E":
            return self.lab.map[self.position[0]][self.position[1] + 1]
        elif self.direction == "S":
            return self.lab.map[self.position[0] + 1][self.position[1]]
        else:
            return self.lab.map[self.position[0]][self.position[1] - 1]
    
    def step_forward(self):
        if self.direction == "N":
            self.position = self.position[0] - 1, self.position[1]
        elif self.direction == "E":
            self.position = self.position[0], self.position[1] + 1
        elif self.direction == "S":
            self.position = self.position[0] + 1, self.position[1]
        else:
            self.position = self.position[0], self.position[1] - 1

    def reset(self):
        self.position = self.start_position
        self.direction = "N"
        self.lab.count_visited()
        self.lab.mark_as_visited(self.position)

my_lab = Lab("../day_6/day_6.txt")
guard = Guard(my_lab)

obstacles = []
for i, row in enumerate(guard.lab.map):
    for j, char in enumerate(row):
        if guard.lab.map[i][j] == "#":
            obstacles.append((i, j))

positions = []

while True:
    square_in_front_of_guard = guard.square_in_front()
    if guard.lab.is_obstacle(square_in_front_of_guard):
        guard.turn_right()
    elif guard.lab.is_outside(square_in_front_of_guard):
        break
    else:
        guard.step_forward()
        guard.lab.mark_as_visited(guard.position)
    positions.append(guard.position)

guard.step_forward()
guard.lab.mark_as_visited(guard.position)
positions.append(guard.position)

pygame.init()

pygame.display.set_caption('Guard Gallivant!')

screen = pygame.display.set_mode((660, 660))

clock = pygame.time.Clock()

i = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    screen.fill("gray11")

    for obstacle in obstacles:
        pygame.draw.rect(screen, "maroon1", (obstacle[1]* 5, obstacle[0]*5,
                         5, 5), width=5)

    for p in positions[0:i]:
        pygame.draw.circle(screen, "chartreuse2", (p[1] * 5 + 2.5, p[0] * 5 + 2.5), 2.5)

    if i < len(positions):
        i += 1
    pygame.display.flip()
    clock.tick(200)
