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
            for key, value in this_set.items():
                visited.add(key)
                total += len(this_set)*value

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

def scan_horizontal(this_set, i, j_min, j_max, already_forward_edge, already_behind_edge):
    forward_edge = 0
    behind_edge = 0
    for j in range(j_min - 1, j_max + 1):

        if (i, j) not in this_set:
            continue

        if (i, j-1) not in this_set:
            if (i-1, j) not in already_behind_edge:
                behind_edge+=1
            already_behind_edge.add((i, j))

        if (i, j+1) not in this_set:
            if (i-1, j) not in already_forward_edge:
                forward_edge+=1
            already_forward_edge.add((i, j))

    return forward_edge + behind_edge


def scan_vertical(this_set, j, i_min, i_max, already_forward_edge, already_behind_edge):
    forward_edge = 0
    behind_edge = 0
    for i in range(i_min - 1, i_max + 1):

        if (i, j) not in this_set:
            continue

        if (i-1, j) not in this_set:
            if (i, j-1) not in already_behind_edge:
                behind_edge+=1
            already_behind_edge.add((i, j))

        if (i+1, j) not in this_set:
            if (i, j-1) not in already_forward_edge:
                forward_edge+=1
            already_forward_edge.add((i, j))

    return forward_edge + behind_edge


def part2(data):
    visited = set()
    total = 0
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if (i, j) in visited:
                continue

            this_set = {}
            find_all_neighbors(data, i, j, this_set, cell)
            for key, value in this_set.items():
                visited.add(key)

            all_i = [t[0] for t in this_set.keys()]
            all_j = [t[1] for t in this_set.keys()]

            global_min_i = min(all_i)
            global_max_i = max(all_i)
            global_min_j = min(all_j)
            global_max_j = max(all_j)

            horizontal = 0
            already_forward_edge = set()
            already_behind_edge = set()
            for ti in range(global_min_i, global_max_i + 1):
                horizontal += scan_horizontal(this_set, ti, global_min_j, global_max_j, already_forward_edge, already_behind_edge)

            vertical = 0
            already_forward_edge = set()
            already_behind_edge = set()
            for ji in range(global_min_j, global_max_j + 1):
                vertical += scan_vertical(this_set, ji, global_min_i, global_max_i, already_forward_edge, already_behind_edge)
            total += len(this_set)*(vertical + horizontal)

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
