import pytest

from days.d7.d7 import find_dir_sizes, find_tree


@pytest.mark.parametrize("terminal, tree_expected", [
    ([
         '$ cd /',
         '$ ls',
         'dir a',
         '14848514 b.txt',
         '8504156 c.dat',
         'dir d',
         '$ cd a',
         '$ ls',
         'dir e',
         '29116 f',
         '2557 g',
         '62596 h.lst',
         '$ cd e',
         '$ ls',
         '584 i',
         '$ cd ..',
         '$ cd ..',
         '$ cd d',
         '$ ls',
         '4060174 j',
         '8033020 d.log',
         '5626152 d.ext',
         '7214296 k',
     ],
     {
         '/': {
             'a': {
                 'e': {
                     'i': 584
                 },
                 'f': 29116,
                 'g': 2557,
                 'h.lst': 62596,
             },
             'b.txt': 14848514,
             'c.dat': 8504156,
             'd': {
                 'j': 4060174,
                 'd.log': 8033020,
                 'd.ext': 5626152,
                 'k': 7214296,
             },
         }
     }),
])
def test_find_tree(terminal, tree_expected):
    tree = find_tree(terminal)
    assert tree_expected == tree


@pytest.mark.parametrize("tree, dir_and_size_expected", [
    ({
         '/': {
             'a': {
                 'e': {
                     'i': 584
                 },
                 'f': 29116,
                 'g': 2557,
                 'h.lst': 62596,
             },
             'b.txt': 14848514,
             'c.dat': 8504156,
             'd': {
                 'j': 4060174,
                 'd.log': 8033020,
                 'd.ext': 5626152,
                 'k': 7214296,
             },
         }
     },
     [
         94853,  # 'a'
         584,  # 'e'
         24933642,  # 'd'
         48381165  # '/'
     ])
])
def test_find_dir_lighter(tree, dir_and_size_expected):
    dir_and_size = find_dir_sizes(tree)
    assert sorted(dir_and_size_expected) == sorted(dir_and_size)


if __name__ == "__main__":
    pytest.main([__file__])
