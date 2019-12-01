import os
import subprocess
import sys
from shutil import copyfile


if __name__ == "__main__":
    day = sys.argv[1]
    if os.path.isdir(day):
        sys.exit("day alreddy exists")

    os.makedirs(day)
    copyfile("base.py", os.path.join(day, "a.py"))
    subprocess.call(["ln", "-s", "utils.txt", os.path.join(day, "utils.py")])
