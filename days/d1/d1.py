from copy import copy
from pathlib import Path
from typing import List, Tuple

from utils.utils import read_file


def update_top_3(current_top_3, tmp_sum: int):
    top_3 = copy(current_top_3)
    assert top_3, f'empty top_3: {top_3}'
    top_3.append(tmp_sum)
    if len(top_3) > 3:
        top_3.sort()
        return top_3[1:]
    return top_3


def find_top_3(calories: List[str]) -> Tuple[int, int, int]:
    calories.append('\n')  # add break-line at the end to consider the last group
    tmp_sum = 0
    top_3 = [0, 0, 0]
    for cal in calories:
        if cal == '\n':
            top_3 = update_top_3(top_3, tmp_sum)
            tmp_sum = 0
        else:
            tmp_sum += int(cal)
    return top_3


def main():
    calories = read_file(Path('days/d1/in.txt'))
    top_3 = find_top_3(calories=calories)
    print(f'max_sum = {max(top_3)}')
    print(f'top_3_sum = {sum(top_3)}')


if __name__ == '__main__':
    main()
