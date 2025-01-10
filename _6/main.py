import numpy as np


class Direction:
    def __init__(self):
        self.directions = ["up", "right", "down", "left"]
        self.current_index = 0

    def current_direction(self):
        """Returns the current direction."""
        return self.directions[self.current_index]

    def change_direction(self):
        """Cycles to the next direction in the order: up -> right -> down -> left -> up."""
        self.current_index = (self.current_index + 1) % len(self.directions)


def go_until_obstacle(line: list, start_index: int) -> (int, int, bool):
    for i in range(start_index+1, len(line)):
        if line[i] == '#':
            return i - 1 - start_index, i-1, False
    return i - start_index, i, True


def find_start(map_list: list) -> (int, int):
    for x in range(len(map_list)):
        for y in range(len(map_list[0])):
            if map_list[x][y] == '^':
                return x, y


def main():
    map_list = np.array([])
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            map_list = np.append(map_list, line)

    start_x, start_y = find_start(map_list)
    end = False
    counter = 0
    start_index = start_y
    direction = Direction()
    while end is False:
        temp, start_index, end = go_until_obstacle()
        counter += temp



if __name__ == '__main__':
    print(main())
