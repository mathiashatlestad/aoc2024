"""AoC 2, 2024: Red-Nosed Reports."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    return [list(map(int, line.split(' '))) for line in puzzle_input.split('\n')]


def part1(data):
    return sum(1 for line in data if is_safe(line))


def part2(data):
    count = 0
    for line in data:
        if is_safe(line):
            count += 1
            continue
        if any(is_safe(line[:i] + line[i + 1:]) for i in range(len(line))):
            count += 1
    return count


def is_safe(line):
    diffs = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    should_increase = diffs[0] > 0
    for diff in diffs:
        if not (1 <= abs(diff) <= 3):
            return False
        if (diff > 0) != should_increase:
            return False
    return True


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
