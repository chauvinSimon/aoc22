import pytest

from days.d1.d1 import find_top_3


@pytest.mark.parametrize("calories, top_3_expected", [
    ([
         '1000\n',
         '2000\n',
         '3000\n',
         '\n',
         '4000\n',
         '\n',
         '5000\n',
         '6000\n',
         '\n',
         '7000\n',
         '8000\n',
         '9000\n',
         '\n',
         '10000\n',
     ], [10000, 11000, 24000]),
])
def test_scores(calories, top_3_expected):
    top_3 = find_top_3(calories=calories)
    assert top_3_expected == top_3


if __name__ == "__main__":
    pytest.main([__file__])
