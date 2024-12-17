"""AoC 17, 2024: Chronospatial Computer."""

# Standard library imports
import pathlib
import sys
import re


def parse_data(puzzle_input):
    """Parse input."""
    registers = {'A': 0, 'B': 0, 'C': 0}
    program = []
    for line in puzzle_input.strip().split("\n"):
        if line.startswith("Register"):
            match = re.match(r"Register (\w): (\d+)", line)
            if match:
                reg, value = match.groups()
                registers[reg] = int(value)
        elif line.startswith("Program:"):
            program = list(map(lambda x: int(x), line.split(":")[1].split(",")))
    return registers, program


def perform_instruction(ptr, registers, program):
    if len(program) <= ptr+1:
        return -1, None

    output = None
    opcode = program[ptr]
    literal = program[ptr+1]

    if literal <= 3:
        combo = literal
    elif literal == 4:
        combo = registers['A']
    elif literal == 5:
        combo = registers['B']
    elif literal == 6:
        combo = registers['C']
    else:
        raise ValueError('invalid combo operand')

    if opcode == 0: # adv
        registers['A'] = registers['A'] // (2 ** combo)
    elif opcode == 1:
        registers['B'] = registers['B'] ^ literal
    elif opcode == 2:
        registers['B'] = combo % 8
    elif opcode == 3:
        if registers['A'] != 0:
            return literal, output
    elif opcode == 4:
        registers['B'] = registers['B'] ^ registers['C']
    elif opcode == 5:
        output = str(combo % 8)
    elif opcode == 6:
        registers['B'] = registers['A'] // (2 ** combo)
    elif opcode == 7:
        registers['C'] = registers['A'] // (2 ** combo)
    else:
        raise ValueError('invalid opcode')

    return ptr + 2, output

def part1(data):
    ptr = 0
    """Solve part 1."""
    registers, program = parse_data(data)
    print(registers)
    print(program)
    outputs = ""
    while ptr >= 0:
        ptr, output = perform_instruction(ptr, registers, program)
        if output:
            outputs += output
    print(registers)

    print(pow(2, 0))

    if outputs == "210462420":
        exit("WRONG")

    return outputs

def part2(data):
    """Solve part 2."""


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    yield part1(puzzle_input)
    yield part2(puzzle_input)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
