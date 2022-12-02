from pathlib import Path
from typing import Sequence

from utils.utils import read_file


def find_max(calories: Sequence[str]) -> int:
    tmp_sum = 0
    max_sum = 0
    for cal in calories:
        if cal == '\n':
            max_sum = max(tmp_sum, max_sum)
            tmp_sum = 0
        else:
            tmp_sum += int(cal)
    return max_sum


def main():
    calories = read_file(Path('days/d1/in.txt'))
    print(f'max_sum = {find_max(calories)}')


if __name__ == '__main__':
    main()
