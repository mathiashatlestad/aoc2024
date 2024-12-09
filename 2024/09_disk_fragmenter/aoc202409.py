"""AoC 9, 2024: Disk Fragmenter."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [int(char) for char in puzzle_input]

def find_last(l):
    for index, x in enumerate(reversed(l)):
        if x >= 0:
            return len(l) - index - 1

def find_first_empty_element(l):
    for index, x in enumerate(l):
        if x < 0:
            return index
    return -1

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


    while True:
        last_index = find_last(l)
        first_empty_index = find_first_empty_element(l)
        if last_index <= first_empty_index:
            break
        temp = l[last_index]
        l[last_index] = l[first_empty_index]
        l[first_empty_index] = temp

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
