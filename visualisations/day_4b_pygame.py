import pygame

WORDSEARCH_SIZE = 50

with open('../day_4/day_4.txt') as f:
    rows = [row[:WORDSEARCH_SIZE] for row in f.read().splitlines()[:WORDSEARCH_SIZE]]

centers = []
total = 0
for x in range(len(rows) - 2):
    for y in range(len(rows[0]) - 2):
        if rows[x + 1][y + 1] == 'A':
            if (rows[x][y] == 'M' and rows[x][y + 2] == 'S' and rows[x + 2][y] == 'M' and rows[x + 2][y + 2] == 'S') or (
                rows[x][y] == 'M' and rows[x][y + 2] == 'M' and rows[x + 2][y] == 'S' and rows[x + 2][y + 2] == 'S') or (
                rows[x][y] == 'S' and rows[x][y + 2] == 'S' and rows[x + 2][y] == 'M' and rows[x + 2][y + 2] == 'M') or (
                rows[x][y] == 'S' and rows[x][y + 2] == 'M' and rows[x + 2][y] == 'S' and rows[x + 2][y + 2] == 'M'):
                total += 1
                centers.append((x + 1, y + 1))

x_mases = []
for center in centers:
    x_mases.append(center)
    x_mases.append((center[0] + 1, center[1] + 1))
    x_mases.append((center[0] - 1, center[1] - 1))
    x_mases.append((center[0] - 1, center[1] + 1))
    x_mases.append((center[0] + 1, center[1] - 1))

# Part B answer
print(total)

pygame.init()

pygame.display.set_caption('x-mas wordsearch')

screen = pygame.display.set_mode((WORDSEARCH_SIZE*12.5 + 35, WORDSEARCH_SIZE*12.5 + 35))
font = pygame.font.Font('freesansbold.ttf', 12)

clock = pygame.time.Clock()

x_mas_num = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    screen.fill("white")
    for n in range(WORDSEARCH_SIZE):
        for m in range(WORDSEARCH_SIZE):
            if (m, n) in x_mases[:x_mas_num] and rows[m][n] == 'A':
                text = font.render(rows[m][n], True, '#da2c38')
            elif (m, n) in x_mases[:x_mas_num] and rows[m][n] == 'M':
                text = font.render(rows[m][n], True, '#226f54')
            elif (m, n) in x_mases[:x_mas_num] and rows[m][n] == 'S':
                text = font.render(rows[m][n], True, '#43291f')

            else:
                text = font.render(rows[m][n], True, "grey")
            textRect = text.get_rect()
            textRect.center = ((n+2)*25 // 2, (m+2)*25 // 2)
            screen.blit(text, textRect)

    if x_mas_num < total*5:
        x_mas_num += 5
    pygame.display.flip()
    clock.tick(60)


