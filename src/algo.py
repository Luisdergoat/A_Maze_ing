"""
Docstring for algo
"""

import mazeparser
import visualize_maze
import random


def check_moves(maze, x, y) -> tuple:
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
    try:
        if maze[x][y - 1].is_visited() is False:
            is_move_valid["N"] = True
    except IndexError:
        pass
    try:
        if maze[x][y + 1].is_visited() is False:
            is_move_valid["S"] = True
    except IndexError:
        pass
    try:
        if maze[x + 1][y].is_visited() is False:
            is_move_valid["E"] = True
    except IndexError:
        pass
    try:
        if maze[x - 1][y].is_visited() is False:
            is_move_valid["W"] = True
    except IndexError:
        pass

    return is_move_valid


def do_next_move(is_move_valid, x, y):
    """
    Docstring for do_next_move
    :param directions: Description
    """
    true_count = 0
    key = None
    for key in is_move_valid:
        if is_move_valid[key] is True:
            true_count += 1
    if true_count == 0:
        return -1, -1
    while True:
        key = random.choice(list(is_move_valid.keys()))
        if is_move_valid[key]:
            break
        break
    if key == "N":
        return x, y - 1
    if key == "E":
        return x + 1, y
    if key == "S":
        return x, y + 1
    if key == "W":
        return x - 1, y


def remove_wall_between(maze, last_cell, new_cell):
    """
    Docstring for change_cell_and_bit
    :param maze: Description
    :param cell: Description
    """
    #  hier muss ich die wände entfernen
    #  also die wände zwischen den zellen entfernen
    #  das ist aber auch nur für die visualisierung wichtig


def generat_maze(maze, config):
    """
    Docstring for generat_maze
    :param config: Description
    """
    #  macht das maze und erstellt den weg halt ha
    maze, config = mazeparser.parse_maze_config()
    x, y = config["ENTRY"]
    # sowas wie eine last cell muss gespeichert werden um zu wissen welche
    # beiden wände entfernt werden müssen.
    while True:
        is_move_valid = check_moves(maze, x, y)
        x, y = do_next_move(is_move_valid, x, y)
        # remove_wall_between(maze, last_cell, (x, y)) muss hier gemacht werden
        visualize_maze.visualize_cell_maze(maze, config)
        if x == -1:
            return 0  # backtracking() #  dieser muellige algo da
    maze[0][0].mark_visited()


if __name__ == "__main__":
    maze, config = mazeparser.parse_maze_config()
    generat_maze(maze, config)
    # Visualisiere das Maze
    visualize_maze.visualize_cell_maze(maze, config)
