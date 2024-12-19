"""AoC 19, 2024: Linen Layout."""
import functools
# Standard library imports
import pathlib
import sys

sys.setrecursionlimit(10 ** 6)

patterns = []

def parse_data(puzzle_input):
    """Parse input."""
    global patterns
    patterns_section, designs_section = puzzle_input.strip().split("\n\n", 1)
    patterns = [p.strip() for p in patterns_section.split(",")]
    designs = designs_section.strip().splitlines()
    return designs


@functools.lru_cache(maxsize=None)
def is_possible_count(design):
    return 1 if not design else sum(
        is_possible_count(design[len(pattern):])
        for pattern in patterns
        if design.startswith(pattern)
    )

def part1(designs):
    """Solve part 1."""
    return sum(is_possible_count(design) > 0 for design in designs)

def part2(designs):
    """Solve part 2."""
    return sum(is_possible_count(design) for design in designs)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    designs = parse_data(puzzle_input)
    yield part1(designs)
    yield part2(designs)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
