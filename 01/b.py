import os
import math

from utils import get_actual


def get_fuel(mass: int) -> int:
    return max(math.floor(mass / 3) - 2, 0)


if __name__ == "__main__":
    day = os.path.dirname(os.path.abspath(__file__)).rsplit("/", 1)[-1]
    input_list = get_actual(day=int(day), year=2019).splitlines()

    total_fuel = 0
    for mass in input_list:
        empty = False
        while not empty:
            fuel = get_fuel(int(mass))
            if fuel == 0:
                empty = True
            total_fuel += fuel
            mass = fuel

    print(total_fuel)
