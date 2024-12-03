"""AoC 3, 2024: Mull It Over."""

# Standard library imports
import pathlib
import sys
import re

def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input


def part1(data):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, data)
    return sum(int(num1) * int(num2) for num1, num2 in matches)


def part2(data):
    pattern = r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))"
    matches = re.findall(pattern, data)
    enabled = True
    result = 0

    for match, num1, num2 in matches:
        if match == "don't()":
            enabled = False
        elif match == "do()":
            enabled = True
        elif enabled and num1 and num2:
            result += int(num1) * int(num2)

    return result


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
