"""AoC 7, 2024: Bridge Repair."""

# Standard library imports
import pathlib
import sys
from itertools import accumulate
import time
from functools import lru_cache

def parse_data(puzzle_input):
    result = []
    for line in puzzle_input.strip().split('\n'):
        key, values = line.split(':')
        result.append((int(key.strip()), list(map(int, values.strip().split())) ))
    return result

def is_match_over(to_match, accumulated, operator, values_left, operators):
    if operator == '+':
        accumulated += values_left[0]
    elif operator == '*':
        accumulated *= values_left[0]
    elif operator == '||':
        accumulated = int(str(accumulated) + str(values_left[0]))

    if accumulated > to_match:
        return False
    if len(values_left) == 1:
        if accumulated == to_match:
            return True
        else:
            return False

    for operator in operators:
        if is_match_over(to_match, accumulated, operator, values_left[1:], operators):
            return True
    return False

def part1(data):
    operators = ["+", "*"]
    matches = 0
    for (to_match, values) in data:
        for operator in operators:
            if is_match_over(to_match, 0, operator, values, operators):
                matches += to_match
                break
    return matches

def part2(data):
    """Solve part 2."""
    t0 = time.time()
    operators = ["+", "*", "||"]
    matches = 0
    for (to_match, values) in data:
        for operator in operators:
            if is_match_over(to_match, 0, operator, values, operators):
                matches += to_match
                break

    t1 = time.time()

    print(f"Execution time: {t1 - t0:.2f} seconds")

    return matches

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
