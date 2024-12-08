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
    m_map = {}
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell != '.':
                m_map.setdefault(cell, []).append((i, j))

    anti_nodes = set()
    add_to_set_if_valid = lambda a, b: anti_nodes.add((a, b)) if 0 <= a < len(data) and 0 <= b < len(data[0]) else None
    for node_positions in m_map.values():
        while node_positions:
            curr = node_positions.pop()
            for other in node_positions:
                di, dj = other[0] - curr[0], other[1] - curr[1]
                add_to_set_if_valid(curr[0] - di, curr[1] - dj)
                add_to_set_if_valid(other[0] + di, other[1] + dj)

    return len(anti_nodes)

def part2(data):
    i_max = len(data)
    j_max = len(data[0])
    m_map = {}
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell != '.':
                m_map.setdefault(cell, []).append((i, j))

    anti_nodes = set()
    for positions in m_map.values():
        while positions:
            curr = positions.pop()
            for other in positions:
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
