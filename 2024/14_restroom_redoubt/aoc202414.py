"""AoC 14, 2024: Restroom Redoubt."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    result = []
    for line in puzzle_input.strip().split("\n"):
        position_part, velocity_part = line.split(" ")
        px, py = map(int, position_part[2:].split(","))
        vx, vy = map(int, velocity_part[2:].split(","))
        result.append(((px, py), (vx, vy)))
    return result

def resulting_position(pos, vel, max_pos, iterations):
    res_x = (pos[0]+iterations*vel[0])%max_pos[0]
    if res_x < 0:
        res_x = max_pos[0] - res_x

    res_y = (pos[1]+iterations*vel[1])%max_pos[1]
    if res_y < 0:
        res_y = max_pos[1] - res_y

    return res_x, res_y

def calculate_weight(results, max_pos):

    first = 0
    for x in range(0, (max_pos[0] // 2)):
        for y in range(0, (max_pos[1] // 2)):
            first += results.count((x, y))

    second = 0
    for x in range(0, (max_pos[0] // 2)):
        for y in range((max_pos[1] // 2) + 1, max_pos[1]):
            second += results.count((x, y))

    third = 0
    for x in range((max_pos[0] // 2) + 1, max_pos[0]):
        for y in range(0, (max_pos[1] // 2)):
            third += results.count((x, y))

    forth = 0
    for x in range((max_pos[0] // 2) + 1 , max_pos[0]):
        for y in range((max_pos[1] // 2) + 1, max_pos[1]):
            forth += results.count((x, y))

    return first * second * third * forth


def part1(data):
    """Solve part 1."""
    print(data)
    result = []
    max_pos = (101, 103)
    for item in data:
        result.append(resulting_position(item[0], item[1], max_pos, 100))

    print(result)
    array = ""
    for j in range(max_pos[1]):
        tmp = ""
        for i in range(max_pos[0]):
            if (i,j) in result:
                tmp+="x"
            else:
                tmp += "."
        array += tmp + "\n"

    print(array)

    return calculate_weight(result, max_pos)


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
