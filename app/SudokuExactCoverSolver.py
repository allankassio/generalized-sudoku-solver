from app.ExactCoverSolver import ExactCoverSolver


class SudokuExactCoverSolver:

    # :type sudoku_matrix: SudokuMatrix
    def __init__(self, sudoku_matrix):

        self.sudoku_matrix = sudoku_matrix
        self.n = sudoku_matrix.get_rank()
        self.exact_cover_matrix, self.possibilities = self._create_exact_cover_matrix()
        self.exact_cover_solver = ExactCoverSolver(self.exact_cover_matrix)

    def solve(self):
        self.exact_cover_solver.search(k=0, o=dict())
        solutions = self.exact_cover_solver.get_answer()

        for solution in solutions[0].values():
            row, column, value = self.possibilities[solution.row_id - 1]
            if self.sudoku_matrix.is_empty_cell(row, column):
                self.sudoku_matrix.set(row, column, value)

    def get_num_updates(self):
        return self.exact_cover_solver.get_num_updates()

    def _create_exact_cover_matrix(self):
        possibilities = self._create_possibilities()
        constraints = self._create_constraints()
        exact_cover_matrix = []

        for possibility in possibilities:
            m = []
            for constraint in constraints:
                m.append(self._handle_possibility_constraint_combination(possibility, constraint))
            exact_cover_matrix.append(m)

        return exact_cover_matrix, possibilities

    def _create_possibilities(self):
        possibilities = []

        for row in range(self.n ** 2):
            for column in range(self.n ** 2):
                if self.sudoku_matrix.is_empty_cell(row, column):
                    for i in range(1, self.n ** 2 + 1):
                        if self.sudoku_matrix.is_valid(row, column, i):
                            possibilities.append((row, column, i))
                else:
                    possibilities.append((row, column, self.sudoku_matrix.get(row, column)))

        return possibilities

    def _create_constraints(self):
        constraints = []

        # restrição de linha-coluna
        for row in range(self.n ** 2):
            for column in range(self.n ** 2):
                constraints.append(('rc', row, column))

        # restrição de número de linha
        for row in range(self.n ** 2):
            for number in range(1, self.n ** 2 + 1):
                constraints.append(('rn', row, number))

        # restrição de número de coluna
        for column in range(self.n ** 2):
            for number in range(1, self.n ** 2 + 1):
                constraints.append(('cn', column, number))

        # restrição de número de caixa
        for box in range(self.n ** 2):
            for number in range(1, self.n ** 2 + 1):
                constraints.append(('bn', box, number))

        return constraints

    def _handle_possibility_constraint_combination(self, possibility, constraint):
        row, column, value = possibility
        constraint_type, x, y = constraint

        if constraint_type == 'rc':
            return 1 if row == x and column == y else 0

        if constraint_type == 'rn':
            return 1 if row == x and value == y else 0

        if constraint_type == 'cn':
            return 1 if column == x and value == y else 0

        if constraint_type == 'bn':
            box_index = self.sudoku_matrix.get_box_index(row, column)
            return 1 if box_index == x and value == y else 0
