#!/usr/bin/env python3
"""
Docstring for algo
"""

import random
from typing import Dict, List, Sequence, Tuple, Union

import visualize_maze


steps: List[Tuple[int, int]] = []


def check_moves(
    maze: Sequence[Sequence[object]],
    config: Dict[str, Union[int, bool, str, Tuple[int, int]]],
    x: int,
    y: int,
) -> Dict[str, bool]:
    """
    Docstring for check_moves
    :param maze: Description
    :param cell: Description
    """
    is_move_valid = {
        "N": False,
        "E": False,
        "S": False,
        "W": False
    }
    # Check North: y-1
    if y > 1:  # y > 1 to avoid frame at y=0
        cell = maze[y - 1][x]
        if not cell.is_visited() and not cell.frame:  # type: ignore
            is_move_valid["N"] = True
    # Check South: y+1
    height_val = config["HEIGHT"]
    assert isinstance(height_val, int)
    if y < height_val:
        cell = maze[y + 1][x]
        if not cell.is_visited() and not cell.frame:  # type: ignore
            is_move_valid["S"] = True
    # Check East: x+1
    width_val = config["WIDTH"]
    assert isinstance(width_val, int)
    if x < width_val:
        cell = maze[y][x + 1]
        if not cell.is_visited() and not cell.frame:  # type: ignore
            is_move_valid["E"] = True
    # Check West: x-1
    if x > 1:  # x > 1 to avoid frame at x=0
        cell = maze[y][x - 1]
        if not cell.is_visited() and not cell.frame:  # type: ignore
            is_move_valid["W"] = True
    return is_move_valid


def do_silent_next_move(
    maze: Sequence[Sequence[object]],
    valid_moves: Dict[str, bool],
    x: int,
    y: int,
) -> Tuple[int, int]:
    """
    Docstring for do_next_move
    :param directions: Description
    """
    true_count = 0
    key = None
    for key in valid_moves:
        if valid_moves[key] is True:
            true_count += 1
    if true_count == 0:
        return -1, -1
    while True:
        key = random.choice(list(valid_moves.keys()))
        if valid_moves[key] is True:
            break
    if key == "N":
        remove_wall_between(maze, x, y, "N")
        new_x, new_y = x, y - 1
    if key == "E":
        remove_wall_between(maze, x, y, "E")
        new_x, new_y = x + 1, y
    if key == "S":
        remove_wall_between(maze, x, y, "S")
        new_x, new_y = x, y + 1
    if key == "W":
        remove_wall_between(maze, x, y, "W")
        new_x, new_y = x - 1, y
    return new_x, new_y


def do_next_move(
    maze: Sequence[Sequence[object]],
    valid_moves: Dict[str, bool],
    x: int,
    y: int,
) -> Tuple[int, int]:
    """
    Docstring for do_next_move
    :param directions: Description
    """
    print("next_move", x, y)
    true_count = 0
    key = None
    for key in valid_moves:
        if valid_moves[key] is True:
            true_count += 1
    if true_count == 0:
        return -1, -1
    while True:
        key = random.choice(list(valid_moves.keys()))
        if valid_moves[key] is True:
            break
    if key == "N":
        remove_wall_between(maze, x, y, "N")
        new_x, new_y = x, y - 1
    if key == "E":
        remove_wall_between(maze, x, y, "E")
        new_x, new_y = x + 1, y
    if key == "S":
        remove_wall_between(maze, x, y, "S")
        new_x, new_y = x, y + 1
    if key == "W":
        remove_wall_between(maze, x, y, "W")
        new_x, new_y = x - 1, y
    maze[new_y][new_x].mark_visited()  # type: ignore
    steps.append((new_x, new_y))
    return new_x, new_y


def remove_wall_between(
    maze: Sequence[Sequence[object]],
    x: int,
    y: int,
    direction: str,
) -> None:
    """
    Docstring for change_cell_and_bit
    :param maze: Description
    :param cell: Description
    """
    N = 7   # 0111
    E = 11  # 1011
    S = 13  # 1101
    W = 14  # 1110
    if direction == "N":
        maze[y][x].set_wall(N)  # type: ignore
        maze[y - 1][x].set_wall(S)  # type: ignore
    if direction == "E":
        maze[y][x].set_wall(E)  # type: ignore
        maze[y][x + 1].set_wall(W)  # type: ignore
    if direction == "S":
        maze[y][x].set_wall(S)  # type: ignore
        maze[y + 1][x].set_wall(N)  # type: ignore
    if direction == "W":
        maze[y][x].set_wall(W)  # type: ignore
        maze[y][x - 1].set_wall(E)  # type: ignore


