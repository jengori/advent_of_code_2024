import re
from sympy import symbols, Eq, solve

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Button:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Machine:
    def __init__(self, a:Button, b:Button, prize_location:Point):
        self.a = a
        self.b = b
        self.claw_location = Point(0, 0)
        self.prize_location = prize_location

    def get_num_tokens(self):
        n, m = symbols('x y')

        eq1 = Eq(self.a.x * n + self.b.x * m, self.prize_location.x)
        eq2 = Eq(self.a.y * n + self.b.y * m, self.prize_location.y)

        solution = solve((eq1, eq2), (n, m))

        if solution[n].is_integer and solution[m].is_integer:
            cost = 3 * solution[n] + solution[m]
            return cost
        return 0

    def update_prize_location(self, n):
        self.prize_location.x += n
        self.prize_location.y += n


with open("day_13.txt") as f:
    text = [line.strip() for line in f.readlines() if line.strip() != '']

machines = []

for i in range(0, len(text), 3):
    button_a_vals = [int(n) for n in re.findall(r'\d+', text[i])]
    button_b_vals = [int(n) for n in re.findall(r'\d+', text[i+1])]
    prize_vals = [int(n) for n in re.findall(r'\d+', text[i+2])]
    machine = Machine(Button(button_a_vals[0], button_a_vals[1]), Button(button_b_vals[0], button_b_vals[1]),
                      Point(prize_vals[0], prize_vals[1]))
    machines.append(machine)

total_cost_part_a = 0

for machine in machines:
    total_cost_part_a += machine.get_num_tokens()

print(total_cost_part_a)

total_cost_part_b = 0

for machine in machines:
    machine.update_prize_location(10000000000000)
    total_cost_part_b += machine.get_num_tokens()

print(total_cost_part_b)
