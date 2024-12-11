import pygame

with open("../day_10/day_10.txt") as f:
    content = f.read().splitlines()

topological_map = []

for i, row in enumerate(content):
   topological_map.append([int(val) for val in row])

all_paths = []
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

    total_paths += len(paths)

    all_paths.append(paths)

i = 0

pygame.init()

pygame.display.set_caption('HOOF IT')

screen = pygame.display.set_mode((750, 750))

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 8)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    screen.fill("gray50")

    for n in range(i+1):
        for paths in all_paths:
            for path in paths:

                if n > 0:
                    pygame.draw.circle(screen, "chartreuse", (path[n][0] * 15 + 7.5, path[n][1] * 15 + 7.5), 4)
                    pygame.draw.line(screen, "chartreuse", (path[n-1][0] * 15 + 7.5, path[n-1][1]* 15 + 7.5),
                                     (path[n][0]*15 + 7.5, path[n][1]*15 + 7.5),1)
                else:
                    pygame.draw.circle(screen, "chartreuse", (path[n][0] * 15 + 7.5, path[n][1] * 15 + 7.5), 4)

                if n == 9:
                    pygame.draw.circle(screen, "chartreuse", (path[n][0] * 15 + 7.5, path[n][1] * 15 + 7.5), 4)
        for x in range(50):
            for y in range(50):
                text = font.render(str(topological_map[x][y]), True, "black")
                textRect = text.get_rect()
                textRect.center = (x * 15  + 6.5, y * 15 + 6.5)
                screen.blit(text, textRect)

    if i <=9:
        pygame.display.flip()
        clock.tick(1)
        if i < 9:
            i += 1
