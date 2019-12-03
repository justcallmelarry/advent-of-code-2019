import os
from collections import *

from utils import get_actual
from utils import *


def manhattan_dist(coords, target_coords):
    dx = abs(coords[0] - target_coords[0])
    dy = abs(coords[1] - target_coords[1])
    return abs(dx + dy)


def calc(x, y, crossings, grid, steps):
    if f"{x}:{y}" in crossings:
        grid[f"{x}:{y}"] = steps if grid.get(f"{x}:{y}") is None else grid[f"{x}:{y}"] + steps


if __name__ == "__main__":
    day = os.path.dirname(os.path.abspath(__file__)).rsplit("/", 1)[-1]
    _input = get_actual(day=int(day), year=2019).splitlines()

    table = []
    middle = (0, 0)
    for row in _input:
        table.append(row.split(","))

    grid = {}

    crossings = set(['1680:266', '-1275:-20', '1313:-1397', '1313:-898', '-1691:-273', '-1122:192', '-940:938', '1969:-811', '1680:287', '1411:0', '1310:-211', '1592:-745', '1699:-632', '1521:-632', '-1177:-574', '3317:6', '1903:-899', '3317:29', '1309:-570', '1310:-30', '1923:-817', '-1583:-491', '3317:-26', '1680:-91', '2353:-811', '-1691:-20', '-434:431', '1592:-817', '2354:-644', '1411:321', '1592:-780', '-940:976', '1310:0', '1309:-632', '-1277:-574', '1691:-745', '-1149:192', '1923:-780', '1888:-817', '1310:-204', '-1122:431', '3264:29', '1544:-1176', '1923:-644', '1411:-30', '-1149:-129', '3264:6', '1553:321', '1691:-780', '1691:-817', '-1831:-48', '3264:-26', '1087:-632', '1903:-811'])

    for i, row in enumerate(table):
        x, y = middle

        grid[f"{x}:{y}"] = "o"

        steps = 0
        for cell in row:
            if "U" in cell:
                for _ in range(int(cell[1:])):
                    steps += 1
                    x += 1
                    calc(x, y, crossings, grid, steps)

            if "D" in cell:
                for _ in range(int(cell[1:])):
                    steps += 1
                    x -= 1
                    calc(x, y, crossings, grid, steps)

            if "R" in cell:
                for _ in range(int(cell[1:])):
                    steps += 1
                    y += 1
                    calc(x, y, crossings, grid, steps)

            if "L" in cell:
                for _ in range(int(cell[1:])):
                    steps += 1
                    y -= 1
                    calc(x, y, crossings, grid, steps)

    shortest = -1
    shortest_coords = "0:0"
    for k, v in grid.items():
        if v == 'o':
            continue
        if v > 0:
            if shortest < 0:
                shortest = v
                shortest_coords = k
                continue

            if v < shortest:
                shortest = v
                shortest_coords = k

    print(shortest_coords, shortest)
