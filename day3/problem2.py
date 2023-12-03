def read_lines():
    with open("inputs/problem2.txt", "r") as file:
        for line in file:
            yield line.strip()


def get_grid():
    grid = []
    for line in read_lines():
        grid.append(line)

    return grid


class GearRatios:
    def __init__(self, grid):
        self.grid = grid
        self.n, self.m = len(grid), len(grid[0])
        self.directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (-1, 1),
            (1, 1),
            (1, -1),
            (-1, -1),
        ]
        self.seen = set()

    def is_valid(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.m and self.grid[x][y].isdigit()

    def get_number(self, i, j):
        if not self.is_valid(i, j) or (i, j) in self.seen:
            return ""

        self.seen.add((i, j))
        return self.get_number(i, j - 1) + self.grid[i][j] + self.get_number(i, j + 1)

    def get_numbers(self, i, j):
        numbers = []
        for dx, dy in self.directions:
            nx, ny = i + dx, j + dy
            number = self.get_number(nx, ny)
            if number:
                numbers.append(number)

        return numbers

    def sum_gear_ratios(self):
        total = 0
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == "*":
                    numbers = self.get_numbers(i, j)
                    if len(numbers) == 2:
                        total += int(numbers[0]) * int(numbers[1])
        return total


gear_ratios = GearRatios(get_grid())
print(gear_ratios.sum_gear_ratios())
