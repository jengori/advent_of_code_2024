import re

with open('day_4.txt') as f:
    rows = f.read().splitlines()

columns = []
for n in range(len(rows)):
    column = ""
    for row in rows:
        column += row[n]
    columns.append(column)

diagonals = []

def get_diagonals(r: list):
    for n in range(len(r[0]) - 3):
        diagonal = ""
        for m in range(len(r) - n):
            diagonal += r[m][n + m]
        diagonals.append(diagonal)

    for n in range(1, len(r) - 3):
        diagonal = ""
        for m in range(len(r[0]) - n):
            diagonal += r[m + n][m]
        diagonals.append(diagonal)

get_diagonals(rows)
rows_reversed = [row[::-1] for row in rows]
get_diagonals(rows_reversed)

def find_xmas(r):
    n_matches = 0
    for x in r:
        xmas_matches = re.findall('XMAS', x)
        n_matches += len(xmas_matches)
        samx_matches = re.findall('SAMX', x)
        n_matches += len(samx_matches)
    return n_matches

total = 0
total += find_xmas(rows)
total += find_xmas(columns)
total += find_xmas(diagonals)

# Part A answer
print(total)

total = 0
for x in range(len(rows) - 2):
    for y in range(len(rows[0]) - 2):
        if rows[x + 1][y + 1] == 'A':
            if (rows[x][y] == 'M' and rows[x][y + 2] == 'S' and rows[x + 2][y] == 'M' and rows[x + 2][y + 2] == 'S') or (
                rows[x][y] == 'M' and rows[x][y + 2] == 'M' and rows[x + 2][y] == 'S' and rows[x + 2][y + 2] == 'S') or (
                rows[x][y] == 'S' and rows[x][y + 2] == 'S' and rows[x + 2][y] == 'M' and rows[x + 2][y + 2] == 'M') or (
                rows[x][y] == 'S' and rows[x][y + 2] == 'M' and rows[x + 2][y] == 'S' and rows[x + 2][y + 2] == 'M'):
                total += 1

# Part B answer
print(total)