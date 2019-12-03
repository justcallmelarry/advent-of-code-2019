import os
from collections import *

from utils import get_actual
from utils import *


def calc(x, y, grid):
    grid[f"{x}:{y}"] = i if grid.get(f"{x}:{y}") in (None, i) else True


if __name__ == "__main__":
    day = os.path.dirname(os.path.abspath(__file__)).rsplit("/", 1)[-1]
    _input = get_actual(day=int(day), year=2019).splitlines()

    table = []
    middle = (0, 0)
    for row in _input:
        table.append(row.split(","))

    grid = {}

    for i, row in enumerate(table):
        x, y = middle

        grid[f"{x}:{y}"] = "o"

        for cell in row:
            if "U" in cell:
                for _ in range(int(cell[1:])):
                    x += 1
                    calc(x, y, grid)

            if "D" in cell:
                for _ in range(int(cell[1:])):
                    x -= 1
                    calc(x, y, grid)

            if "R" in cell:
                for _ in range(int(cell[1:])):
                    y += 1
                    calc(x, y, grid)

            if "L" in cell:
                for _ in range(int(cell[1:])):
                    y -= 1
                    calc(x, y, grid)

    shortest = -1
    shortest_coords = "0:0"
    crossings = set()
    for k, v in grid.items():
        if v is True:
            crossings.add(k)
            if shortest < 0:
                shortest = manhattan_dist(middle, ints(k))
                shortest_coords = k
                continue

            dist = manhattan_dist(middle, ints(k))
            if dist < shortest:
                shortest = dist
                shortest_coords = k

    print(crossings)  # print to use in the next puzzle
    print(shortest_coords, shortest)
