"""AoC 11, 2024: Plutonian Pebbles."""
import functools
# Standard library imports
import pathlib
import sys
from collections import defaultdict


def parse_data(puzzle_input):
    """Parse input."""
    return list(map(int, puzzle_input.split()))

def countDigit(n):
    # Base case
    if n == 0:
        return 1

    count = 0

    # Iterate till n has digits remaining
    while n != 0:
        # Remove rightmost digit
        n = n // 10

        # Increment digit count by 1
        count += 1

    return count

@functools.lru_cache(maxsize=None)
def split_number(number):

    if number == 0:
        return [1]

    digits = countDigit(number)
    if (digits % 2) == 0:
        s = str(number)
        return [int(s[:digits//2]), int(s[digits//2:])]

    return [number*2024]

import collections

def solve_for_blinks(data, blinks):

    nums = defaultdict()
    for num in data:
        nums[num] = (1, 0)

    for i in range(0, blinks):
        exp1 = i % 2 == 0
        exp2 = i % 2 != 0
        new_items = []
        for key, values in nums.items():
            (nu, nx) = values
            if nu * exp1 + nx * exp2 == 0:
                continue

            nums[key] = (nu * exp2, nx * exp1)
            for res in split_number(key):
                new_items.append((nx * exp2, nu * exp1, res))

        for new_it in new_items:
            nums.setdefault(new_it[2], (0, 0))
            nums[new_it[2]] = tuple(x + y for x, y in zip(nums[new_it[2]], (new_it[0], new_it[1])))

    total = 0
    for num in nums.values():
        total += num[0] + num[1]

    return total

def part1(data):
    """Solve part 1."""
    return solve_for_blinks(data, 25)

def part2(data):
    """Solve part 2."""
    return solve_for_blinks(data, 75)


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
