import pytest

from days.d5.d5 import decode_state, move


@pytest.mark.parametrize("state_str, state_expected", [
    ([
         '    [D]    ',
         '[N] [C]    ',
         '[Z] [M] [P]',
         ' 1   2   3',
     ],
     [
         ['N', 'Z'],
         ['D', 'C', 'M'],
         ['P'],
     ]),
])
def test_state_decoding(state_str, state_expected):
    state = decode_state(state_str)
    assert state_expected == state


@pytest.mark.parametrize("state, moves, end_state_expected", [
    ([
         ['N', 'Z'],
         ['D', 'C', 'M'],
         ['P'],
     ], [
         'move 1 from 2 to 1',
         'move 3 from 1 to 3',
         'move 2 from 2 to 1',
         'move 1 from 1 to 2',
     ], [
         ['C'],
         ['M'],
         ['Z', 'N', 'D', 'P'],
     ]),
])
def test_moves(state, moves, end_state_expected):
    end_state = move(state, moves)
    assert end_state_expected == end_state


@pytest.mark.parametrize("state, moves, end_state_expected", [
    ([
         ['N', 'Z'],
         ['D', 'C', 'M'],
         ['P'],
     ], [
         'move 1 from 2 to 1',
         'move 3 from 1 to 3',
         'move 2 from 2 to 1',
         'move 1 from 1 to 2',
     ], [
         ['M'],
         ['C'],
         ['D', 'N', 'Z', 'P'],
     ]),
])
def test_moves_block(state, moves, end_state_expected):
    end_state = move(state, moves, use_block=True)
    assert end_state_expected == end_state


if __name__ == "__main__":
    pytest.main([__file__])
