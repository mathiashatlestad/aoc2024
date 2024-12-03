"""AoC 3, 2024: Mull It Over."""

# Standard library imports
import pathlib
import sys
import re

def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input


def part1(data):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, data)
    data = []
    for match in matches:
        match = match.replace("mul(", "").replace(")", "")
        split = match.split(",")
        data.append((int(split[0]), int(split[1])))
    return sum(pair[0] * pair[1] for pair in data)


def part2(data):
    pattern = r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))"
    matches = re.findall(pattern, data)
    data = []
    enabled = True
    for match in matches:
        if match == "don't()":
            enabled = False
            continue

        if match == "do()":
            enabled = True
            continue

        if enabled is False:
            continue

        match = match.replace("mul(", "").replace(")", "")
        split = match.split(",")
        data.append((int(split[0]), int(split[1])))

    return sum(pair[0] * pair[1] for pair in data)


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
