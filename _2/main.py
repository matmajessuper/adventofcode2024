from itertools import combinations

import numpy as np


def check_conditions(diffs: list):
    return all((1 <= abs(diff) <= 3 for diff in diffs)) and \
        (all((diff < 0 for diff in diffs)) or all((diff > 0 for diff in diffs)))


def main():
    safe_1 = 0
    safe_2 = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            numbers = [int(number) for number in line.split()]
            diffs = np.diff(numbers)
            if check_conditions(diffs):
                safe_1 += 1
            if any((check_conditions(np.diff(combination)) for combination in combinations(numbers, len(numbers) - 1))):
                safe_2 += 1
                print(line)
    return f'{safe_1} {safe_2}'


if __name__ == '__main__':
    print(main())
