import pytest

from days.d1.d1 import find_max


@pytest.mark.parametrize("calories, max_expected", [
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
     ], 24000),
])
def test_scores(calories, max_expected):
    _max = find_max(calories=calories)
    assert max_expected == _max


if __name__ == "__main__":
    pytest.main([__file__])
