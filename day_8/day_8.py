from itertools import combinations

with open('day_8.txt') as f:
    antenna_map = [[char for char in line] for line in f.read().splitlines()]

map_width = len(antenna_map[0])
map_height = len(antenna_map)

antenna_dict = {}
antenna_map_copy_a = [row.copy() for row in antenna_map]
antenna_map_copy_b = [row.copy() for row in antenna_map]

for i, row in enumerate(antenna_map):
    for j, char in enumerate(row):
        if char != '.':
            if char in antenna_dict.keys():
                antenna_dict[char].append((i, j))
            else:
                antenna_dict[char] = [(i, j)]

for symbol in antenna_dict.keys():
    pairs = list(combinations(antenna_dict[symbol], 2))

    for pair in pairs:
        diff = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])

        line_1 = []
        x = pair[0][0] + diff[0]
        y = pair[0][1] + diff[1]

        while 0 <= x < map_height and 0 <= y < map_width:
            line_1.append((x, y))
            x += diff[0]
            y += diff[1]

        line_2 = []
        x = pair[0][0] - diff[0]
        y = pair[0][1] - diff[1]

        while 0 <= x < map_height and 0 <= y < map_width:
            line_2.append((x, y))
            x -= diff[0]
            y -= diff[1]

        for point in line_1:
            antenna_map_copy_b[point[0]][point[1]] = '#'
            if (point[0] - pair[0][0]) == 2*(point[0] - pair[1][0]):
                antenna_map_copy_a[point[0]][point[1]] = '#'

        for point in line_2:
            antenna_map_copy_b[point[0]][point[1]] = '#'
            if 2*(point[0] - pair[0][0]) == (point[0] - pair[1][0]):
                antenna_map_copy_a[point[0]][point[1]] = '#'

anti_nodes_count_a = 0
anti_nodes_count_b = 0

for row in antenna_map_copy_a:
    for char in row:
        if char == '#':
            anti_nodes_count_a += 1

print(anti_nodes_count_a)

for row in antenna_map_copy_b:
    for char in row:
        if char == '#':
            anti_nodes_count_b += 1

print(anti_nodes_count_b)
