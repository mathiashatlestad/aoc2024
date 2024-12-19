"""AoC 19, 2024: Linen Layout."""
import functools
# Standard library imports
import pathlib
import sys

sys.setrecursionlimit(10 ** 6)

patterns = []

def parse_data(puzzle_input):
    """Parse input."""
    parts = puzzle_input.split("\n\n")

    global patterns
    patterns = [pattern.strip() for pattern in parts[0].strip().split(",")]

    designs = parts[1].strip().split("\n")
    return designs

@functools.lru_cache(maxsize=None)
def is_possible(design):
    for pattern in patterns:
        if pattern == design:
            return True
        if design.startswith(pattern):
            if is_possible(design[:len(pattern)]) and (len(pattern) >= len(design) or is_possible(design[len(pattern):])):
                return True

    return False

@functools.lru_cache(maxsize=None)
def is_possible_count(design):
    permutation = 0
    for pattern in patterns:
        if pattern == design:
            permutation += 1
        elif design.startswith(pattern):
            permutation += is_possible_count(design[:len(pattern)])
            permutation += is_possible_count(design[len(pattern):]) if len(design) > len(pattern) else 0
    return permutation

def part1(data):
    """Solve part 1."""
    designs = parse_data(data)
    print(patterns)
    print(designs)
    count = 0
    for design in designs:
        if is_possible(design):
            count += 1
    return count

def part2(data):
    """Solve part 2."""
    designs = parse_data(data)
    print(patterns)
    print(designs)
    count = 0
    for design in designs:
        count += is_possible_count(design)
    return count


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    yield part1(puzzle_input)
    yield part2(puzzle_input)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
