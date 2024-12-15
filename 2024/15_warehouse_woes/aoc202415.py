"""AoC 15, 2024: Warehouse Woes."""

# Standard library imports
import pathlib
import sys

def parse_data(puzzle_input):
    """Parse input."""
    parts = puzzle_input.strip().split("\n\n")
    mapp = [list(line) for line in parts[0].split('\n')]
    moves = list(parts[1].replace('\n', ''))
    return mapp, moves

def try_move(mapp, start, direction):
    current = start
    first_empty = None
    first_box_to_move = None
    while True:
        ni, nj = current[0] + direction[0], current[1] + direction[1]
        current = (ni, nj)

        if not (0 <= ni < len(mapp[0]) or not (0 <= nj < len(mapp[1]))):
            return start

        if mapp[ni][nj] == '#':
            return start

        if mapp[ni][nj] == '.':
            first_empty = (ni, nj)
            break

        if mapp[ni][nj] == 'O' and first_box_to_move is None:
            first_box_to_move = (ni, nj)

    if first_box_to_move is not None and first_empty is not None:
        mapp[first_box_to_move[0]][first_box_to_move[1]], mapp[first_empty[0]][first_empty[1]] = mapp[first_empty[0]][first_empty[1]], mapp[first_box_to_move[0]][first_box_to_move[1]]
        first_empty = first_box_to_move

    if first_empty is not None:
        mapp[start[0]][start[1]], mapp[first_empty[0]][first_empty[1]] = mapp[first_empty[0]][first_empty[1]], mapp[start[0]][start[1]]
        return first_empty

    return start

def part1(mapp, moves):
    """Solve part 1."""
    print(mapp)
    print(moves)
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    current = (0, 0)
    for i, row in enumerate(mapp):
        for j, col in enumerate(row):
            if col == '@':
                current = (i, j)
                break

    print("MOVE : " + "0")
    result = ""
    for i, row in enumerate(mapp):
        tmp = ""
        for j, col in enumerate(row):
            tmp += col
        result += tmp + '\n'
    print(result)

    for move in moves:
        current = try_move(mapp, current, directions[move])

    value = 0
    for i, row in enumerate(mapp):
        for j, col in enumerate(row):
            if col == 'O':
                value += i*100 + j

    return value

def part2(mapp, moves):
    """Solve part 2."""


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data, moves = parse_data(puzzle_input)
    yield part1(data, moves)
    yield part2(data, moves)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
