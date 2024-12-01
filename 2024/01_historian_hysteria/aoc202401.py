"""AoC 1, 2024: Historian Hysteria."""

# Standard library imports
import pathlib
import sys
from collections import Counter


def parse_data(puzzle_input):
    return [list(map(int, line.split())) for line in puzzle_input.strip().split('\n')]


def part1(data):
    return sum(abs(a - b) for a, b in zip(sorted([row[0] for row in data]), sorted([row[1] for row in data])))


def part2(data):
    occurrences = Counter(row[1] for row in data)
    return sum(i * occurrences.get(i, 0) for i in (row[0] for row in data))


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
