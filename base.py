import os

from utils import get_actual


if __name__ == '__main__':
    day = os.path.dirname(os.path.abspath(__file__)).rsplit('/', 1)[-1]
    input_list = get_actual(day=int(day), year=2019).splitlines()

    # code here
