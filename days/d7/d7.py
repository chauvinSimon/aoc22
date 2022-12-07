import re
from functools import reduce
from pathlib import Path
from typing import Dict, List

from utils.utils import read_file


def deep_get(dictionary, *keys):
    return reduce(
        lambda d, key: d.get(key)
        if d else None,
        keys,
        dictionary
    )


def find_tree(terminal: List[str]) -> Dict:
    tree = {'/': {}}
    i = 0
    current_path = []
    while i < len(terminal):
        line = terminal[i]
        if '$ cd ' in line:
            new_folder = line[5:]
            if new_folder == '/':
                current_path = [new_folder]
            elif new_folder == '..':
                current_path = current_path[:-1]
            else:
                current_path.append(new_folder)
            # print(f'now in [{current_path}]')
            i = i + 1
        elif '$ ls' == line:
            while i < len(terminal) - 1:
                i = i + 1
                line = terminal[i]
                if line[0] == '$':
                    break
                # print(f'in {current_path}: {line}')
                if 'dir ' in line:
                    name = line[4:]
                    if name not in deep_get(tree, *current_path):
                        deep_get(tree, *current_path)[name] = {}
                else:
                    m = re.match(r"(?P<size>\d+) (?P<name>\w.*)", line)
                    match = m.groupdict()
                    # print(f"{match['name']}: {match['size']}")
                    deep_get(tree, *current_path)[match['name']] = int(match['size'])
        else:
            i = i + 1

    # import json
    # print(json.dumps(tree, sort_keys=True, indent=4))

    return tree


def find_dir_size(_d) -> int:
    if isinstance(_d, int):
        return _d
    return sum(find_dir_size(v) for v in _d.values())


def find_dir_sizes(tree):
    sizes = {}

    def examine_tree(_tree):
        for k, v in _tree.items():
            if isinstance(v, dict):
                dir_size = find_dir_size(v)
                # print(f'dir_size of [{k}] = {dir_size}')
                sizes[k] = dir_size
                examine_tree(v)

    examine_tree(tree)
    # print(sizes)
    return sizes


def answer(dir_and_sizes) -> int:
    return sum(s for s in dir_and_sizes.values() if s <= 100000)


def main():
    terminal = read_file(Path('days/d7/in.txt'))
    tree = find_tree(terminal=terminal)
    dir_sizes = find_dir_sizes(tree)
    print(f'answer: {answer(dir_sizes)}')


if __name__ == '__main__':
    main()
