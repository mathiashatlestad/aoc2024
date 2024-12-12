"""AoC 12, 2024: Garden Groups."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [list(line) for line in puzzle_input.strip().split('\n')]


def part1(data):
    """Solve part 1."""
    visited = set()

    total = 0
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if (i, j) in visited:
                continue
            this_set = {}
            find_all_neighbors(data, i, j, this_set, cell)
            print(cell, this_set)
            for key, value in this_set.items():
                visited.add(key)
                total += value*len(this_set)

    return total

def find_all_neighbors(data,  i, j, this_set, curr):
    if (i, j) in this_set:
        return

    """Find all neighbors."""
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    rating = 4

    for direction in directions:
        nx = i + direction[0]
        ny = j + direction[1]
        if ny < 0 or ny >= len(data) or nx < 0 or nx >= len(data[0]):
            continue
        if data[nx][ny] != curr:
            continue
        rating -= 1

    this_set[(i, j)] = rating

    for direction in directions:
        nx = i + direction[0]
        ny = j + direction[1]
        if ny < 0 or ny >= len(data) or nx < 0 or nx >= len(data[0]):
            continue
        if data[nx][ny] != curr:
            continue
        find_all_neighbors(data, nx, ny, this_set, curr)


def part2(data):
    """Solve part 2."""


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
