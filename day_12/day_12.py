from collections import defaultdict

def merge_common(lists):
    neigh = defaultdict(set)
    visited = set()
    for each in lists:
        for item in each:
            neigh[item].update(each)

    def comp(node, neigh = neigh, visited = visited, vis = visited.add):
        nodes = set([node])
        next_node = nodes.pop
        while nodes:
            node = next_node()
            vis(node)
            nodes |= neigh[node] - visited
            yield node
    for node in neigh:
        if node not in visited:
            yield sorted(comp(node))


def get_neighbors(pos: tuple):
    return [(pos[0], pos[1] - 1), (pos[0], pos[1] + 1), (pos[0] - 1, pos[1]), (pos[0] + 1, pos[1])]


with open('day_12.txt') as f:
    plots = [[x for x in row] for row in f.read().splitlines()]

for row in plots:
    row.insert(0, "*")
    row.append("*")

plot_width = len(plots[0])
plots.insert(0, ["*"] * plot_width)
plots.append(["*"] * plot_width)

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plots_dict = {letter: [] for letter in letters}
for i, row in enumerate(plots):
    for j, square in enumerate(row):
        if plots[i][j] != "*":
            plots_dict[plots[i][j]].append((i, j))

for letter in letters:
    if len(plots_dict[letter]) == 0:
        del plots_dict[letter]

regions = []
for key in plots_dict.keys():
    key_regions = []

    for location in plots_dict[key]:
        neighbors = get_neighbors(location)
        neighbours_with_same_plot_letter = []
        for neighbor in neighbors:
            if plots[location[0]][location[1]] == plots[neighbor[0]][neighbor[1]] and neighbor in plots_dict[key]:
                neighbours_with_same_plot_letter.append(neighbor)
        neighbours_with_same_plot_letter.append(location)

        key_regions.append(neighbours_with_same_plot_letter)

    key_regions = list(merge_common(key_regions))

    for region in key_regions:
        regions.append(region)

total_price = 0

for region in regions:
    area = len(region)
    perimeter = 0
    for location in region:
        neighbors = get_neighbors(location)
        count = 0
        for neighbor in neighbors:
            if neighbor in region:
                count += 1
        perimeter += 4 - count
    total_price += area * perimeter

print(total_price)
