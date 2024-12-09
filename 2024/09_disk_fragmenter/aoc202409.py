"""AoC 9, 2024: Disk Fragmenter."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [int(char) for char in puzzle_input]


def find_last(l, start_index):
    for index in range(start_index, -1, -1):  # Iterate backwards from start_index-1
        if l[index] >= 0:
            return index
    return -1  # If no non-negative element is found


def find_first_empty_element(l, start_index):
    for index in range(start_index, len(l)):  # Iterate from start_index to the end
        if l[index] < 0:
            return index
    return -1  # If no empty element is found


def part1(data):
    """Solve part 1."""
    l = []
    file = True
    curr_id = 0
    for index, value_size in enumerate(data):
        for i in range(0, value_size):
            if file:
                l.append(curr_id)
            else:
                l.append(-1)
        if file:
            curr_id+=1

        file = not file

    index_last = len(l) - 1
    index_first = 0

    while True:
        index_last = find_last(l, index_last)
        index_first = find_first_empty_element(l, index_first)
        if index_last <= index_first:
            break
        temp = l[index_last]
        l[index_last] = l[index_first]
        l[index_first] = temp

    total = 0
    exp = 0
    for index, value in enumerate(l):
        if value > 0:
            total += value*exp
        exp = exp+1

    return total

def part2(data):
    """Solve part 2."""


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
