"""Tests for AoC 4, 2024: Ceres Search."""

# Standard library imports
import pathlib

# Third party imports
import aoc202404
import pytest
import numpy as np

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202404.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202404.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
    ['.', '.', 'X', '.', '.', '.'],
    ['.', 'S', 'A', 'M', 'X', '.'],
    ['.', 'A', '.', '.', 'A', '.'],
    ['X', 'M', 'A', 'S', '.', 'S'],
    ['.', 'X', '.', '.', '.', '.']
]


def test_part1_example1(example2):
    """Test part 1 on example input."""
    assert aoc202404.part1(example2) == 18


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202404.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202404.part2(example2) == ...
