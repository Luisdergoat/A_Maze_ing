#!/usr/bin/env python3
"""
Hier wir die logik genommen aus der config.txt werden die regel eingesetzt
und in ein maze umgewandelt.
"""
from typing import Dict, List, Optional, Tuple, Union
from cell import Cell

import os


def read_out_config(
    file_path: str,
) -> Optional[Dict[str, Union[int, bool, str, Tuple[int, int]]]]:
    """
    Nimmt die werte aus der Config.txt
    und gibt sie als dictionary zurueck
    die keys werden dann noch in integer und boolean umgewandelt.
    """
    config: Dict[str, Union[int, bool, str, Tuple[int, int]]] = {}

    try:
        #  Versucht die config datei zu oeffnen und die werte in ein Dict macht
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue  # Skip empty lines and comments

                if '=' not in line:
                    continue  # Skip lines without '='

                key, value = line.split('=', 1)
                if value.isdigit():
                    config[key] = int(value)
                elif value.lower() in ['true']:
                    config[key] = True
                else:
                    config[key] = value

        #  checked ob alle Werte auch gegeben wurden
        required_keys = [
            "WIDTH",
            "HEIGHT",
            "ENTRY",
            "EXIT",
            "OUTPUT_FILE",
            "PERFECT",
            "42PATTERN",
            "SEED",
        ]

        for key in required_keys:
            if key not in config:
                raise ValueError(f"Missing required config key:{key}")

        #  checked ob die werte fuer die groesse des mazes passen
        width: int = 0
        height: int = 0
        for i in config:
            if i == "WIDTH":
                val = config[i]
                assert isinstance(val, int)
                width = val
            if i == "HEIGHT":
                val = config[i]
                assert isinstance(val, int)
                height = val
            if i == "ENTRY" or i == "EXIT":
                val = config[i]
                if isinstance(val, str):
                    x, y = val.split(',')
                    config[i] = (int(x.strip()), int(y.strip()))

        if width < 3 or height < 3:
            raise ValueError(
                "The Maze turned out to small. "
                "At least 3x3 is required."
            )
        entry_tuple = config['ENTRY']
        exit_tuple = config['EXIT']
        if not isinstance(entry_tuple, tuple) or len(entry_tuple) != 2:
            raise ValueError("ENTRY must be a tuple of two integers")
        if not isinstance(exit_tuple, tuple) or len(exit_tuple) != 2:
            raise ValueError("EXIT must be a tuple of two integers")
        entry_x, entry_y = int(entry_tuple[0]), int(entry_tuple[1])
        exit_x, exit_y = int(exit_tuple[0]), int(exit_tuple[1])
        if not -1 < entry_x < width:
            raise ValueError("The entry is out of bounds.")
        if not -1 < entry_y < height:
            raise ValueError("The entry is out of bounds.")
        if not -1 < exit_x < width:
            raise ValueError("The exit is out of bounds.")
        if not -1 < exit_y < height:
            raise ValueError("The exit is out of bounds.")
        if config['ENTRY'] == config['EXIT']:
            raise ValueError("The entry and exit points must be different.")

    except FileNotFoundError as e:
        print("ERROR: The config.txt file was not found ", e)
        return None
    except Exception as e:
        print(
            "ERROR: An error occurred while reading the config file: "
            f"{e}"
        )
        return None
    return config


def parse_maze_config(
) -> Optional[
    Tuple[List[List[Cell]], Dict[str, Union[int, bool, str, Tuple[int, int]]]]
]:
    """
    Also die funktion macht die validierung der config werte,
    hier wird sich um die logik des Mazes auf Bit ebene gekuemmert.
    Das Maze wird erst einmal als 2D-Liste von Zellen dargestellt,
    ohne korrekten Weg zzwischen Entry und Exit.
    """

    project_root = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(project_root, "config.txt")
    config = read_out_config(config_path)
    if config is None:
        return None

    #  Initialisiere das Maze mit cells anstadt ints
    # maze[y][x] mit y=0..HEIGHT+1, x=0..WIDTH+1
    # Der Frame ist bei x=0, x=WIDTH+1, y=0, y=HEIGHT+1
    width_val = config["WIDTH"]
    height_val = config["HEIGHT"]
    assert isinstance(width_val, int)
    assert isinstance(height_val, int)
    width = width_val
    height = height_val
    maze = [
        [Cell(x, y) for x in range(width + 2)]
        for y in range(height + 2)
    ]

    # Markiere Frame-Zellen (Rand)
    for y in range(height + 2):
        for x in range(width + 2):
            if (x == 0 or x == width + 1 or y == 0 or y == height + 1):
                maze[y][x].mark_as_frame()

    return maze, config
