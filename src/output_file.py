#!/usr/bin/env python3


from typing import Dict, Sequence, Tuple, Union


def generate_output_file(
    maze: Sequence[Sequence[object]],
    config: Dict[str, Union[int, bool, str, Tuple[int, int]]],
) -> None:
    """generate the output_maze.txt"""
    entry_tuple = config['ENTRY']
    exit_tuple = config['EXIT']
    assert isinstance(entry_tuple, tuple)
    assert isinstance(exit_tuple, tuple)
    entry_x, entry_y = entry_tuple
    exit_x, exit_y = exit_tuple
    output_file = str(config['OUTPUT_FILE'])
    height_val = config['HEIGHT']
    width_val = config['WIDTH']
    assert isinstance(height_val, int)
    assert isinstance(width_val, int)
    with open(output_file, "w") as f:
        for row in maze[1:height_val + 1]:
            for cell in row[1:width_val + 1]:
                f.write(f"{hex(cell.get_wall())[2:]}")  # type: ignore
            f.write("\n")
        f.write("\n")
        f.write(f"{entry_x},{entry_y}\n")
        f.write(f"{exit_x},{exit_y}\n")
