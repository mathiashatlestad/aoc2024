import functools
import pathlib
import sys

@functools.lru_cache(maxsize=None)
def solve(design):
    return 1 if not design else sum(solve(design[len(p):]) for p in patterns if design.startswith(p))

patterns_section, designs = pathlib.Path(sys.argv[1]).read_text().strip().split("\n\n")
patterns = [p.strip() for p in patterns_section.split(",")]
print(sum(solve(d) > 0 for d in designs.strip().splitlines())) # Part 1
print(sum(solve(d) for d in designs.strip().splitlines())) # Part 2