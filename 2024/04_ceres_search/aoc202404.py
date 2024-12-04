"""AoC 4, 2024: Ceres Search."""

# Standard library imports
import pathlib
import sys

def parse_data(puzzle_input):
    """Parse input."""
    return [list(line) for line in puzzle_input.split('\n')]


def part1(data):
    """Solve part 1."""
    return sum(
        is_part_of_xmas(data, i, j)
        for i in range(len(data))
        for j in range(len(data[0]))
    )

def part2(data):
    """Solve part 2."""
    return sum(
        is_part_of_cross_mas(data, i, j)
        for i in range(len(data))
        for j in range(len(data[0]))
    )


def is_part_of_cross_mas(map, x,y):
    if map[x][y] != "A":
        return 0

    directions = [
        (1, 1),   # Down-right
        (1, -1),  # Down-left
        (-1, 1),  # Up-right
        (-1, -1)  # Up-left
    ]

    rows, cols = len(map), len(map[0])

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < rows and 0 <= ny < cols):
            return 0
        if map[nx][ny] not in {"M", "S"}:
            return 0

    if map[x-1][y-1] == map[x+1][y+1] or map[x+1][y-1] == map[x-1][y+1]:
        return 0

    return 1


def is_part_of_xmas(map, x, y):

    if map[x][y] != "X":
        return 0

    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
        (-1, 0),  # Up
        (1, 1),   # Down-right
        (1, -1),  # Down-left
        (-1, 1),  # Up-right
        (-1, -1)  # Up-left
    ]

    sequence = "XMAS"
    rows, cols = len(map), len(map[0])
    count = 0

    for dx, dy in directions:
        if all((0 <= x + i * dx < rows and 0 <= y + i * dy < cols and map[x + i * dx][y + i * dy] == sequence[i]) for i in range(1, len(sequence))):
            count += 1

    return count


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
