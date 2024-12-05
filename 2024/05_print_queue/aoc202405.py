"""AoC 5, 2024: Print Queue."""

# Standard library imports
import pathlib
import sys

from functools import cmp_to_key


def parse_data(puzzle_input):
    parts = puzzle_input.strip().split("\n\n")
    rules = {}
    for line in parts[0].splitlines():
        l, r = map(int, line.split("|"))
        rules.setdefault(l, []).append(r)
    sorting_func = lambda a, b: -1 if b in rules.get(a, []) else (1 if a in rules.get(b, []) else 0)
    updates = [list(map(int, line.split(","))) for line in parts[1].splitlines()]
    return updates, sorting_func


def part1(updates, sorting_func):
    total = 0
    for update in updates:
        sorted_update = sorted(update, key=cmp_to_key(sorting_func))
        if sorted_update == update:
            total += sorted_update[int(len(sorted_update) / 2)]
    return total


def part2(updates, sorting_func):
    total = 0
    for update in updates:
        sorted_update = sorted(update, key=cmp_to_key(sorting_func))
        if sorted_update != update:
            total += sorted_update[int(len(sorted_update) / 2)]
    return total


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data, sorting_func = parse_data(puzzle_input)
    yield part1(data, sorting_func)
    yield part2(data, sorting_func)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
