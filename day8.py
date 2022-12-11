"""
"""


from functools import reduce
from operator import mul


def get_input():
    with open('inputs/day8.txt') as f:
        inputs = [list(map(int, s)) for s in f.read().split('\n')]
    return inputs


class Grid:
    def __init__(self, grid) -> None:
        self.grid = grid
        self.grid_rotated = list(zip(*reversed(grid)))

    @property
    def len_x(self):
        return len(self.grid[0])

    @property
    def len_y(self):
        return len(self.grid)

    def check_visibility(self, x: int, y: int) -> bool:
        viewed_tree = self.grid[y][x]
        bmbrman = self.apply_on_bomberman_grid(x, y, max)
        return any(viewed_tree > highest_tree for highest_tree in bmbrman)

    def apply_on_bomberman_grid(self, x, y, func: callable):
        y_rotated = abs(y - (len(self.grid[y]) - 1))
        right = func(self.grid[y][x + 1:])
        left = func(reversed(self.grid[y][:x]))
        up = func(self.grid_rotated[x][y_rotated + 1:])
        down = func(reversed(self.grid_rotated[x][:y_rotated]))
        return [right, left, up, down]

    def get_scenic_score(self, x: int, y: int) -> int:
        viewed_tree = self.grid[y][x]

        def _get_distance(slice: list):
            list_slice = list(slice)
            full_distance = len(list_slice)
            for i, tree in enumerate(list_slice, 1):
                if tree >= viewed_tree:
                    return i
            return full_distance

        bmbrman = self.apply_on_bomberman_grid(x, y, _get_distance)
        return reduce(mul, bmbrman)

    def count_visible_trees(self):
        visibility_counter = 0
        for y in range(1, self.len_y - 1):
            for x in range(1, self.len_x - 1):
                visibility_counter += self.check_visibility(x, y)

        return visibility_counter + (self.len_x * 2 + (self.len_y - 2) * 2)

    def get_scenic_score_grid(self) -> list[list[int]]:
        scenic_scores = []
        for y in range(1, self.len_y - 1):
            for x in range(1, self.len_x - 1):
                scenic_scores.append(self.get_scenic_score(x, y))

        return max(scenic_scores)


def part1():
    """
    """
    inpt = get_input()

    grid = Grid(inpt)

    return grid.count_visible_trees()


def part2():
    """
    """
    inpt = get_input()

    grid = Grid(inpt)

    return grid.get_scenic_score_grid()


if __name__ == '__main__':
    print(part1())
    print(part2())
