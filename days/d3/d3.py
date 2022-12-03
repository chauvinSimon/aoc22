from pathlib import Path
from typing import Sequence

from utils.utils import read_file


def priority(char: str) -> int:
    uppers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']
    lowers = [c.lower() for c in uppers]
    all_priorities = [''] + lowers + uppers
    return all_priorities.index(char)


def find_groups(rucksack: str) -> Sequence[str]:
    assert rucksack
    len_rucksack = len(rucksack)
    assert len_rucksack % 2 == 0, 'len(rucksack) is not odd'
    c1 = rucksack[:len_rucksack // 2]
    c2 = rucksack[len_rucksack // 2:]
    return [c1, c2]


def find_duplicate(rucksack_group: Sequence[str]) -> str:
    # todo
    #  groups = [map(set, group) for group in groups]
    #  groups = [set.intersection(*group).pop() for group in groups]
    if len(rucksack_group) == 2:
        intersection = set(rucksack_group[0]).intersection(set(rucksack_group[1]))
    elif len(rucksack_group) == 3:
        intersection = set(rucksack_group[0]).intersection(
            set(rucksack_group[1])).intersection(set(rucksack_group[2]))
    else:
        raise ValueError(f'cannot deal with group of len {len(rucksack_group)}')

    assert len(intersection) == 1, f'not exactly one common element: {intersection}'
    return list(intersection)[0]


def chunks(lst, n):
    # https://stackoverflow.com/questions/312443/how-do-i-split-a-list-into-equally-sized-chunks
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def main():
    rucksacks = read_file(Path('days/d3/in.txt'))
    rucksacks = [rucksack.replace('\n', '') for rucksack in rucksacks]
    prio_sum_ind = sum(
        priority(find_duplicate(find_groups(rucksack)))
        for rucksack in rucksacks
    )
    print(f'prio_sum_ind = {prio_sum_ind}')

    prio_sum_3_group = sum(
        priority(find_duplicate(rucksack_group=rucksack_group))
        for rucksack_group in chunks(rucksacks, 3)
    )

    print(f'prio_sum_3_group = {prio_sum_3_group}')


if __name__ == '__main__':
    main()
