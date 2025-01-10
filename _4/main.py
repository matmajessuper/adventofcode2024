import re
from copy import copy


def get_horizontal_reverse(lines: list) -> list:
    return [line[::-1] for line in lines]


def get_vertical(lines: list) -> list:
    vertical = zip(*lines)
    vertical = ["".join(line) for line in vertical]
    return [line[::-1] for line in vertical] + vertical


def get_diagonal(matrix):
    rows = len(matrix)
    top_left_to_bottom_right = []
    top_right_to_bottom_left = []

    # Collect diagonals from top-left to bottom-right
    for d in range(rows + max(len(row) for row in matrix) - 1):
        diagonal = []
        for row in range(rows):
            col = d - row
            if (
                0 <= col < len(matrix[row])
            ):  # Ensure col is within the current row's length
                diagonal.append(matrix[row][col])
        if diagonal:
            top_left_to_bottom_right.append(diagonal)

    # Collect diagonals from top-right to bottom-left
    for d in range(rows + max(len(row) for row in matrix) - 1):
        diagonal = []
        for row in range(rows):
            col = len(matrix[row]) - 1 - (d - row)
            if (
                0 <= col < len(matrix[row])
            ):  # Ensure col is within the current row's length
                diagonal.append(matrix[row][col])
        if diagonal:
            top_right_to_bottom_left.append(diagonal)

    f_diag = ["".join(row) for row in top_left_to_bottom_right] + [
        "".join(row) for row in top_right_to_bottom_left
    ]
    r_diag = [diag[::-1] for diag in f_diag]
    return f_diag + r_diag


def check_mas(
    top_left: str, top_right: str, bottom_right: str, bottom_left: str
) -> bool:
    if {top_left, bottom_right} == {"M", "S"} == {top_right, bottom_left}:
        return True
    return False


def main():
    with open("input.txt", "r") as f:
        content = f.readlines()
    content = [line.strip() for line in content]

    all_lines = copy(content)
    all_lines += get_horizontal_reverse(content)
    all_lines += get_vertical(content)
    all_lines += get_diagonal(content)

    counter_1 = counter_2 = 0
    for row in all_lines:
        counter_1 += len(re.findall("XMAS", row))

    for index, row in enumerate(content):
        if 0 < index < len(content) - 1:
            a_indexes = [
                i
                for i, letter in enumerate(row)
                if letter == "A" and 0 < i < len(row) - 1
            ]
            counter_2 += len([
                i
                for i in a_indexes
                if check_mas(
                    content[index - 1][i - 1],
                    content[index - 1][i + 1],
                    content[index + 1][i + 1],
                    content[index + 1][i - 1],
                )
            ])
    return f"{counter_1} {counter_2}"


if __name__ == "__main__":
    print(main())
