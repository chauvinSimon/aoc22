from pathlib import Path

from utils.utils import read_file


def find_start(steam: str, size: int) -> int:
    for i in range(len(steam) - size):
        # print(steam[i:i+4])
        if len(set(steam[i:i + size])) == size:
            return i + size


def answer(state) -> str:
    return ''.join(s[0] for s in state)


def main():
    stream = read_file(Path('days/d6/in.txt'))[0]
    print(f'answer: {find_start(stream, size=4)}')
    print(f'answer: {find_start(stream, size=14)}')


if __name__ == '__main__':
    main()
