"""AoC 14, 2024: Restroom Redoubt."""
import functools
# Standard library imports
import pathlib
import sys
from PIL import Image

def parse_data(puzzle_input):
    """Parse input."""
    result = []
    for line in puzzle_input.strip().split("\n"):
        position_part, velocity_part = line.split(" ")
        px, py = map(int, position_part[2:].split(","))
        vx, vy = map(int, velocity_part[2:].split(","))
        result.append(((px, py), (vx, vy)))
    return result

@functools.lru_cache(maxsize=None)
def resulting_position(pos, vel, max_pos, iterations):
    res_x = (pos[0]+iterations*vel[0])%max_pos[0]
    if res_x < 0:
        res_x = max_pos[0] - res_x

    res_y = (pos[1]+iterations*vel[1])%max_pos[1]
    if res_y < 0:
        res_y = max_pos[1] - res_y

    return (res_x, res_y)


def calculate_weight(results, max_pos):
    half_x, half_y = max_pos[0] // 2, max_pos[1] // 2

    first = sum(results.count((x, y)) for x in range(half_x) for y in range(half_y))
    second = sum(results.count((x, y)) for x in range(half_x) for y in range(half_y+1, max_pos[1]))
    third = sum(results.count((x, y)) for x in range(half_x+1, max_pos[0]) for y in range(half_y))
    forth = sum(results.count((x, y)) for x in range(half_x+1, max_pos[0]) for y in range(half_y+1, max_pos[1]))

    return first * second * third * forth

def part1(data):
    """Solve part 1."""
    result = []
    max_pos = (101, 103)
    for item in data:
        result.append(resulting_position(item[0], item[1], max_pos, 100))
    return calculate_weight(result, max_pos)


def part2(data):
    """Solve part 2."""
    max_pos = (101, 103)
    iterations = 0

    for _ in range(10000):
        img = Image.new('RGB', (103, 103), "white")
        pix = img.load()
        for index, item in enumerate(data):
            res = resulting_position(item[0], item[1], max_pos, 1)
            data[index] = (res, item[1])
            pix[res[0], res[1]] = (255, 0, 0)
        iterations += 1
        img.save("pictures/" + str(iterations) + ".png")

    return iterations


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
