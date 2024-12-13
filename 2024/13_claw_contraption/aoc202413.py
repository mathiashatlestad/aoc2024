"""AoC 13, 2024: Claw Contraption."""
import functools
# Standard library imports
import pathlib
import sys
import re

def parse_data(puzzle_input):
    """Parse input."""
    pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
    matches = re.findall(pattern, puzzle_input)
    results = []
    for match in matches:
        a_x, a_y, b_x, b_y, prize_x, prize_y = map(int, match)
        results.append((a_x, a_y, b_x, b_y, prize_x, prize_y))
    return results

@functools.lru_cache(maxsize=None)
def price(rem_prize_x, rem_prize_y, a_x, a_y, b_x, b_y):
    if rem_prize_x < 0 or rem_prize_y < 0:
        return 10000000000000

    if rem_prize_x == 0 and rem_prize_y == 0:
        return 0

    price_a = 3 + price(rem_prize_x-a_x, rem_prize_y-a_y, a_x, a_y, b_x, b_y)
    price_b = 1 + price(rem_prize_x-b_x, rem_prize_y-b_y, a_x, a_y, b_x, b_y)

    if price_b is not None and price_a is not None:
        return min(price_a, price_b)

    if price_a is not None:
        return price_a

    if price_b is not None:
        return price_b

    return 10000000000000

def part1(data):
    """Solve part 1."""
    tokens = 0
    for a_x, a_y, b_x, b_y, prize_x, prize_y in data:
        smallest = price(prize_x, prize_y, a_x, a_y, b_x, b_y)
        if smallest < 100000000000000000000000000:
            tokens += smallest
    return tokens

def part2(data):
    """Solve part 2."""
    tokens = 0
    for a_x, a_y, b_x, b_y, prize_x, prize_y in data:
        prize_x += 10000000000000
        prize_y += 10000000000000

        least_common_denominator = a_x*b_x*a_y*b_y
        prize_x = prize_x // least_common_denominator
        prize_y = prize_y // least_common_denominator

        smallest = price(prize_x, prize_y, a_x, a_y, b_x, b_y)
        if smallest < 10000000000000000000000000000000:
            tokens += smallest*least_common_denominator
    return tokens

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
