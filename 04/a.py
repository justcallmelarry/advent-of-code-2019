import os
import re
from collections import *

from utils import get_actual
from utils import *


RX = re.compile(r"(.)\1+")


def check(password):
    """
    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
    """
    if len(password) < 6:
        return

    if not RX.search(password):
        return

    last = 0
    for i in password:
        if int(i) < last:
            return
        last = int(i)

    return password


if __name__ == "__main__":
    day = os.path.dirname(os.path.abspath(__file__)).rsplit("/", 1)[-1]
    _input = get_actual(day=int(day), year=2019)

    r = _input.split("-")

    passwords = set()
    for password in range(int(r[0]), int(r[1]) + 1):
        a = check(str(password))
        if a:
            passwords.add(a)

    print(passwords)
    print(len(passwords))
