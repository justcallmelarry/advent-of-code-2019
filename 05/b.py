import os
from collections import *

from utils import get_actual
from utils import *


class Halt(Exception):
    pass


def run_input(pos, l, input_=0):
    opcode = l[pos]

    if opcode == 99:
        raise Halt("found 99, exiting")

    if opcode >= 100:
        inp = str(opcode)
        while len(inp) < 5:
            inp = f"0{inp}"
        opcode = int(inp[-2:])
        pa, pb, pc = inp[:-2]
    else:
        pa, pb, pc = "", "", ""
    del pa

    if opcode in (1, 2):
        pos1 = l[pos + 1]
        pos2 = l[pos + 2]
        pos3 = l[pos + 3]
        c = l[pos1] if pc != "1" else pos1
        b = l[pos2] if pb != "1" else pos2
        l[pos3] = c + b if opcode == 1 else c * b

        if pos3 != pos:
            return pos + 4

        return l[pos3]

    if opcode == 3:
        pos1 = l[pos + 1]
        l[pos1] = input_

        if pos1 != pos:
            return pos + 2

        return l[pos1]

    if opcode == 4:
        pos1 = l[pos + 1]
        output = l[pos1] if pc != "1" else pos1
        print(f"value is {output}")

        return pos + 2

    if opcode in (5, 6):
        pos1 = l[pos + 1]
        pos2 = l[pos + 2]
        if opcode == 5:
            check = l[pos1] if pc != "1" else pos1
            if check != 0:
                l[pos] = l[pos2] if pb != "1" else pos2
                return l[pos]

        if opcode == 6:
            check = l[pos1] if pc != "1" else pos1
            if check == 0:
                l[pos] = l[pos2] if pb != "1" else pos2
                return l[pos]

        return pos + 3

    if opcode in (7, 8):
        pos1 = l[pos + 1]
        pos2 = l[pos + 2]
        pos3 = l[pos + 3]

        if opcode == 7:
            c = l[pos1] if pc != "1" else pos1
            b = l[pos2] if pb != "1" else pos2
            l[pos3] = 1 if c < b else 0

        if opcode == 8:
            c = l[pos1] if pc != "1" else pos1
            b = l[pos2] if pb != "1" else pos2
            l[pos3] = 1 if c == b else 0

        if pos3 != pos:
            return pos + 4

        return l[pos3]


if __name__ == "__main__":
    day = os.path.dirname(os.path.abspath(__file__)).rsplit("/", 1)[-1]
    _input = get_actual(day=int(day), year=2019)

    _input = ints(_input)

    try:
        pos = 0
        while True:
            pos = run_input(pos, _input, 5)
    except Halt as e:
        print(e)
