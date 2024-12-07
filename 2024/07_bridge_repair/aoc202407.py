"""AoC 7, 2024: Bridge Repair."""

# Standard library imports
import pathlib
import sys
import time

def parse_data(puzzle_input):
    return [
        (int(key), list(map(int, values.split())))
        for line in puzzle_input.strip().split('\n')
        for key, values in [line.split(':')]
    ]

def calculate_if_match(to_match, accumulated, operator, values, operators):

    if operator == '+':
        accumulated += values[0]
    elif operator == '*':
        accumulated *= values[0]
    elif operator == '||':
        accumulated = int(f"{accumulated}{values[0]}")

    if len(values) == 1:
        return accumulated == to_match

    # We only have increasing operators, so no point to continue if overshoot
    if accumulated > to_match:
        return False

    for operator in operators:
        if calculate_if_match(to_match, accumulated, operator, values[1:], operators):
            return True

    return False


def count_matches_for_operators(data, operators):
    matches = 0
    for to_match, values in data:
        if any(calculate_if_match(to_match, 0, operator, values, operators) for operator in operators):
            matches += to_match
    return matches


def part1(data):
    """Solve part 1."""
    t0 = time.time()
    matches = count_matches_for_operators(data, ["+", "*"])
    t1 = time.time()
    print(f"Execution time pt1: {t1 - t0:.2f} seconds")
    return matches


def part2(data):
    """Solve part 2."""
    t0 = time.time()
    matches = count_matches_for_operators(data, ["||", "*", "+"])
    t1 = time.time()
    print(f"Execution time pt2: {t1 - t0:.2f} seconds")
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
