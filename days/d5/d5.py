import re
from pathlib import Path

from utils.utils import read_file


def move(state, moves, use_block: bool = False) -> bool:
    for mov in moves:
        m = re.match(
            r"move (?P<n_moves>\d+) from (?P<i_origin>\d+) to (?P<i_target>\d+)",
            mov
        )
        res = dict(m.groupdict())
        n_moves = int(res['n_moves'])
        i_origin = int(res['i_origin']) - 1
        i_target = int(res['i_target']) - 1
        tmp = []
        for _ in range(n_moves):
            tmp.append(state[i_origin][0])
            if len(state[i_origin]) == 1:
                state[i_origin] = []
            else:
                state[i_origin] = state[i_origin][1:]
        if not use_block:
            tmp = tmp[::-1]
        state[i_target] = tmp + state[i_target]

    return state


def decode_state(state_str):
    n_piles = int(state_str[-1][-1])  # index starting with 1
    state = [[] for _ in range(n_piles)]
    for s in state_str[:-1]:
        for i_pile in range(n_piles):
            _id = 1 + 4 * i_pile
            if len(s) > _id:
                letter = s[_id]
                if letter == ' ':
                    continue
                state[i_pile].append(letter)
    return state


def answer(state) -> str:
    return ''.join(s[0] for s in state)


def main():
    for i, use_block in enumerate([False, True]):
        lines = read_file(Path('days/d5/in.txt'))
        i_split = lines.index('')
        state_str = lines[:i_split]
        moves = lines[1 + i_split:]
        state = decode_state(state_str)

        print(f'answer {i}: {answer(move(state=state, moves=moves, use_block=use_block))}')


if __name__ == '__main__':
    main()
