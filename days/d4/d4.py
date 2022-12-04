from pathlib import Path

from utils.utils import read_file


def are_indices_overlapping(i11: int, i12: int, i21: int, i22: int) -> bool:
    return (i11 <= i21 and i22 <= i12) or (i21 <= i11 and i12 <= i22)


def are_indices_included(i11: int, i12: int, i21: int, i22: int) -> bool:
    return (i11 <= i21 <= i12) or (i21 <= i11 <= i22)


def split_assignment(a: str):
    return [int(e) for e in a.split('-')]


def is_one_included(s: str) -> bool:
    i1, i2 = (split_assignment(e) for e in s.split(','))
    return are_indices_included(*i1, *i2)


def is_overlap(s: str) -> bool:
    i1, i2 = (split_assignment(e) for e in s.split(','))
    return are_indices_overlapping(*i1, *i2)


def main():
    assignment_pairs = read_file(Path('days/d4/in.txt'))

    included = [is_one_included(p) for p in assignment_pairs]
    print(f'included: {sum(included)}')

    overlaps = [is_overlap(p) for p in assignment_pairs]
    print(f'overlaps: {sum(overlaps)}')


if __name__ == '__main__':
    main()
