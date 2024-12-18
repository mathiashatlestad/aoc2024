"""AoC 16, 2024: Warehouse Woes."""

# Standard library imports
import pathlib
import sys
import heapq
from collections import defaultdict
from inspect import stack

DIRECTIONS = {
    'up': (0, -1),
    'down': (0, 1),
    'left': (-1, 0),
    'right': (1, 0),
}

sys.setrecursionlimit(2000)


TURN_COST = 1000


def parse_data(puzzle_input):
    return [list(line) for line in puzzle_input.split('\n')]


def find_item(mapp, c):
    for i, row in enumerate(mapp):
        for j, col in enumerate(row):
            if col == c:
                return (i, j)


def part1(maze):
    return -1
    start = find_item(maze, 'S')
    end = find_item(maze, 'E')
    cost, visited = dijkstra_with_turns(maze, start, end)
    return cost


def dijkstra_with_turns(maze, start, end):
    height, width = len(maze), len(maze[0])
    pq = []
    heapq.heappush(pq, (0, start[0], start[1], None))
    visited = {}

    predecessors = defaultdict(list)
    min_cost = float('inf')

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
                    # Only add to predecessors if it reduces the cost or equals the minimum cost
                    if (ny, nx, new_direction) not in visited or visited[(ny, nx, new_direction)] > new_cost:
                        predecessors[(ny, nx)].append((y, x))

    # Backtrack to find all paths
    def backtrack(node, exits):
        y, x = node
        if node in exits:
            return []
        exits.add(node)
        if (y, x) == start:
            return [(y, x)]
        if (y, x) not in predecessors:
            return []
        paths = []
        l = predecessors[(y, x)]
        for (y, x) in l:
            pt = [y, x]
            for path in backtrack((y, x), exits):
                pt.append(path)
            paths.append(pt)
        return paths

    unique_positions = set()
    min_paths = backtrack(end, unique_positions)
    return min_cost, min_paths


def part2(maze):
    """Solve part 2."""
    start = find_item(maze, 'S')
    end = find_item(maze, 'E')
    cost, visited = dijkstra_with_turns(maze, start, end)
    return len(visited)


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
