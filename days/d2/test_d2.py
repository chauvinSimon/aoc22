import pytest

from days.d2.d2 import points_per_tuple, points_per_letter, points_per_goal


@pytest.mark.parametrize("_tuple, score_1_expected, score_2_expected", [
    (('A', 'Y'), 8, 4),
    (('B', 'X'), 1, 1),
    (('C', 'Z'), 6, 7),
])
def test_scores(_tuple, score_1_expected, score_2_expected):
    other, my = _tuple

    score_1 = points_per_tuple(my=my, other=other) + points_per_letter[my]
    assert score_1_expected == score_1

    score_2 = points_per_goal(goal_letter=my, other=other)
    assert score_2_expected == score_2


if __name__ == "__main__":
    pytest.main([__file__])
