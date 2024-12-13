"""AoC 13, 2024: Claw Contraption."""
import functools
# Standard library imports
import pathlib
import sys
import re
from math import gcd
from math import lcm
from sympy import symbols, Eq, solve, Integer
from scipy.optimize import linprog
import pulp as pl

from functools import reduce

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
    tokens = 0

    # Define the problem
    problem = pl.LpProblem("Minimize_tokens", pl.LpMinimize)

    # Variables
    n_a = pl.LpVariable("n_a", lowBound=0, cat=pl.LpInteger)
    n_b = pl.LpVariable("n_b", lowBound=0, cat=pl.LpInteger)

    problem += 3 * n_a + n_b

    problem += (dx_a * n_a + dx_b * n_b == prize_x)
    problem += (dy_a * n_a + dy_b * n_b == prize_y)

    solver = pl.PULP_CBC_CMD()
    problem.solve(solver)

    if problem.status == 1:
        tokens += (3 * n_a.value() + n_b.value())
    return tokens

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
        prize_x+=10000000000000
        prize_y+=10000000000000
        tokens += solve_equation(dx_a, dy_a, dx_b, dy_b, prize_x, prize_y)

    if tokens <= 1762329637000 or tokens == 65975505751957 or tokens == 61556658416632 or tokens == 78481942092912:
        print("Part 2 incorrect")
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
