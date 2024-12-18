"""AoC 18, 2024: RAM Run."""

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
    return [tuple(map(int, line.split(','))) for line in puzzle_input.splitlines()]


def dijkstra_on_corruped_memory(corruped, start, end, size):
    height, width = size, size
    pq = []
    heapq.heappush(pq, (0, start[0], start[1], None))
    visited = {}

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
            if 0 <= ny < height and 0 <= nx < width and (ny, nx) not in corruped:
                new_cost = cost + 1
                heapq.heappush(pq, (new_cost, ny, nx, new_direction))

    return min_cost

def part1(data):
    """Solve part 1."""
    cor_map = set()
    to_drop = 1024
    max_pos = 70
    for corr in data[:to_drop]:
        cor_map.add(corr)
    cost = dijkstra_on_corruped_memory(cor_map, (0,0), (max_pos, max_pos), max_pos + 1)
    return cost

def part2(data):
    """Solve part 2."""
    cor_map = set()
    to_drop = 1024
    max_pos = 70
    
    for corr in data[:to_drop]:
        cor_map.add(corr)

    ## Should look into using binary search instead of brute forcing this!
    while True:
        cor_map.add(data[to_drop])
        cost = dijkstra_on_corruped_memory(cor_map, (0, 0), (max_pos, max_pos), max_pos + 1)
        if cost == float('inf'):
            return data[to_drop]
        to_drop += 1

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
