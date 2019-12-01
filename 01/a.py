import os
import math

from utils import get_actual


def get_fuel(mass: int) -> int:
    return math.floor(mass / 3) - 2


if __name__ == '__main__':
    day = os.path.dirname(os.path.abspath(__file__)).rsplit('/', 1)[-1]
    input_list = get_actual(day=int(day), year=2019).splitlines()

    total_fuel = 0
    for mass in input_list:
        total_fuel += get_fuel(int(mass))

    print(total_fuel)
