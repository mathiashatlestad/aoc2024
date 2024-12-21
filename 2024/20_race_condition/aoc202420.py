"""AoC 20, 2024: Race Condition."""

# Standard library imports
import pathlib
import sys

import heapq

DIRECTIONS = {
    'up': (0, -1),
    'down': (0, 1),
    'left': (-1, 0),
    'right': (1, 0),
}


def parse_data(puzzle_input):
    if isinstance(puzzle_input, str):
        lines = puzzle_input.split('\n')
    else:
        lines = puzzle_input
    return [list(line) for line in lines if line]


def dijkstra_with_cheating(walls, already_cheated, start, end, width, height, allowed_to_cheat):
    pq = []
    no_cheat = (-1, -1, None)

    heapq.heappush(pq, (0, start[0], start[1], no_cheat))
    visited = {}
    min_cost = float('inf')
    min_cheat = (-1, -1)

    while pq:
        cost, y, x, cheat = heapq.heappop(pq)

        if not 0 <= y < height or not 0 <= x < width:
            continue

        if cheat in already_cheated:
            continue

        if (y, x) == end:
            if cost < min_cost:
                min_cost = cost
                min_cheat = cheat

        if (y, x, cheat is no_cheat) in visited and visited[(y, x, cheat is no_cheat)] <= cost:
            continue

        visited[(y, x, cheat is no_cheat)] = cost

        for new_direction, (dy, dx) in DIRECTIONS.items():
            ny, nx = y + dy, x + dx
            if 0 <= ny < height and 0 <= nx < width:
                if (ny, nx) not in walls:
                    heapq.heappush(pq, (cost + 1, ny, nx, cheat))
                elif allowed_to_cheat and cheat is no_cheat:
                    for new_cheat_direction, (dy, dx) in DIRECTIONS.items():
                        cy, cx = ny + dy, nx + dx
                        new_cheat = (cy, cx, new_cheat_direction)
                        heapq.heappush(pq, (cost + 1, ny, nx, new_cheat))
                        heapq.heappush(pq, (cost + 2, cy, cx, new_cheat))

    return min_cost, min_cheat

def find_item(mapp, c):
    for i, row in enumerate(mapp):
        for j, col in enumerate(row):
            if col == c:
                return (i, j)

def part1(data):
    """Solve part 1."""
    walls = set()
    width, height = len(data[0]), len(data)
    start = find_item(data, 'S')
    end = find_item(data, 'E')
    already_cheated = set()
    for y in range(height):
        for x in range(width):
            if data[y][x] == '#':
                walls.add((y, x))

    no_cheat_cost, min_cheat = dijkstra_with_cheating(walls, already_cheated, start, end, width, height, False)

    while True:
        with_cheat_cost, cheat = dijkstra_with_cheating(walls, already_cheated, start, end, width, height, True)
        print(no_cheat_cost, with_cheat_cost, cheat)
        if no_cheat_cost - with_cheat_cost >= 100:
            already_cheated.add(cheat)
        else:
            break

    return len(already_cheated)

def part2(data):
    return find_item(data, 'S')

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
