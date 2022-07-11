from tabulate import tabulate


class SudokuMatrix:

    def __init__(self, n):
        self.n = n  # classificação (rank)
        self.k = 0  # número de pistas (números preenchidos)
        self.sudoku_matrix = [[0 for _ in range(n ** 2)] for _ in range(n ** 2)]
        self.EMPTY_CELL = 0

    def __str__(self):
        return tabulate(self.get_rows(), tablefmt="fancy_grid")

    def get(self, row, column):
        return self.sudoku_matrix[row][column]

    def get_rows(self):
        return self.sudoku_matrix

    def get_row(self, row):
        return self.sudoku_matrix[row]

    def get_columns(self):
        return [*zip(*self.sudoku_matrix)]

    def get_column(self, column):
        return self.get_columns()[column]

    def get_boxes(self):
        indices = [(x % self.n, int(x / self.n)) for x in range(self.n ** 2)]
        boxes = [[self.sudoku_matrix[x * self.n + xx][y * self.n + yy] for xx, yy in indices] for x, y in indices]
        return boxes

    def get_box(self, row, column):
        box_index = self.get_box_index(row, column)
        return self.get_boxes()[box_index]

    def get_box_index(self, row, column):
        indices = [(x % self.n, int(x / self.n)) for x in range(self.n ** 2)]

        xx = row % self.n
        yy = column % self.n

        x = (row - xx) / self.n
        y = (column - yy) / self.n

        return indices.index((x, y))

    def get_rank(self):
        return self.n

    def get_num_clues(self):
        return self.k

    def get_empty_cells(self):
        empty_cells = []

        for row in range(self.n ** 2):
            for column in range(self.n ** 2):
                if self.is_empty_cell(row, column):
                    empty_cells.append((row, column))

        return empty_cells

    def has_empty_cells(self):
        for row in range(self.n ** 2):
            for column in range(self.n ** 2):
                if self.is_empty_cell(row, column):
                    return True

        return False

    def is_empty_cell(self, row, column):
        return self.get(row, column) == self.EMPTY_CELL

    def set(self, row, column, value):
        self.sudoku_matrix[row][column] = value

        if value != self.EMPTY_CELL:
            self.increment_num_clues()

    def set_if_valid(self, row, column, value):
        if self.is_valid(row, column, value):
            self.set(row, column, value)
            return True

        return False

    def make_cell_empty(self, row, column):
        self.set(row, column, self.EMPTY_CELL)

    def increment_num_clues(self):
        self.k += 1

    def is_valid(self, row, column, value):
        if value in self.get_row(row):
            return False

        if value in self.get_column(column):
            return False

        if value in self.get_box(row, column):
            return False

        return True
