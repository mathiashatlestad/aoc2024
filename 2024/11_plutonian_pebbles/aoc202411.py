"""AoC 11, 2024: Plutonian Pebbles."""
import functools
# Standard library imports
import pathlib
import sys
from collections import defaultdict
import time

def parse_data(puzzle_input):
    return list(map(int, puzzle_input.split()))

@functools.lru_cache(None)
def split_stone(number):
    if number == 0:
        return [1]
    s = str(number)
    mid = len(s) // 2
    return [int(s[:mid]), int(s[mid:])] if len(s) % 2 == 0 else [number * 2024]

def solve_for_blinks(data, blinks):
    stones = defaultdict(lambda: (0, 0), {s: (1, 0) for s in data})
    for i in range(blinks):
        even, odd, new_stones = i % 2 == 0, i % 2 == 1, defaultdict(lambda: (0, 0))
        for stone, (a, b) in stones.items():
            if a * even + b * odd:
                stones[stone] = (a * odd, b * even)
                for new_stone in split_stone(stone):
                    na, nb = new_stones[new_stone]
                    new_stones[new_stone] = (na + b * odd, nb + a * even)
        stones.update({k: (stones[k][0] + a, stones[k][1] + b) for k, (a, b) in new_stones.items()})
    return sum(sum(pair) for pair in stones.values())

def part1(data):
    t0 = time.time()
    res = solve_for_blinks(data, 25)
    t1 = time.time()
    print(f"Part 1 time: {(t1 - t0) * 1000} ms ")
    return res

def part2(data):
    t0 = time.time()
    res = solve_for_blinks(data, 75)
    t1 = time.time()
    print(f"Part 2 time: {(t1 - t0) * 1000} ms ")
    return res

def solve(puzzle_input):
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
