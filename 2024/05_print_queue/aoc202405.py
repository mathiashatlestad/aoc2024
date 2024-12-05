"""AoC 5, 2024: Print Queue."""

# Standard library imports
import pathlib
import sys

from functools import cmp_to_key

def custom_compare(item1, item2, rules):
    if item2 in rules.get(item1, []):
        return -1
    if item1 in rules.get(item2, []):
        return 1
    return 0


def parse_data(puzzle_input):
    parts = puzzle_input.strip().split("\n\n")
    rules = {}
    for line in parts[0].splitlines():
        left, right = map(int, line.split("|"))
        rules.setdefault(left, []).append(right)
    updates = [list(map(int, line.split(","))) for line in parts[1].splitlines()]
    return updates, rules


def part1(updates, rules):
    total = 0
    for update in updates:
        sorted_update = sorted(update, key=cmp_to_key(lambda a, b: custom_compare(a, b, rules)))
        if sorted_update == update:
            total += sorted_update[int(len(sorted_update) / 2)]
    return total


def part2(updates, rules):
    total = 0
    for update in updates:
        sorted_update = sorted(update, key=cmp_to_key(lambda a, b: custom_compare(a, b, rules)))
        if sorted_update != update:
            total += sorted_update[int(len(sorted_update) / 2)]
    return total


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data, rules = parse_data(puzzle_input)
    yield part1(data, rules)
    yield part2(data, rules)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
