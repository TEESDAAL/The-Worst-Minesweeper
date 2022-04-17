import random


class Grid:
    def __init__(self, grid_size: int, number_of_mines: int) -> None:
        self.grid_size: int = grid_size
        self.number_of_mines: int = number_of_mines
        self.grid: list[list[int]] = [
            [0 for _ in range(self.grid_size)] for _ in range(self.grid_size)
        ]
        self._add_mines()
        self.add_hints()

    def _add_mines(self):
        for _ in range(self.number_of_mines):
            while True:
                x = random.randint(0, self.grid_size - 1)
                y = random.randint(0, self.grid_size - 1)
                if self.grid[x][y] != -1:
                    self.grid[x][y] = -1
                    break

    def increment_cell(self, row_index, col_index):
        if (
            any(
                (
                    row_index < 0,
                    row_index > self.grid_size - 1,
                    col_index < 0,
                    col_index > self.grid_size - 1,
                )
            )
            or self.grid[row_index][col_index] == -1
        ):
            return

        self.grid[row_index][col_index] += 1

    def add_hints(self):
        for row_index, row in enumerate(self.grid):
            for col_index, cell in enumerate(row):
                if cell == -1:
                    # increment adjacent cells if they aren't mines
                    self.increment_cell(row_index - 1, col_index - 1)
                    self.increment_cell(row_index - 1, col_index)
                    self.increment_cell(row_index - 1, col_index + 1)

                    self.increment_cell(row_index, col_index - 1)
                    self.increment_cell(row_index, col_index + 1)

                    self.increment_cell(row_index + 1, col_index - 1)
                    self.increment_cell(row_index + 1, col_index)
                    self.increment_cell(row_index + 1, col_index + 1)


if __name__ == "__main__":
    for row in Grid(10, 10).grid:
        print(*row)