def add_42_pattern(maze, config):
    """
    Docstring for add_42_patter
    :param maze: Description
    """
    height = config['HEIGHT'] + 1
    width = config['WIDTH'] + 1
    mid_x = int(height / 2)
    mid_y = int(width / 2)
    if height < 8 or width < 10:
        print("Maze is to small for 42 pattern")
        return
    # mark 4 as frame
    maze[mid_x][mid_y - 1].mark_as_frame()
    maze[mid_x + 1][mid_y - 1].mark_as_frame()
    maze[mid_x + 2][mid_y - 1].mark_as_frame()
    maze[mid_x][mid_y - 2].mark_as_frame()
    maze[mid_x][mid_y - 3].mark_as_frame()
    maze[mid_x - 1][mid_y - 3].mark_as_frame()
    maze[mid_x - 2][mid_y - 3].mark_as_frame()
    # mark 2 as frame
    maze[mid_x][mid_y + 1].mark_as_frame()
    maze[mid_x + 1][mid_y + 1].mark_as_frame()
    maze[mid_x + 2][mid_y + 1].mark_as_frame()
    maze[mid_x + 2][mid_y + 2].mark_as_frame()
    maze[mid_x + 2][mid_y + 3].mark_as_frame()
    maze[mid_x][mid_y + 2].mark_as_frame()
    maze[mid_x][mid_y + 3].mark_as_frame()
    maze[mid_x - 1][mid_y + 3].mark_as_frame()
    maze[mid_x - 2][mid_y + 3].mark_as_frame()
    maze[mid_x - 2][mid_y + 2].mark_as_frame()
    maze[mid_x - 2][mid_y + 1].mark_as_frame()


def generat_maze(
    maze: Sequence[Sequence[object]],
    config: Dict[str, Union[int, bool, str, Tuple[int, int]]],
    animate: bool = False,
    delay: float = 0.01,
) -> None:
    """
    Docstring for generat_maze
    :param config: Description
    :param animate: Wenn True, zeige Animation nach jedem Move
    :param delay: Verzögerung zwischen Frames (Sekunden)
    """
    import time

    #  macht das maze und erstellt den weg halt ha
    # Config coordinates are without frame, so add +1 offset
    entry_tuple = config["ENTRY"]
    exit_tuple = config["EXIT"]
    assert isinstance(entry_tuple, tuple)
    assert isinstance(exit_tuple, tuple)
    entry_x, entry_y = entry_tuple
    exit_x, exit_y = exit_tuple
    exit_x, exit_y = exit_x + 1, exit_y + 1  # Add frame
    x, y = entry_x + 1, entry_y + 1  # Add frame offset
    maze[y][x].mark_visited()  # type: ignore
    maze[exit_y][exit_x].mark_visited()  # type: ignore
    steps.append((x, y))

    # Start Live-Visualisierung
    if animate:
        visualize_maze.start_live_visualization(
            maze,
            config,
            current_pos=(x, y),
        )

    # handle seeds
    seed_val = config['SEED']
    try:
        seed_int = int(seed_val)  # type: ignore
    except ValueError:
        seed_int = random.randint(-2147483648, 2147483647)
    random.seed(seed_int)

    # add 42 pattern
    add_42_pattern(maze, config)

    exit_moves = check_moves(
        maze,
        config,
        exit_x,
        exit_y,
    )  # open Exit Wall
    exit_x, exit_y = do_silent_next_move(
        maze,
        exit_moves,
        exit_x,
        exit_y,
    )
    move_count = 0
    while True:
        valid_moves = check_moves(maze, config, x, y)
        x, y = do_next_move(
            maze,
            valid_moves,
            x,
            y,
        )
        move_count += 1

        # Aktualisiere Live-Visualisierung für jeden Move
        if animate:
            visualize_maze.update_live_visualization(
                maze,
                config,
                current_pos=(x, y),
            )
            time.sleep(delay)

        # remove_wall_between(maze, last_cell, (x, y))
        # muss hier gemacht werden
        perfect_maze = config["PERFECT"]
        if perfect_maze is False:
            pass
        if x == -1:
            if len(steps) > 0:
                x, y = steps.pop()
            else:
                break

    # Stoppe Live-Visualisierung
    if animate:
        visualize_maze.stop_live_visualization()
