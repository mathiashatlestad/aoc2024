"""AoC 9, 2024: Disk Fragmenter."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [int(char) for char in puzzle_input]


def find_last(l, to_find, start_index):
    count = 0
    target_value_index = 0
    for index in range(start_index, -1, -1):
        if l[index] == to_find:
            count += 1
            if count == 1:
                target_value_index = index
        elif count >= 1:
            break

    return target_value_index, count  # Return the starting position and count


def find_first_empty_element(l, start_index, require_size_in_a_row):
    consecutive_count = 0
    for index in range(start_index, len(l)):
        if l[index] < 0:
            consecutive_count += 1
            if consecutive_count == require_size_in_a_row:
                return index + 1 - require_size_in_a_row
        else:
            consecutive_count = 0  # Reset the count if the sequence is broken

    return None

def part2(data):
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

    to_find = curr_id - 1
    index_first = {}

    while to_find >= 0:
        tmp_index = -1
        while True:
            (index_last, count) = find_last(l, to_find, len(l) - 1)
            i_first = find_first_empty_element(l, index_first.get(count, 0), count)

            if i_first is None or (tmp_index == index_last or i_first >= index_last):
                break

            if l[index_last] != to_find:
                break

            index_first[count] = 0
            index_first[count-1] = i_first

            temp = l[index_last]
            l[index_last] = l[i_first]
            l[i_first] = temp
            tmp_index = index_last

        to_find-=1

    total = 0
    exp = 0
    for index, value in enumerate(l):
        if value > 0:
            total += value*exp
        exp = exp+1

    return total


def part1(data):
    """Solve part 1."""
    return -1
    l = []
    file = True
    curr_id = 0
    for index, value_size in enumerate(data):
        for i in range(0, value_size):
            l.append(curr_id if file else -1)
        if file:
            curr_id+=1

        file = not file

    index_last = len(l) - 1
    index_first = 0

    while True:
        (index_last, count) = find_last(l, -1, index_last)
        index_first = find_first_empty_element(l, index_first, 1)
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
