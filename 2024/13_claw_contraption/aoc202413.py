"""AoC 13, 2024: Claw Contraption."""
import functools
# Standard library imports
import pathlib
import sys
import re
import numpy as np

def parse_data(puzzle_input):
    """Parse input."""
    pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
    matches = re.findall(pattern, puzzle_input)
    results = []
    for match in matches:
        a_x, a_y, b_x, b_y, prize_x, prize_y = map(int, match)
        results.append((a_x, a_y, b_x, b_y, prize_x, prize_y))
    return results

def solve_equation(dx_a, dy_a, dx_b, dy_b, prize_x, prize_y):
    prize = (prize_x, prize_y)
    matrix = np.array([(dx_a, dy_a), (dx_b, dy_b)], dtype=int).transpose()
    result = np.linalg.solve(matrix, prize)

    result[0] = round(result[0])
    result[1] = round(result[1])

    if not np.any(matrix @ result - prize):
        return int(3 * result[0] + result[1])

    return 0

def part1(data):
    """Solve part 1."""
    tokens = 0
    for dx_a, dy_a, dx_b, dy_b, prize_x, prize_y in data:
        tokens += solve_equation(dx_a, dy_a, dx_b, dy_b, prize_x, prize_y)
    return tokens


def part2(data):
    """Solve part 2."""
    tokens = 0
    for dx_a, dy_a, dx_b, dy_b, prize_x, prize_y in data:
        tokens += solve_equation(dx_a, dy_a, dx_b, dy_b, prize_x+10000000000000, prize_y+10000000000000)
    return tokens


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
