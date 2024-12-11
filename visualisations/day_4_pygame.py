import pygame
import re

WORDSEARCH_SIZE = 50

with open('../day_4/day_4.txt') as f:
    rows = [row[:WORDSEARCH_SIZE] for row in f.read().splitlines()[:WORDSEARCH_SIZE]]

columns = []
for n in range(len(rows)):
    column = ""
    for row in rows:
        column += row[n]
    columns.append(column)

def find_xmas(r):
    indices = []
    for x in range(len(r)):
        xmas_matches = re.finditer('XMAS', r[x])
        xmas_pos = [match.span() for match in xmas_matches]
        samx_matches = re.finditer('SAMX', r[x])
        samx_pos = [match.span() for match in samx_matches]
        for pos in xmas_pos:
            for n in range(pos[0], pos[1]):
                indices.append((x, n))
        for pos in samx_pos:
            for n in range(pos[0], pos[1]):
                indices.append((x, n))
    return indices

row_indices = find_xmas(rows)
column_indices = find_xmas(columns)

def get_diagonals(r: list):
    diagonals = []
    for n in range(len(r[0]) - 3):
        diagonal = ""
        for m in range(len(r) - n):
            diagonal += r[m][n + m]
        diagonals.append({((0, n), (len(r) - n, len(r[0]))): diagonal})

    for n in range(1, len(r) - 3):
        diagonal = ""
        for m in range(len(r[0]) - n):
            diagonal += r[m + n][m]
        diagonals.insert(0, {((n, 0), (len(r), len(r[0])-n)): diagonal})

    return diagonals


diagonals = get_diagonals(rows)
rows_reversed = [row[::-1] for row in rows]
other_diagonals = get_diagonals(rows_reversed)
other_diagonals = other_diagonals.__reversed__()

diagonal_indices = []

for diagonal in diagonals:
        s = "".join(diagonal.values())
        xmas_matches = re.finditer('XMAS', s)
        xmas_pos = [match.span() for match in xmas_matches]
        samx_matches = re.finditer('SAMX', s)
        samx_pos = [match.span() for match in samx_matches]

        for pos in xmas_pos:
            for n in range(4):
                diagonal_indices.append((list(diagonal.keys())[0][0][0] + pos[0] + n, list(diagonal.keys())[0][0][1] + pos[0] + n))

other_diagonal_indices = []
for diagonal in other_diagonals:
        s = "".join(diagonal.values())
        xmas_matches = re.finditer('XMAS', s)
        xmas_pos = [match.span() for match in xmas_matches]
        samx_matches = re.finditer('SAMX', s)
        samx_pos = [match.span() for match in samx_matches]

        for pos in xmas_pos:
            for n in range(4):
                other_diagonal_indices.append((list(diagonal.keys())[0][0][0] + pos[0] + n, len(rows) - 1 - (list(diagonal.keys())[0][0][1] + pos[0] + n)))

pygame.init()

pygame.display.set_caption('xmas wordsearch')

screen = pygame.display.set_mode((WORDSEARCH_SIZE*12.5 + 35, WORDSEARCH_SIZE*12.5 + 35))
font = pygame.font.Font('freesansbold.ttf', 12)

clock = pygame.time.Clock()

row_word_num = 0
col_word_num = 0
diag_word_num = 0
otherdiag_word_num = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    screen.fill("white")
    for n in range(WORDSEARCH_SIZE):
        for m in range(WORDSEARCH_SIZE):
            if (m, n) in other_diagonal_indices[0: otherdiag_word_num]:
                text = font.render(rows[m][n], True, "#43291f")
            elif (m, n) in diagonal_indices[0: diag_word_num]:
                text = font.render(rows[m][n], True, "deeppink")
            elif (n, m) in column_indices[0:col_word_num]:
                text = font.render(rows[m][n], True, "#226f54")
            elif (m, n) in row_indices[0:row_word_num]:
                text = font.render(rows[m][n], True, "#da2c38")
            else:
                text = font.render(rows[m][n], True, "grey")
            textRect = text.get_rect()
            textRect.center = ((n+2)*25 // 2, (m+2)*25 // 2)
            screen.blit(text, textRect)

    pygame.display.flip()
    clock.tick(100)

    if row_word_num < len(row_indices):
        row_word_num += 1
    elif col_word_num < len(column_indices):
        col_word_num += 1
    elif diag_word_num < len(diagonal_indices):
        diag_word_num += 1
    elif otherdiag_word_num < len(other_diagonal_indices):
        otherdiag_word_num += 1
