"""AoC 15, 2024: Warehouse Woes."""

# Standard library imports
import pathlib
import sys

directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

def parse_data(puzzle_input):
    """Parse input."""
    parts = puzzle_input.strip().split("\n\n")
    mapp = [list(line) for line in parts[0].split('\n')]
    moves = list(parts[1].replace('\n', ''))
    return mapp, moves

def calculate_weights(mapp):
    value = 0
    for i, row in enumerate(mapp):
        for j, col in enumerate(row):
            if col == 'O' or col == '[':
                value += i*100 + j
    return value

def find_start(mapp):
    for i, row in enumerate(mapp):
        for j, col in enumerate(row):
            if col == '@':
                return (i, j)

def try_move_pt1(mapp, start, direction):
    current = start
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

def find_allowed_to_move_boxes(mapp, start, direction):
    boxes_to_move = []
    ni, nj = new_coordinate(start, direction)

    if mapp[ni][nj] == '[':
        boxes_to_move.append((ni, nj))
        boxes_to_move.append((ni, nj+1))
    elif mapp[ni][nj] == ']':
        boxes_to_move.append((ni, nj))
        boxes_to_move.append((ni, nj-1))

    prev_boxes = []
    while prev_boxes != boxes_to_move:
        for box in boxes_to_move:
            ni, nj = box[0] + direction[0], box[1] + direction[1]
            if mapp[ni][nj] == '[' and (ni, nj) not in boxes_to_move:
                boxes_to_move.append((ni, nj))
                if (ni, nj+1) not in boxes_to_move:
                    boxes_to_move.append((ni, nj+1))
            elif mapp[ni][nj] == ']' and (ni, nj) not in boxes_to_move:
                boxes_to_move.append((ni, nj))
                if (ni, nj-1) not in boxes_to_move:
                    boxes_to_move.append((ni, nj-1))
        prev_boxes = boxes_to_move

    for box in boxes_to_move:
        ni, nj = new_coordinate(box, direction)
        if mapp[ni][nj] == '#':
            return []

    return boxes_to_move

def new_coordinate(cord, direction):
    return cord[0] + direction[0], cord[1] + direction[1]

def try_move_pt2(mapp, start, direction):
    allowed_boxes_to_move = find_allowed_to_move_boxes(mapp, start, direction)

    def projection(coord, vector):
        return coord[0] * vector[0] + coord[1] * vector[1]

    for item in sorted(allowed_boxes_to_move, key=lambda coord: projection(coord, direction), reverse=True):
        ni, nj = new_coordinate(item, direction)
        mapp[item[0]][item[1]], mapp[ni][nj] = mapp[ni][nj], mapp[item[0]][item[1]]

    ni, nj = new_coordinate(start, direction)
    if mapp[ni][nj] == '.':
        mapp[start[0]][start[1]]  = '.'
        mapp[ni][nj] = '@'
        return (ni, nj)

    return start

def extend_map_pt2(mapp):
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
    return new_mapp

def part1(puzzle_input):
    """Solve part 1."""
    mapp, moves = parse_data(puzzle_input)
    current = find_start(mapp)
    for move in moves:
        current = try_move_pt1(mapp, current, directions[move])
    return calculate_weights(mapp)

def part2(puzzle_input):
    """Solve part 2."""
    mapp, moves = parse_data(puzzle_input)
    mapp = extend_map_pt2(mapp)
    current = find_start(mapp)
    for move in moves:
        current = try_move_pt2(mapp, current, directions[move])
    return calculate_weights(mapp)

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    yield part1(puzzle_input)
    yield part2(puzzle_input)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
