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
    cleared_to_move = False
    boxes_to_move = []
    while True:
        ni, nj = current[0] + direction[0], current[1] + direction[1]
        current = (ni, nj)

        if not (0 <= ni < len(mapp[0]) or not (0 <= nj < len(mapp[1]))):
            return start

        if mapp[ni][nj] == '#':
            return start

        if mapp[ni][nj] == '.':
            cleared_to_move = True
            break

        if mapp[ni][nj] == 'O':
            boxes_to_move.append((ni, nj))

    for item in reversed(boxes_to_move):
        ni, nj = item[0] + direction[0], item[1] + direction[1]
        mapp[item[0]][item[1]], mapp[ni][nj] = mapp[ni][nj], mapp[item[0]][item[1]]

    if cleared_to_move:
        ni, nj = start[0] + direction[0], start[1] + direction[1]
        mapp[start[0]][start[1]]  = '.'
        mapp[ni][nj] = '@'
        return (ni, nj)

    return start

def find_if_allowed_to_move_boxes(mapp, start, direction):
    boxes_to_move = []
    ni, nj = start[0] + direction[0], start[1] + direction[1]
    all_allowed = True

    if mapp[ni][nj] == '[':
        boxes_to_move.append((ni, nj))
        boxes_to_move.append((ni, nj+1))
    elif mapp[ni][nj] == ']':
        boxes_to_move.append((ni, nj))
        boxes_to_move.append((ni, nj-1))

    box_added = True

    while box_added and all_allowed:
        box_added = False
        for box in boxes_to_move:
            ni, nj = box[0] + direction[0], box[1] + direction[1]
            if mapp[ni][nj] == '[' and (ni, nj) not in boxes_to_move:
                box_added = True
                boxes_to_move.append((ni, nj))
                if (ni, nj+1) not in boxes_to_move:
                    boxes_to_move.append((ni, nj+1))
            elif mapp[ni][nj] == ']' and (ni, nj) not in boxes_to_move:
                boxes_to_move.append((ni, nj))
                if (ni, nj-1) not in boxes_to_move:
                    boxes_to_move.append((ni, nj-1))
                box_added = True

    for box in boxes_to_move:
        ni, nj = box[0] + direction[0], box[1] + direction[1]
        if mapp[ni][nj] == '#':
            return []

    return boxes_to_move

def try_move_v2(mapp, start, direction):
    current = start
    ni, nj = current[0] + direction[0], current[1] + direction[1]

    if mapp[ni][nj] == '#':
        return start

    boxes_to_move = find_if_allowed_to_move_boxes(mapp, start, direction)

    def projection(coord, vector):
        return coord[0] * vector[0] + coord[1] * vector[1]

    sorted_boxes = sorted(boxes_to_move, key=lambda coord: projection(coord, direction))
    for item in reversed(sorted_boxes):
        ni, nj = item[0] + direction[0], item[1] + direction[1]
        mapp[item[0]][item[1]], mapp[ni][nj] = mapp[ni][nj], mapp[item[0]][item[1]]

    ni, nj = start[0] + direction[0], start[1] + direction[1]
    if mapp[ni][nj] == '.':
        mapp[start[0]][start[1]]  = '.'
        mapp[ni][nj] = '@'
        return (ni, nj)

    return start

def part1(mapp, moves):
    """Solve part 1."""
    return None

    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    current = (0, 0)
    for i, row in enumerate(mapp):
        for j, col in enumerate(row):
            if col == '@':
                current = (i, j)
                break

    for move in moves:
        current = try_move(mapp, current, directions[move])

    value = 0
    for i, row in enumerate(mapp):
        for j, col in enumerate(row):
            if col == 'O':
                value += i*100 + j

    if value == 1318523:
        print("PART 1 DONE")

    return value

import copy

def part2(mapp, moves):
    """Solve part 2."""
    print_mapp(mapp)

    new_mapp = []
    for i, row in enumerate(mapp):
        adjusted = []
        for j, col in enumerate(row):
            if col == '@':
                adjusted.append('@')
                adjusted.append('.')
            elif col == '#':
                adjusted.append('#')
                adjusted.append('#')
            elif col == '.':
                adjusted.append('.')
                adjusted.append('.')
            elif col == 'O':
                adjusted.append('[')
                adjusted.append(']')
        new_mapp.append(adjusted)
    mapp = new_mapp

    print("Initial map")
    print_mapp(mapp)

    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    current = (0, 0)
    for i, row in enumerate(mapp):
        for j, col in enumerate(row):
            if col == '@':
                current = (i, j)
                break

    for move in moves:
        current = try_move_v2(mapp, current, directions[move])

    value = 0
    for i, row in enumerate(mapp):
        for j, col in enumerate(row):
            if col == '[':
                value += i * 100 + j

    print_mapp(mapp)

    if value == 1342227:
        print("PART 2 WRONG")

    return value

def print_mapp(mapp):
    result = ""
    for i, row in enumerate(mapp):
        tmp = ""
        for j, col in enumerate(row):
            tmp += col
        result += tmp + '\n'
    print(result)

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
