import sys
import pathlib
from collections import deque

DIRECTIONS = [
    (0, 1),   # down
    (0, -1),  # up
    (1, 0),   # right
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

def bfs_normal(mapp, start):
    rows, cols = len(mapp), len(mapp[0])
    dist = [[None]*cols for _ in range(rows)]
    queue = deque()
    r0, c0 = start
    dist[r0][c0] = 0
    queue.append((r0, c0))
    while queue:
        r, c = queue.popleft()
        for dr, dc in DIRECTIONS:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if mapp[nr][nc] != '#' and dist[nr][nc] is None:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
    return dist

def bfs_ignore_walls_limited(mapp, start, max_steps):
    rows, cols = len(mapp), len(mapp[0])
    dist = [[None]*cols for _ in range(rows)]
    queue = deque()
    r0, c0 = start
    dist[r0][c0] = 0
    queue.append((r0, c0))
    while queue:
        r, c = queue.popleft()
        for dr, dc in DIRECTIONS:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if dist[nr][nc] is None:
                    new_cost = dist[r][c] + 1
                    if new_cost <= max_steps:
                        dist[nr][nc] = new_cost
                        queue.append((nr, nc))
    return dist

def find_track_cells(mapp):
    track = []
    rows, cols = len(mapp), len(mapp[0])
    for r in range(rows):
        for c in range(cols):
            if mapp[r][c] != '#':
                track.append((r, c))
    return track

def part1(mapp):
    S = find_item(mapp, 'S')
    E = find_item(mapp, 'E')

    # 1) BFS for normal cost from S
    dist_from_S = bfs_normal(mapp, S)
    # 2) BFS for normal cost from E
    dist_from_E = bfs_normal(mapp, E)

    # Baseline no-cheat cost T0
    T0 = dist_from_S[E[0]][E[1]]
    if T0 is None:
        # If there's no path at all, puzzle is ill-posed or map is impossible
        return 0

    # Gather all track cells
    track_cells = find_track_cells(mapp)

    # For each track cell, precompute BFS ignoring walls (up to 2 steps).
    # We'll store them in a dictionary: cheat_dist[(r, c)] = 2D-dist-array
    cheat_dist_map = {}
    for cell in track_cells:
        cheat_dist_map[cell] = bfs_ignore_walls_limited(mapp, cell, max_steps=2)

    # Now enumerate all pairs of track cells (A, B).
    # The cheat is: S -> A (normal), A -> B (ignore walls, <=2 steps), B -> E (normal).
    # If the ignoring-walls distance is None or >2, skip.  Must also land on track again.
    # Then saving = T0 - total_time.  If >= 100 => count that cheat.
    # Distinct cheats are determined by (A, B).
    good_cheats = 0
    for A in track_cells:
        aS = dist_from_S[A[0]][A[1]]  # cost S->A
        if aS is None:
            continue
        for B in track_cells:
            distAtoB = cheat_dist_map[A][B[0]][B[1]]
            if distAtoB is None:  # can't cheat from A->B in <=2 steps
                continue
            bE = dist_from_E[B[0]][B[1]]  # cost B->E
            if bE is None:
                continue
            T_cheat = aS + distAtoB + bE
            saving = T0 - T_cheat
            if saving >= 100:
                good_cheats += 1
    return good_cheats

def part2(mapp):
    S = find_item(mapp, 'S')
    E = find_item(mapp, 'E')
    dist_from_S = bfs_normal(mapp, S)
    dist_from_E = bfs_normal(mapp, E)
    T0 = dist_from_S[E[0]][E[1]]
    if T0 is None:
        return 0

    track_cells = find_track_cells(mapp)

    # Precompute ignoring-walls BFS up to 20 steps from each track cell
    cheat_dist_map = {}
    for cell in track_cells:
        cheat_dist_map[cell] = bfs_ignore_walls_limited(mapp, cell, max_steps=20)

    good_cheats = 0
    for A in track_cells:
        aS = dist_from_S[A[0]][A[1]]
        if aS is None:
            continue
        for B in track_cells:
            distAtoB = cheat_dist_map[A][B[0]][B[1]]
            if distAtoB is None:
                continue
            bE = dist_from_E[B[0]][B[1]]
            if bE is None:
                continue
            T_cheat = aS + distAtoB + bE
            saving = T0 - T_cheat
            if saving >= 100:
                good_cheats += 1
    return good_cheats

def solve(puzzle_input):
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        mapp = parse_data(pathlib.Path(path).read_text())
        answers = solve(mapp)
        print(path, *answers)
