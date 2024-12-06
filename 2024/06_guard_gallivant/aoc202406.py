"""AoC 6, 2024: Guard Gallivant."""

# Standard library imports
import pathlib
import sys
import time


def parse_data(puzzle_input):
    """Parse input."""
    return [list(line) for line in puzzle_input.split('\n')]


def part1(data):
    """Solve part 1."""
    directions = [
        (-1, 0),  # Up
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
    ]

    start = (0, 0)
    obstacles = set()

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '^':
                start = (i, j)
            elif data[i][j] == '#':
                obstacles.add((i, j))

    current = start
    currentDir = 0
    visited = set()
    visited.add(current)
    while True:
        ni, nj = current[0] + directions[currentDir][0], current[1] + directions[currentDir][1]
        if ni >= len(data) or ni < 0 or nj >= len(data[0]) or nj < 0:
            break
        elif (ni, nj) not in obstacles:
            visited.add((ni, nj))
            current = (ni, nj)
            continue
        else:
            currentDir = currentDir + 1
            if currentDir >= len(directions):
                currentDir = 0

    return len(visited)

def part2(data):
    t0 = time.time()
    """Solve part 2."""
    directions = [
        (-1, 0),  # Up
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
    ]

    start = (0, 0)
    obstacles = set()

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '^':
                start = (i, j)
            elif data[i][j] == '#':
                obstacles.add((i, j))

    current = start
    currentDir = 0
    visited = set()

    while True:
        ni, nj = current[0] + directions[currentDir][0], current[1] + directions[currentDir][1]
        if ni >= len(data) or ni < 0 or nj >= len(data[0]) or nj < 0:
            break
        elif (ni, nj) not in obstacles:
            visited.add((ni, nj))
            current = (ni, nj)
            continue
        else:
            currentDir = currentDir + 1
            if currentDir >= len(directions):
                currentDir = 0
    sum = 0
    lenghts = (len(data), len(data[0]))
    for (i, j) in visited:
        obstacles.add((i, j))
        if isInfinite(obstacles, directions, start, lenghts):
            sum = sum + 1
        obstacles.remove((i, j))

    t1 = time.time()

    total = t1-t0
    print(total)
    return sum

def isInfinite(obstacles, directions, start, lengths):
    visited = set()
    current = start
    currentDir = 0
    while True:
        ni, nj = current[0] + directions[currentDir][0], current[1] + directions[currentDir][1]
        if ni >= lengths[0] or ni < 0 or nj >= lengths[1] or nj < 0:
            return False
        elif (ni, nj) not in obstacles:
            if (ni, nj, currentDir) not in visited:
                visited.add((ni, nj, currentDir))
            else:
                return True
            current = (ni, nj)
            continue
        else:
            currentDir = currentDir + 1
            if currentDir >= len(directions):
                currentDir = 0


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
