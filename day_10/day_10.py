with open("day_10.txt") as f:
    content = f.read().splitlines()

topological_map = []

for i, row in enumerate(content):
   topological_map.append([int(val) for val in row])

graph = {}
for i, row in enumerate(topological_map):
    for j, val in enumerate(row):
        graph[(i, j)] = []
        l = (i, j - 1)
        r = (i, j + 1)
        u = (i - 1, j)
        d = (i + 1, j)

        for direction in [l, r, u, d]:
            if 0 <= direction[0] < len(topological_map[0]) and 0 <= direction[1] < len(topological_map) and topological_map[direction[0]][direction[1]] == val + 1:
                graph[(i, j)].append(direction)

removed = True
while removed:
    points_to_remove = [key for key in graph.keys() if len(graph[key]) == 0 and topological_map[key[0]][key[1]] != 9]
    if len(points_to_remove) == 0:
        removed = False
    else:
        for point in points_to_remove:
            del graph[point]
            for key in graph.keys():
                if point in graph[key]:
                    graph[key].remove(point)

trailheads = []
for i, row in enumerate(topological_map):
    for j, val in enumerate(row):
        if val == 0 and len(graph[(i, j)]) > 0:
            trailheads.append((i, j))

total_paths = 0
total_score = 0

for trailhead in trailheads:
    paths = []
    for point in graph[trailhead]:
        paths.append([trailhead, point])

    for _ in range(8):
        for path in paths:
                if len(graph[path[-1]]) == 1:
                    path.append(graph[path[-1]][0])
                elif len(graph[path[-1]]) == 2:
                    paths.append(path.copy())
                    path.append(graph[path[-1]][0])
                    paths[-1].append(graph[path[-2]][1])
                elif len(graph[path[-1]]) == 3:
                    paths.append(path.copy())
                    paths.append(path.copy())
                    path.append(graph[path[-1]][0])
                    paths[-2].append(graph[path[-2]][1])
                    paths[-1].append(graph[path[-2]][2])

    score = len(set([path[-1] for path in paths]))
    total_score += score
    total_paths += len(paths)

    for path in paths:
        print(path)

print(total_score)
print(total_paths)