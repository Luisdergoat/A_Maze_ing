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


def do_next_move(valid_moves, x, y):
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
        print("N")
        remove_wall_between(maze, x, y, "N")
        maze[x][y - 1].mark_visited()
        return x, y - 1
    if key == "E":
        print("E")
        remove_wall_between(maze, x, y, "E")
        maze[x + 1][y].mark_visited()
        return x + 1, y
    if key == "S":
        print("S")
        remove_wall_between(maze, x, y, "S")
        maze[x][y + 1].mark_visited()
        return x, y + 1
    if key == "W":
        print("W")
        remove_wall_between(maze, x, y, "W")
        maze[x - 1][y].mark_visited()
        return x - 1, y


def remove_wall_between(maze: list, x: int, y: int, direction: str) -> None:
    """
    Docstring for change_cell_and_bit
    :param maze: Description
    :param cell: Description
    """
    N = 7
    E = 11
    S = 13
    W = 14
    zu = 15 
    if direction == "N":
        maze[x][y].set_wall(N)
        maze[x][y - 1].set_wall(S)
    if direction == "E":
        maze[x][y].set_wall(E)
        maze[x + 1][y].set_wall(W)
    if direction == "S":
        maze[x][y].set_wall(S)
        maze[x][y + 1].set_wall(N)
    if direction == "W":
        maze[x][y].set_wall(W)
        maze[x - 1][y].set_wall(E)
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
    maze[x][y].mark_visited()
    # sowas wie eine last cell muss gespeichert werden um zu wissen welche
    # beiden wände entfernt werden müssen.
    while True:
        valid_moves = check_moves(maze, x, y)
        x, y = do_next_move(valid_moves, x, y)
        # remove_wall_between(maze, last_cell, (x, y)) muss hier gemacht werden
        # visualize_maze.visualize_cell_maze(maze, config)
        if x == -1:
            return 0  # backtracking() #  dieser muellige algo da
    maze[0][0].mark_visited()


if __name__ == "__main__":
    maze, config = mazeparser.parse_maze_config()
    generat_maze(maze, config)
    # # Visualisiere das Maze
    visualize_maze.visualize_cell_maze(maze, config)

