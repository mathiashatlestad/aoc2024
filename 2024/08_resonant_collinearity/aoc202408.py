"""AoC 8, 2024: Resonant Collinearity."""

# Standard library imports
import pathlib
import sys

import time

def parse_data(puzzle_input):
    """Parse input."""
    return [list(line) for line in puzzle_input.strip().split('\n')]


def part1(data):
    """Solve part 1."""
    i_max = len(data)
    j_max = len(data[0])
    m_map = {}
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell != '.':
                m_map.setdefault(cell, []).append((i, j))

    anti_nodes = set()
    for node_positions in m_map.values():
        while node_positions:
            curr = node_positions.pop()
            for other in node_positions:
                di, dj = other[0] - curr[0], other[1] - curr[1]
                ni, nj = curr[0]-di, curr[1]-dj
                if 0 <= ni < i_max and 0 <= nj < j_max:
                    anti_nodes.add((ni, nj))
                ni, nj = other[0] + di, other[1] + dj
                if 0 <= ni < i_max and 0 <= nj < j_max:
                    anti_nodes.add((ni, nj))

    return len(anti_nodes)

def part2(data):
    t0 = time.time()

    """Solve part 2."""
    i_max = len(data)
    j_max = len(data[0])
    m_map = {}
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell != '.':
                m_map.setdefault(cell, []).append((i, j))

    anti_nodes = set()
    for node_positions in m_map.values():
        while node_positions:
            curr = node_positions.pop()
            for other in node_positions:
                di, dj = other[0] - curr[0], other[1] - curr[1]
                for direction in [-1, 1]:
                    exp = 0
                    while True:
                        ni = curr[0] + direction * di * exp
                        nj = curr[1] + direction * dj * exp
                        if 0 <= ni < i_max and 0 <= nj < j_max:
                            anti_nodes.add((ni, nj))
                            exp += 1
                        else:
                            break

    t1 = time.time()
    print(f"Execution time pt1: {(t1 - t0)*1000} ms")

    return len(anti_nodes)


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
