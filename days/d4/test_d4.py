import pytest

from days.d4.d4 import is_one_included, is_overlap


@pytest.mark.parametrize("s, overlap_expected, included_expected", [
    ('2-4,6-8', False, False),
    ('2-3,4-5', False, False),
    ('5-7,7-9', False, True),
    ('2-8,3-7', True, True),
    ('6-6,4-6', True, True),
    ('2-6,4-8', False, True),
])
def test_is_overlap_and_included(s, overlap_expected, included_expected):
    included = is_one_included(s)
    assert included_expected == included

    overlap = is_overlap(s)
    assert overlap_expected == overlap


if __name__ == "__main__":
    pytest.main([__file__])
