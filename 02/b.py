import os

from utils import get_actual, ints


def run_input(l):
    pos = 0
    while True:
        opcode = l[pos]

        if opcode == 99:
            return

        pos1 = l[pos + 1]
        pos2 = l[pos + 2]
        pos3 = l[pos + 3]

        if opcode == 1:
            l[pos3] = l[pos1] + l[pos2]

        if opcode == 2:
            l[pos3] = l[pos1] * l[pos2]

        pos += 4


if __name__ == "__main__":
    day = os.path.dirname(os.path.abspath(__file__)).rsplit("/", 1)[-1]
    input_list = get_actual(day=int(day), year=2019)

    int_list = ints(input_list)
    target = 19690720

    for x in range(100):
        for y in range(100):
            solution = 0

            new_list = int_list.copy()
            new_list[1] = x
            new_list[2] = y

            run_input(new_list)

            solution = new_list[0]

            if solution == target:
                break
        if solution == target:
            break

    print(new_list[0], 100 * x + y)
