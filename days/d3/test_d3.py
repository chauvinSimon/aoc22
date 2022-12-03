import pytest

from days.d2.d2 import points_per_tuple, points_per_letter, points_per_goal
from days.d3.d3 import find_duplicate, priority, find_groups


@pytest.mark.parametrize("rucksack, elem_expected, prio_expected", [
    ('vJrwpWtwJgWrhcsFMMfFFhFp', 'p', 16),
    ('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'L', 38),
    ('PmmdzqPrVvPwwTWBwg', 'P', 42),
    ('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'v', 22),
    ('ttgJtRGJQctTZtZT', 't', 20),
    ('CrZsJsPPZsGzwwsLwLmpwMDw', 's', 19),
])
def test_ind_rucksack(rucksack, elem_expected, prio_expected):
    elem = find_duplicate(rucksack_group=find_groups(rucksack))
    assert elem_expected == elem

    prio = priority(elem_expected)
    assert prio_expected == prio


@pytest.mark.parametrize("rucksack_group, elem_expected, prio_expected", [
    (('vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg'), 'r', 18),
    (('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw'), 'Z', 52),
])
def test_3_group_rucksacks(rucksack_group, elem_expected, prio_expected):
    elem = find_duplicate(rucksack_group=rucksack_group)
    assert elem_expected == elem

    prio = priority(elem_expected)
    assert prio_expected == prio


if __name__ == "__main__":
    pytest.main([__file__])
