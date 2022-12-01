from pathlib import Path

from utils.utils import read_file


def main():
    calories_list = read_file(Path('days/d1/in.txt'))
    tmp_sum = 0
    max_sum = 0
    for cal in calories_list:
        if cal == '\n':
            max_sum = max(tmp_sum, max_sum)
            tmp_sum = 0
        else:
            tmp_sum += int(cal)

    print(f'max_sum = {max_sum}')

if __name__ == '__main__':
    main()
