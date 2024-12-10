"""AoC 10, 2024: Hoof It."""

# Standard library imports
import pathlib
import sys
from collections import deque


def parse_data(puzzle_input):
    """Parse input."""
    return [[int(char) for char in line] for line in puzzle_input.strip().split('\n')]

def find_all_trail_heads_p1(data, start):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    q = [start]
    trails = set()

    while q:
        x, y = q.pop()
        for direction in directions:
            if data[x][y] == 9:
                trails.add((x, y))
                break

            nx = x + direction[0]
            ny = y + direction[1]

            if 0 <= nx < len(data) and 0 <= ny < len(data[0]):
                if data[nx][ny] - data[x][y] == 1:
                    q.append((nx, ny))

    return len(trails)

def find_all_trail_heads_rating_pt2(data, start):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    q = [[start]]
    trails = []

    while q:
        current_path = q.pop()
        for direction in directions:
            if data[current_path[-1][0]][current_path[-1][1]] == 9 and current_path not in trails:
                trails.append(current_path)
                continue

            nx = current_path[-1][0] + direction[0]
            ny = current_path[-1][1] + direction[1]

            if 0 <= nx < len(data) and 0 <= ny < len(data[0]):
                if data[nx][ny] - data[current_path[-1][0]][current_path[-1][1]] == 1:
                    copy_vector = current_path.copy()
                    copy_vector.append((nx, ny))
                    q.append(copy_vector)

    return len(trails)


def part1(data):
    """Solve part 1."""
    total = 0
    for i, line in enumerate(data):
        for j, val in enumerate(line):
            if val == 0:
                total += find_all_trail_heads_p1(data, (i, j))

    return total

def part2(data):
    """Solve part 2."""
    total = 0
    for i, line in enumerate(data):
        for j, val in enumerate(line):
            if val == 0:
                total += find_all_trail_heads_rating_pt2(data, (i, j))

    return total

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
