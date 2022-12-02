from pathlib import Path

from utils.utils import read_file

points_per_letter = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}


def points_per_tuple(my: str, other: str) -> int:
    if my == 'X':  # rock
        if other == 'A':  # rock
            return 3
        elif other == 'B':  # paper
            return 0
        elif other == 'C':  # scissors
            return 6
    elif my == 'Y':  # paper
        if other == 'A':  # rock
            return 6
        elif other == 'B':  # paper
            return 3
        elif other == 'C':  # scissors
            return 0
    elif my == 'Z':  # scissors
        if other == 'A':  # rock
            return 0
        elif other == 'B':  # paper
            return 6
        elif other == 'C':  # scissors
            return 3


def points_per_goal(other: str, goal_letter: str) -> int:
    word_from_letter = {
        'X': 'lose',
        'Y': 'draw',
        'Z': 'win',
    }
    goal_word = word_from_letter[goal_letter]
    if other == 'A':  # rock
        if goal_word == 'win':
            my = 'Y'  # paper
        elif goal_word == 'draw':
            my = 'X'  # rock
        elif goal_word == 'lose':
            my = 'Z'  # scissors
    elif other == 'B':  # paper
        if goal_word == 'win':
            my = 'Z'  # scissors
        elif goal_word == 'draw':
            my = 'Y'  # paper
        elif goal_word == 'lose':
            my = 'X'  # rock
    elif other == 'C':  # scissors
        if goal_word == 'win':
            my = 'X'  # rock
        elif goal_word == 'draw':
            my = 'Z'  # scissors
        elif goal_word == 'lose':
            my = 'Y'  # paper

    return points_per_letter[my] + points_per_tuple(my=my, other=other)


def main():
    strategy = read_file(Path('days/d2/in.txt'))
    score_1 = 0
    score_2 = 0
    for _round in strategy:
        other_action = _round[0]
        my_action = _round[2]
        score_1 += points_per_letter[my_action]
        score_1 += points_per_tuple(my=my_action, other=other_action)

        score_2 += points_per_goal(other=other_action, goal_letter=my_action)
    print(f'score_1 = {score_1}')
    print(f'score_2 = {score_2}')


if __name__ == '__main__':
    main()
