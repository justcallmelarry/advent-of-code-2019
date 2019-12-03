import os
from collections import *

from utils import get_actual
from utils import *


def manhattan_dist(coord, x, y):
    dx = abs(coord[0] - x)
    dy = abs(coord[1] - y)
    return abs(dx + dy)


if __name__ == "__main__":
    day = os.path.dirname(os.path.abspath(__file__)).rsplit("/", 1)[-1]
    _input = get_actual(day=int(day), year=2019).splitlines()

    table = []
    _max = 0
    up = 0
    right = 0
    down = 0
    left = 0
    for row in _input:
        table.append(row.split(','))
    for row in table:
        for cell in row:
            if 'U' in cell:
                up += int(cell[1:])
            if 'R' in cell:
                right += int(cell[1:])
            if 'D' in cell:
                down += int(cell[1:])
            if 'L' in cell:
                left += int(cell[1:])

    grid = make_grid(left + right + 2, up + down + 2, fill='.')

    ox = left + 1
    oy = up + 1
    grid[oy][ox] = 'o'

    for row in table:
        x = ox
        y = oy
        for o in row:
            if 'U' in o:
                for step in range(int(o[1:])):
                    y -= 1
                    grid[y][x] = '|' if grid[y][x] != '-' else '+'

            elif 'D' in o:
                for step in range(int(o[1:])):
                    y += 1
                    grid[y][x] = '|' if grid[y][x] != '-' else '+'

            elif 'R' in o:
                for step in range(int(o[1:])):
                    x += 1
                    grid[y][x] = '-' if grid[y][x] != '|' else '+'

            elif 'L' in o:
                for step in range(int(o[1:])):
                    x -= 1
                    grid[y][x] = '-' if grid[y][x] != '|' else '+'

    cells = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '+':
                cells.append((x, y))

    shortest = -1
    for coords in cells:
        if shortest == -1:
            shortest = manhattan_dist(coords, ox, oy)
        else:
            shortest = min(shortest, manhattan_dist(coords, ox, oy))
    print(shortest)
