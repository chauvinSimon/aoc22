import pytest

from days.d6.d6 import find_start


@pytest.mark.parametrize("stream, start_expected", [
    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
    ('nppdvjthqldpwncqszvftbrmjlhg', 6),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11),
])
def test_find_marker_start(stream, start_expected):
    start = find_start(stream, size=4)
    assert start_expected == start


@pytest.mark.parametrize("stream, start_expected", [
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
    ('nppdvjthqldpwncqszvftbrmjlhg', 23),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26),
])
def test_find_msg_start(stream, start_expected):
    start = find_start(stream, size=14)
    assert start_expected == start


if __name__ == "__main__":
    pytest.main([__file__])
