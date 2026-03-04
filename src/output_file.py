#!/usr/bin/env python3

from __future__ import annotations

from typing import Dict, Sequence, Tuple, Union, List

from mazegen.cell import Cell

ConfigValue = Union[int, bool, str, Tuple[int, int]]
Config = Dict[str, ConfigValue]


def reverse_first_4_bits(number: int) -> int:
    """reverse the first 4 bits"""
    binary_str = bin(number)[2:]
    binary_str = binary_str.zfill(4)
    first_4_bits = binary_str[:4]
    reversed_4_bits = first_4_bits[::-1]
    modified_binary_str = reversed_4_bits + binary_str[4:]
    reversed_number = int(modified_binary_str, 2)

    return reversed_number


def generate_output_file(
    maze: Sequence[Sequence[Cell]],
    config: Config,
    solution: List[Tuple[int, int]] | None
) -> None:
    """generate the output_maze.txt"""
    entry_tuple = config["ENTRY"]
    exit_tuple = config["EXIT"]
    assert isinstance(entry_tuple, tuple)
    assert isinstance(exit_tuple, tuple)
    entry_x, entry_y = entry_tuple
    exit_x, exit_y = exit_tuple
    output_file = str(config["OUTPUT_FILE"])
    height_val = config["HEIGHT"]
    width_val = config["WIDTH"]
    assert isinstance(height_val, int)
    assert isinstance(width_val, int)
    with open(output_file, "w", encoding="utf-8") as f:
        for row in maze[1:height_val + 1]:
            for cell in row[1:width_val + 1]:
                f.write(f"{hex(reverse_first_4_bits(cell.get_wall()))[2:]}")
            f.write("\n")
        f.write("\n")
        f.write(f"{entry_x},{entry_y}\n")
        f.write(f"{exit_x},{exit_y}\n")
        x = 0
        ix = 0
        y = 0
        iy = 0
        tup: tuple[int, int] = (0, 0)
        if solution is not None:
            for tup in solution:
                if x != 0 and y != 0 and ix != 0 and iy != 0:
                    if y < iy:
                        f.write("N")
                    if y > iy:
                        f.write("S")
                    if x > ix:
                        f.write("E")
                    if x < ix:
                        f.write("W")
                ix = x
                iy = y
                x, y = tup
        f.write("\n")
