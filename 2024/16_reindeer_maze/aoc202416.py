"""AoC 16, 2024: Warehouse Woes."""

# Standard library imports
import pathlib
import sys
import heapq
from collections import defaultdict

# Directions (dy, dx) and their corresponding names
DIRECTIONS = {
    'UP': (-1, 0),
    'DOWN': (1, 0),
    'LEFT': (0, -1),
    'RIGHT': (0, 1),
}

TURN_COST = 1000

def parse_data(puzzle_input):
    return [list(line) for line in puzzle_input.split('\n')]

def find_item(mapp, c):
    for i, row in enumerate(mapp):
        for j, col in enumerate(row):
            if col == c:
                return (i, j)

def part1(maze):
    """Solve part 1."""
    start = find_item(maze, 'S')
    end = find_item(maze, 'E')
    cost, visited = dijkstra_with_turns(maze, start, end)
    return cost


def dijkstra_with_turns(maze, start, end):
    height, width = len(maze), len(maze[0])
    pq = []  # Priority queue: (cost, y, x, direction)
    heapq.heappush(pq, (0, start[0], start[1], None))  # Initial state
    visited = {}  # To store the minimal cost to reach each position with direction

    parents = defaultdict(list)
    min_cost = float('inf')  # Keep track of the minimum cost to reach the end

    while pq:
        cost, y, x, direction = heapq.heappop(pq)

        if (y, x) == end:
            min_cost = min(min_cost, cost)

        if (y, x, direction) in visited and visited[(y, x, direction)] <= cost:
            continue

        visited[(y, x, direction)] = cost
        for new_direction, (dy, dx) in DIRECTIONS.items():
            ny, nx = y + dy, x + dx
            if 0 <= ny < height and 0 <= nx < width and maze[ny][nx] != '#':

                turn_cost = 0 if direction == new_direction else TURN_COST
                new_cost = cost + 1 + turn_cost
                heapq.heappush(pq, (new_cost, ny, nx, new_direction))

                if new_cost <= min_cost:
                    parents[(ny, nx, new_direction)].append((y, x, direction))

    return min_cost, visited

def part2(maze):
    """Solve part 2."""
    start = find_item(maze, 'S')
    end = find_item(maze, 'E')
    cost, visited = dijkstra_with_turns(maze, start, end)
    print(visited)
    return len(set(visited))


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
