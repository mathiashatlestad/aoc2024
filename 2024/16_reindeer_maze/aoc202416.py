"""AoC 16, 2024: Warehouse Woes."""

import pathlib
import sys
import heapq

sys.setrecursionlimit(2000)

DIRECTION_VECTORS = [(-1,0),(0,1),(1,0),(0,-1)]
TURN_COST = 1000

def parse_data(puzzle_input):
    if isinstance(puzzle_input, str):
        lines = puzzle_input.split('\n')
    else:
        lines = puzzle_input
    return [list(line) for line in lines if line]

def find_item(mapp, c):
    for i, row in enumerate(mapp):
        for j, col in enumerate(row):
            if col == c:
                return (i, j)

def dijkstra_with_turns(maze, start, end):
    N, M = len(maze), len(maze[0])

    INF = 10**15

    dist = [[[INF]*4 for _ in range(M)] for __ in range(N)]

    start_y, start_x = start
    dist[start_y][start_x][1] = 0
    pq = []
    heapq.heappush(pq, (0, start_y, start_x, 1))

    while pq:
        cost, y, x, d = heapq.heappop(pq)
        if cost > dist[y][x][d]:
            continue

        dy, dx = DIRECTION_VECTORS[d]
        ny, nx = y+dy, x+dx
        if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] != '#':
            new_cost = cost + 1
            if new_cost < dist[ny][nx][d]:
                dist[ny][nx][d] = new_cost
                heapq.heappush(pq, (new_cost, ny, nx, d))

        d_left = (d - 1) % 4
        new_cost = cost + TURN_COST
        if new_cost < dist[y][x][d_left]:
            dist[y][x][d_left] = new_cost
            heapq.heappush(pq, (new_cost, y, x, d_left))

        d_right = (d + 1) % 4
        new_cost = cost + TURN_COST
        if new_cost < dist[y][x][d_right]:
            dist[y][x][d_right] = new_cost
            heapq.heappush(pq, (new_cost, y, x, d_right))

    end_y, end_x = end
    min_end_cost = min(dist[end_y][end_x])

    on_best_path = [[[False]*4 for _ in range(M)] for __ in range(N)]

    stack = []
    for d in range(4):
        if dist[end_y][end_x][d] == min_end_cost:
            on_best_path[end_y][end_x][d] = True
            stack.append((end_y, end_x, d))

    while stack:
        cy, cx, cd = stack.pop()
        c_cost = dist[cy][cx][cd]
        dy, dx = DIRECTION_VECTORS[cd]
        py, px = cy - dy, cx - dx
        if 0 <= py < N and 0 <= px < M and maze[py][px] != '#':
            if dist[py][px][cd] + 1 == c_cost:
                if not on_best_path[py][px][cd]:
                    on_best_path[py][px][cd] = True
                    stack.append((py, px, cd))

        cd_left = (cd + 1) % 4
        if dist[cy][cx][cd_left] + TURN_COST == c_cost:
            if not on_best_path[cy][cx][cd_left]:
                on_best_path[cy][cx][cd_left] = True
                stack.append((cy, cx, cd_left))

        cd_right = (cd - 1) % 4
        if dist[cy][cx][cd_right] + TURN_COST == c_cost:
            if not on_best_path[cy][cx][cd_right]:
                on_best_path[cy][cx][cd_right] = True
                stack.append((cy, cx, cd_right))

    # Extract tiles on best paths
    best_tiles = set()
    for r in range(N):
        for c in range(M):
            for dd in range(4):
                if on_best_path[r][c][dd]:
                    best_tiles.add((r, c))
                    break

    return min_end_cost, best_tiles


def part1(maze):
    start = find_item(maze, 'S')
    end = find_item(maze, 'E')
    cost, _ = dijkstra_with_turns(maze, start, end)
    return cost


def part2(maze):
    start = find_item(maze, 'S')
    end = find_item(maze, 'E')
    _, best_tiles = dijkstra_with_turns(maze, start, end)
    return len(best_tiles)


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
