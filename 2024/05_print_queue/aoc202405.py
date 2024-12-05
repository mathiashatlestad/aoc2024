"""AoC 5, 2024: Print Queue."""

# Standard library imports
import pathlib
import sys

from functools import cmp_to_key


custom_comp_data_left = {}


def custom_compare(item1, item2):
    item1_rule = custom_comp_data_left.get(item1, None)
    if item1_rule is not None and item2 in item1_rule:
        return -1
    item2_rule = custom_comp_data_left.get(item2, None)
    if item2_rule is not None and item1 in item2_rule:
        return 1

    return 0


def parse_data(puzzle_input):
    parts = puzzle_input.strip().split("\n\n")
    part1, part2 = parts[0], parts[1]

    list_of_rules = [tuple(map(int, line.split("|"))) for line in part1.splitlines()]

    for rule in list_of_rules:
        if rule[0] in custom_comp_data_left:
            custom_comp_data_left[rule[0]].append(rule[1])
        else:
            custom_comp_data_left[rule[0]] = [rule[1]]

    list_of_updates = [list(map(int, line.split(","))) for line in part2.splitlines()]

    return list_of_updates


def part1(data):
    sum = 0
    for update in data:
        sorted_data = sorted(update, key=cmp_to_key(custom_compare))
        if sorted_data == update:
            sum += update[int(len(update) / 2)]
    return sum


def part2(data):
    sum = 0
    for update in data:
        sorted_data = sorted(update, key=cmp_to_key(custom_compare))
        if sorted_data != update:
            sum += sorted_data[int(len(sorted_data) / 2)]

    return sum


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
