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



def count_digit(n):
    if n == 0:
        return 1
    count = 0
    while n != 0:
        n = n // 10
        count += 1
    return count


@functools.lru_cache(maxsize=None)
def split_number(number):
    if number == 0:
        return [1]
    digits = count_digit(number)
    if (digits % 2) == 0:
        s = str(number)
        return [int(s[:digits//2]), int(s[digits//2:])]
    return [number*2024]


def solve_for_blinks(data, blinks):
    nums = defaultdict(lambda: (0, 0))
    for num in data:
        nums[num] = (1, 0)

    for i in range(blinks):
        is_even = i % 2 == 0
        is_odd = not is_even

        new_items = defaultdict(lambda: (0, 0))

        for key, (nu, nx) in nums.items():
            if nu * is_even + nx * is_odd == 0:
                continue

            nums[key] = (nu * is_odd, nx * is_even)

            for res in split_number(key):
                current_nu, current_nx = new_items[res]
                new_items[res] = (
                    current_nu + nx * is_odd,
                    current_nx + nu * is_even,
                )

        for key, (nu, nx) in new_items.items():
            nums[key] = (
                nums[key][0] + nu,
                nums[key][1] + nx,
            )

    total = sum(nu + nx for nu, nx in nums.values())
    return total

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
