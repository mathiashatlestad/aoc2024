"""AoC 11, 2024: Plutonian Pebbles."""
import functools
# Standard library imports
import pathlib
import sys
from collections import defaultdict
import time

def parse_data(puzzle_input):
    """Parse input."""
    return list(map(int, puzzle_input.split()))

@functools.lru_cache(None)
def split_number(number):
    if number == 0:
        return [1]
    s = str(number)
    mid = len(s) // 2
    return [int(s[:mid]), int(s[mid:])] if len(s) % 2 == 0 else [number * 2024]

def solve_for_blinks(data, blinks):
    nums = defaultdict(lambda: (0, 0), {num: (1, 0) for num in data})

    for i in range(blinks):
        even, odd, new_items = i % 2 == 0, i % 2 == 1, defaultdict(lambda: (0, 0))

        for key, (nu, nx) in nums.items():
            if nu * even + nx * odd:
                nums[key] = (nu * odd, nx * even)
                for res in split_number(key):
                    a, b = new_items[res]
                    new_items[res] = (a + nx * odd, b + nu * even)

        nums.update({k: (nums[k][0] + nu, nums[k][1] + nx) for k, (nu, nx) in new_items.items()})

    return sum(sum(pair) for pair in nums.values())


def part1(data):
    t0 = time.time()
    """Solve part 1."""
    res = solve_for_blinks(data, 25)
    t1 = time.time()
    print(f"Part 1 time: {(t1 - t0) * 1000} ms ")
    return res


def part2(data):
    """Solve part 2."""
    t0 = time.time()
    """Solve part 1."""
    res = solve_for_blinks(data, 75)
    t1 = time.time()
    print(f"Part 2 time: {(t1 - t0) * 1000} ms ")
    return res


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
