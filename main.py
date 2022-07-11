import csv
import time

from app.SudokuBackTrackingSolver import SudokuBackTrackingSolver
from app.SudokuExactCoverSolver import SudokuExactCoverSolver
from app.SudokuGenerator import SudokuGenerator
from app.SudokuValidator import SudokuValidator


def run_exact_cover_solver():
    for n in range(3, 6):
        print(f'n={n}')
        main_solver(
            solver=SudokuExactCoverSolver,
            n=n,
            write_to_csv=True
        )


def run_backtracking_solver():
    for n in range(3, 6):
        print(f'n={n}')
        main_solver(
            solver=SudokuBackTrackingSolver,
            n=n,
            write_to_csv=True
        )


def main_solver(solver, n, num_puzzles=None, write_to_csv=False):

    print(f'{solver.__name__}')
    results = [('num_updates', 'time_taken', 'is_valid')]

    sudoku_generator = SudokuGenerator(n)
    sudoku_matrices = sudoku_generator.generate_puzzles(num_puzzles)

    for sudoku_matrix in sudoku_matrices:
        num_updates, time_taken = solve_puzzle(solver, sudoku_matrix)
        sudoku_validator = SudokuValidator(sudoku_matrix)
        is_valid = sudoku_validator.validate()
        print((n, num_updates, time_taken, is_valid))
        results.append((num_updates, time_taken, is_valid))

    if write_to_csv:
        write_data_to_csv(results, f'output/sudoku_rank_{n}_{solver.__name__}.csv')
    else:
        [print(r) for r in results]

    return results


def solve_puzzle(solver, sudoku_matrix):
    s = solver(sudoku_matrix)

    start = time.time()
    s.solve()
    end = time.time()
    num_updates = s.get_num_updates()
    return num_updates, end - start


def write_data_to_csv(results, csv_file):
    with open(csv_file, 'w') as csv_file:
        writer = csv.writer(csv_file)
        [writer.writerow([r for r in result]) for result in results]


def main():
    # Rodar esses dois métodos vai permitir executar
    # todos os testes dos ranks 3 até 5 (9x9, 16x16 e 25x25)
    # ===========================================================
    # run_exact_cover_solver()
    # run_backtracking_solver()

    # Rodar dessa forma permite definir qual dataset vai
    # ser utilizado apenas mudando o N, desde que n>=3 e n<=9.
    # Para cada valor de n, o tamanho da matriz será de n**2
    # ===========================================================
    # main_solver(solver=SudokuBackTrackingSolver, n=4, write_to_csv=True)
    main_solver(solver=SudokuExactCoverSolver, n=5, write_to_csv=True)
    main_solver(solver=SudokuBackTrackingSolver, n=4, write_to_csv=True)
    main_solver(solver=SudokuBackTrackingSolver, n=5, write_to_csv=True)

if __name__ == "__main__":
    main()
