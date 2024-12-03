"""Tests for AoC 3, 2024: Mull It Over."""

# Standard library imports
import pathlib

# Third party imports
import aoc202403
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202403.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202403.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202403.part1(example1) == 161


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202403.part2(example1) == ...


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202403.part2(example2) == 48
