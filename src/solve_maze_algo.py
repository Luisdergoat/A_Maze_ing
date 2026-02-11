"""
Docstring for clearmazealgo
"""

import visualize_maze


###########################################################################
################ muss alles in clearmazealgo rein #########################
###########################################################################


def check_valid_moves(maze, x, y, visited):
    """
    Findet alle möglichen Bewegungen von aktueller Position.
    Nutzt Bit-Masken statt exakte Werte!
    """
    moves = []
    wall = maze[y][x].get_wall()  # Oder .wall je nach Implementierung

    # Check Norden (Bit 3 = 0 → offen)
    if not (wall & 8) and (x, y - 1) not in visited:
        if not maze[y - 1][x].frame:  # Nicht in Frame
            moves.append(('N', x, y - 1))

    # Check Osten (Bit 2 = 0 → offen)
    if not (wall & 4) and (x + 1, y) not in visited:
        if not maze[y][x + 1].frame:
            moves.append(('E', x + 1, y))

    # Check Süden (Bit 1 = 0 → offen)
    if not (wall & 2) and (x, y + 1) not in visited:
        if not maze[y + 1][x].frame:
            moves.append(('S', x, y + 1))

    # Check Westen (Bit 0 = 0 → offen)
    if not (wall & 1) and (x - 1, y) not in visited:
        if not maze[y][x - 1].frame:
            moves.append(('W', x - 1, y))

    return moves


def maze_solve(maze, config):
    # Entry und Exit holen (mit Frame-Offset)
    entry_tuple = config["ENTRY"]
    exit_tuple = config["EXIT"]
    assert isinstance(entry_tuple, tuple)
    assert isinstance(exit_tuple, tuple)

    start_x, start_y = entry_tuple[0] + 1, entry_tuple[1] + 1  # Frame offset
    exit_x, exit_y = exit_tuple[0] + 1, exit_tuple[1] + 1
    stack = [(start_x, start_y, [])]  # (x, y, path)
    visited = set()

    while stack:
        try:
            x, y, path = stack.pop()
        except ValueError:
            continue

        # Bereits besucht? Skip
        if (x, y) in visited:
            continue

        # Markiere als besucht
        visited.add((x, y))
        current_path = path + [(x, y)]

        # Exit erreicht?
        if x == exit_x and y == exit_y:
            print(f"Found Exit: length {len(current_path)}")
            return current_path

        # Finde alle möglichen Moves
        possible_moves = check_valid_moves(maze, x, y, visited)

        # Füge alle Moves zum Stack hinzu
        for direction, new_x, new_y in possible_moves:
            stack.append((new_x, new_y, current_path))

    print(" No solution found!")
    return None


def maze_visualization(
    maze,
    config,
    solution_path,
    animate: bool = True,
    delay: float = 0.01,
):
    """
    Löst Maze und markiert den Lösungsweg
    """
    import time

    if solution_path:
        if animate:
            visualize_maze.start_live_visualization(maze, config)

        # Markiere den finalen Lösungsweg
        for x, y in solution_path:
            maze[y][x].mark_need_to_solve()  # type: ignore

            if animate:
                visualize_maze.update_live_visualization(maze, config)
                time.sleep(delay)

        if animate:
            visualize_maze.stop_live_visualization()

        print(f"Pfadlänge: {len(solution_path)}")
        print(f"Start: {solution_path[0]}")
        print(f"Ende: {solution_path[-1]}")

        return solution_path

    return None
