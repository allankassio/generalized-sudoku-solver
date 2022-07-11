import csv

from app.SudokuMatrix import SudokuMatrix


class SudokuGenerator:

    def __init__(self, n):
        self.n = n
        self.csv_file = f'datasets/sudoku_rank_{self.n}.csv'

    def generate_puzzles(self, num_puzzles=None):
        puzzles = self._read_sudoku_csv(num_puzzles)
        return [self._convert_string_to_matrix(puzzle) for puzzle in puzzles]

    def generate_puzzle_from_id(self, i):
        with open(self.csv_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            sudoku_puzzle = list(csv_reader)[i][0]

        return [self._convert_string_to_matrix(sudoku_puzzle)]

    def _read_sudoku_csv(self, num_puzzles=None):
        sudoku_puzzles = []
        with open(self.csv_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader, None)  # pula o cabeçalho

            for i, row in enumerate(csv_reader):
                if num_puzzles and len(sudoku_puzzles) == num_puzzles:
                    break

                sudoku_puzzles.append(row[0])

        return sudoku_puzzles

    def _convert_string_to_matrix(self, sudoku_string):
        sudoku_matrix = SudokuMatrix(self.n)

        c = 0
        for i in range(self.n ** 2):
            for j in range(self.n ** 2):
                if sudoku_string[c] == '.':
                    sudoku_matrix.set(i, j, 0)
                else:
                    sudoku_matrix.set(i, j, int(sudoku_string[c:c + 2]))
                c += 2

        return sudoku_matrix
