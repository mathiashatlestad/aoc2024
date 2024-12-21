import sys
import pathlib
from collections import deque

DIRECTIONS = [
    (0, 1),  # down
    (0, -1),  # up
    (1, 0),  # right
    (-1, 0),  # left
]

def parse_data(puzzle_input):
    if isinstance(puzzle_input, str):
        lines = puzzle_input.strip().split('\n')
    else:
        lines = puzzle_input
    return [list(line) for line in lines if line]


def find_item(mapp, c):
    for r, row in enumerate(mapp):
        for c_idx, val in enumerate(row):
            if val == c:
                return (r, c_idx)
    return None


def bfs(mapp, start, ignore_walls=False, max_steps=None):
    rows, cols = len(mapp), len(mapp[0])
    dist = [[None] * cols for _ in range(rows)]
    queue = deque()
    r0, c0 = start
    dist[r0][c0] = 0
    queue.append((r0, c0))

    while queue:
        r, c = queue.popleft()
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if ignore_walls or mapp[nr][nc] != '#':
                    if dist[nr][nc] is None:
                        new_cost = dist[r][c] + 1
                        if max_steps is None or new_cost <= max_steps:
                            dist[nr][nc] = new_cost
                            queue.append((nr, nc))
    return dist


def find_all_track_cells(mapp):
    track = []
    rows, cols = len(mapp), len(mapp[0])
    for r in range(rows):
        for c in range(cols):
            if mapp[r][c] != '#':
                track.append((r, c))
    return track


def cheat_count(mapp, cheat_length, min_saving=100):

    S = find_item(mapp, 'S')
    E = find_item(mapp, 'E')

    dist_from_S = bfs(mapp, S, ignore_walls=False, max_steps=None)
    dist_from_E = bfs(mapp, E, ignore_walls=False, max_steps=None)

    T0 = dist_from_S[E[0]][E[1]]

    track_cells = find_all_track_cells(mapp)
    ignore_bfs = {}

    for cell in track_cells:
        ignore_bfs[cell] = bfs(mapp, cell, ignore_walls=True, max_steps=cheat_length)

    good_cheats = 0
    for A in track_cells:
        dist_s_a = dist_from_S[A[0]][A[1]]
        if dist_s_a is None:
            continue
        for B in track_cells:
            dist_a_b = ignore_bfs[A][B[0]][B[1]]
            if dist_a_b is None:
                continue
            dist_b_e = dist_from_E[B[0]][B[1]]
            if dist_b_e is None:
                continue
            T_cheat = dist_s_a + dist_a_b + dist_b_e
            saving = T0 - T_cheat
            if saving >= min_saving:
                good_cheats += 1
    return good_cheats


def part1(mapp):
    return cheat_count(mapp, cheat_length=2, min_saving=100)

def part2(mapp):
    return cheat_count(mapp, cheat_length=20, min_saving=100)

def solve(puzzle_input):
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        raw_text = pathlib.Path(path).read_text()
        data = parse_data(raw_text)
        answers = solve(data)
        print(path, *answers)
