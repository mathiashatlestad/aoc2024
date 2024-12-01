"""AoC 1, 2024: Historian Hysteria."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    return [list(map(int, line.split())) for line in puzzle_input.strip().split('\n')]


def part1(data):
    first_row = [row[0] for row in data]
    first_row.sort()
    second_row = [row[1] for row in data]
    second_row.sort()
    result = 0
    for i in range(0, len(first_row)):
        result += abs(first_row[i] - second_row[i])
    return result


def part2(data):
    first_row = [row[0] for row in data]
    occurrences = {}
    for number in [row[1] for row in data]:
        occurrences[number] = occurrences.get(number, 0) + 1
    result = 0
    for i in first_row:
        result += i * occurrences.get(i, 0)
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
