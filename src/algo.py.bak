#!/usr/bin/env python3
"""
Docstring for algo
"""

import mazeparser
import visualize_maze
import random


steps = list()


def check_moves(maze, config, x, y) -> tuple:
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
        if not cell.is_visited() and not cell.frame:
            is_move_valid["N"] = True
    # Check South: y+1
    if y < config["HEIGHT"]:
        cell = maze[y + 1][x]
        if not cell.is_visited() and not cell.frame:
            is_move_valid["S"] = True
    # Check East: x+1
    if x < config["WIDTH"]:
        cell = maze[y][x + 1]
        if not cell.is_visited() and not cell.frame:
            is_move_valid["E"] = True
    # Check West: x-1
    if x > 1:  # x > 1 to avoid frame at x=0
        cell = maze[y][x - 1]
        if not cell.is_visited() and not cell.frame:
            is_move_valid["W"] = True
    return is_move_valid


def do_silent_next_move(maze, valid_moves, x, y):
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


def do_next_move(maze, valid_moves, x, y):
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
    maze[new_y][new_x].mark_visited()
    steps.append((new_x, new_y))
    return new_x, new_y


def remove_wall_between(maze: list, x: int, y: int, direction: str) -> None:
    """
    Docstring for change_cell_and_bit
    :param maze: Description
    :param cell: Description
    """
    N = 7   # 0111 - remove top wall
    E = 11  # 1011 - remove right wall
    S = 13  # 1101 - remove bottom wall
    W = 14  # 1110 - remove left wall
    if direction == "N":
        maze[y][x].set_wall(N)      # Remove top wall of current cell
        maze[y - 1][x].set_wall(S)  # Remove bottom wall of cell above
    if direction == "E":
        maze[y][x].set_wall(E)      # Remove right wall of current cell
        maze[y][x + 1].set_wall(W)  # Remove left wall of cell to the right
    if direction == "S":
        maze[y][x].set_wall(S)      # Remove bottom wall of current cell
        maze[y + 1][x].set_wall(N)  # Remove top wall of cell below
    if direction == "W":
        maze[y][x].set_wall(W)      # Remove left wall of current cell
        maze[y][x - 1].set_wall(E)  # Remove right wall of cell to the left


# def make_backtrack():

def generat_maze(maze, config, animate=False, delay=0.01):
    """
    Docstring for generat_maze
    :param config: Description
    :param animate: Wenn True, zeige Animation nach jedem Move
    :param delay: Verzögerung zwischen Frames (Sekunden)
    """
    import time
    
    #  macht das maze und erstellt den weg halt ha
    # Config coordinates are without frame, so add +1 offset
    entry_x, entry_y = config["ENTRY"]
    exit_x, exit_y = config["EXIT"]
    exit_x, exit_y = exit_x + 1, exit_y + 1  # Add frame
    x, y = entry_x + 1, entry_y + 1  # Add frame offset
    maze[y][x].mark_visited()
    maze[exit_x][exit_y].mark_visited()
    steps.append((x, y))
    
    # Start Live-Visualisierung
    if animate:
        visualize_maze.start_live_visualization(maze, config, current_pos=(x, y))
    
    # sowas wie eine last cell muss gespeichert werden um zu wissen welche
    # beiden wände entfernt werden müssen.
    exit_moves = check_moves(maze, config, exit_x, exit_y)  # open Exit Wall
    exit_x, exit_y = do_silent_next_move(maze, exit_moves, exit_x, exit_y)
    
    move_count = 0
    for i in range(999999999999999):
        valid_moves = check_moves(maze, config, x, y)
        x, y = do_next_move(maze, valid_moves, x, y)
        move_count += 1
        
        # Aktualisiere Live-Visualisierung für jeden Move
        if animate:
            visualize_maze.update_live_visualization(maze, config, current_pos=(x, y))
            time.sleep(delay)
        
        # remove_wall_between(maze, last_cell, (x, y)) muss hier gemacht werden
        if x == -1:
            if len(steps) > 0:
                x, y = steps.pop()
            else:
                break
    
    # Stoppe Live-Visualisierung
    if animate:
        visualize_maze.stop_live_visualization()


if __name__ == "__main__":
    maze, config = mazeparser.parse_maze_config()
    
    # Mit Animation (extrem schnell): animate=True, delay=0.00000000001
    # Ohne Animation (schnell): animate=False
    generat_maze(maze, config, animate=True, delay=0.00000000001)
    
    # Finale Visualisierung mit allen Details
    visualize_maze.visualize_cell_maze(maze, config, clear_screen=True)
