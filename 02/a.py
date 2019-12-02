import os

from utils import get_actual, ints


if __name__ == "__main__":
    day = os.path.dirname(os.path.abspath(__file__)).rsplit("/", 1)[-1]
    input_list = get_actual(day=int(day), year=2019)

    int_list = ints(input_list)

    int_list[1] = 12
    int_list[2] = 2

    pos = 0
    while True:
        opcode = int_list[pos]

        if opcode == 99:
            break

        pos1 = int_list[pos + 1]
        pos2 = int_list[pos + 2]
        pos3 = int_list[pos + 3]

        if opcode == 1:
            int_list[pos3] = int_list[pos1] + int_list[pos2]

        if opcode == 2:
            int_list[pos3] = int_list[pos1] * int_list[pos2]

        pos += 4

    print(int_list[0])
