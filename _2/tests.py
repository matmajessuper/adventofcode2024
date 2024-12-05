import pytest

from main import check_conditions


def test_check_conditions():
    diffs = [1, 2, 3, 4, 5]  # difference is bigger then 3
    assert not check_conditions(diffs)

    diffs = [0, 2, 3, 3, 1]  # difference is smaller then _1
    assert not check_conditions(diffs)

    diffs = [1, 2, 3, -1, -2]  # positive and negative mixed
    assert not check_conditions(diffs)

    diffs = [-1, -3, -2, -3, -1]  # all negative with proper decline
    assert check_conditions(diffs)

    diffs = [1, 3, 2, 3, 1]  # all positive with proper incline
    assert check_conditions(diffs)
