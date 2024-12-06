"""AoC 6, 2024: Guard Gallivant."""

# Standard library imports
import pathlib
import sys
import time

def parse_data(puzzle_input):
    return [list(line) for line in puzzle_input.strip().split('\n')]


def get_initial_state(data):

    start = None
    obstacles = set()

    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell == '^':
                start = (i, j)
            elif cell == '#':
                obstacles.add((i, j))

    return start, obstacles, (len(data), len(data[0]))


def traverse_grid(start, obstacles, directions, grid_size):

    visited = set()
    current = start
    current_dir = 0

    while True:
        ni, nj = current[0] + directions[current_dir][0], current[1] + directions[current_dir][1]

        if not (0 <= ni < grid_size[0] and 0 <= nj < grid_size[1]):
            break

        if (ni, nj) not in obstacles:  # Free to move
            visited.add((ni, nj))
            current = (ni, nj)
        else:
            current_dir = (current_dir + 1) % len(directions)

    return visited


def is_infinite_loop(obstacles, directions, start, grid_size):

    visited = set()
    current = start
    current_dir = 0

    while True:
        ni, nj = current[0] + directions[current_dir][0], current[1] + directions[current_dir][1]

        if not (0 <= ni < grid_size[0] and 0 <= nj < grid_size[1]):
            return False

        if (ni, nj) not in obstacles:
            state = (ni, nj, current_dir)
            if state in visited:
                return True
            visited.add(state)
            current = (ni, nj)
        else:
            current_dir = (current_dir + 1) % len(directions)


def part1(data):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    start, obstacles, grid_size = get_initial_state(data)
    visited = traverse_grid(start, obstacles, directions, grid_size)
    visited.add(start)
    return len(visited)


def part2(data):

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    start, obstacles, grid_size = get_initial_state(data)

    visited = traverse_grid(start, obstacles, directions, grid_size)

    t0 = time.time()
    infinite_cells = 0
    for cell in visited:
        obstacles.add(cell)
        if is_infinite_loop(obstacles, directions, start, grid_size):
            infinite_cells += 1
        obstacles.remove(cell)
    t1 = time.time()

    print(f"Execution time: {t1 - t0:.2f} seconds")
    return infinite_cells


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
