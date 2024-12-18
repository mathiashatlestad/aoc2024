"""AoC 17, 2024: Chronospatial Computer."""

# Standard library imports
import pathlib
import sys
import re
from operator import truediv


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
        return -1, -1

    output = -1
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
        output = combo % 8
    elif opcode == 6:
        registers['B'] = registers['A'] // (2 ** combo)
    elif opcode == 7:
        registers['C'] = registers['A'] // (2 ** combo)

    return ptr + 2, output

def part1(data):
    """Solve part 1."""
    registers, program = parse_data(data)
    outputs = []
    ptr = 0
    while ptr >= 0:
        ptr, output = perform_instruction(ptr, registers, program)
        if output >= 0:
            outputs.append(str(output))

    return ','.join(outputs)

def part2(data):

    """Solve part 2."""
    registers, program = parse_data(data)
    b_org = registers['B']
    c_org = registers['C']
    found = False
    register_a_value = 4675000000
    while found is False:
        outputs = []
        ptr = 0
        register_a_value += 1
        registers['A'] = register_a_value
        registers['B'] = b_org
        registers['C'] = c_org
        if register_a_value % 1000000 == 0:
            print(register_a_value)

        while ptr >= 0:
            ptr, output = perform_instruction(ptr, registers, program)
            if output >= 0:
                outputs.append(output)

            if outputs == program:
                found = True
                break

            if is_subarray_prefix(outputs, program) is False:
                found = False
                break

    return register_a_value


def is_subarray_prefix(subarray, main_array):
    if len(subarray) == 0:
        return True

    # Check if the length of subarray is greater than main_array
    if len(subarray) > len(main_array):
        return False

    # Compare the subarray with the start of the main array
    return main_array[:len(subarray)] == subarray

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    yield part1(puzzle_input)
    yield part2(puzzle_input)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
