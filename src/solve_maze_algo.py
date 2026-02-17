"""
Docstring for clearmazealgo
"""

from __future__ import annotations

from typing import Dict, List, Optional, Sequence, Set, Tuple, Union

from cell import Cell
import visualize_maze as vis
from collections import deque

ConfigValue = Union[int, bool, str, Tuple[int, int]]
Config = Dict[str, ConfigValue]
Maze = Sequence[Sequence[Cell]]


def check_valid_moves(
    maze: Maze,
    x: int,
    y: int,
    visited: Set[Tuple[int, int]],
) -> List[Tuple[str, int, int]]:
    """
    Findet alle möglichen Bewegungen von aktueller Position.
    Nutzt Bit-Masken statt exakte Werte!
    """
    moves: List[Tuple[str, int, int]] = []
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


# gerade bug hier wir None returnt deswegen wir das Maze nicht gelöst
def maze_solve(
    maze: Maze,
    config: Config,
) -> Optional[List[Tuple[int, int]]]:

    # Entry und Exit holen (mit Frame-Offset)
    entry_tuple = config["ENTRY"]
    exit_tuple = config["EXIT"]
    assert isinstance(entry_tuple, tuple)
    assert isinstance(exit_tuple, tuple)

    start_x, start_y = entry_tuple[0] + 1, entry_tuple[1] + 1  # Frame offset
    exit_x, exit_y = exit_tuple[0] + 1, exit_tuple[1] + 1

    queue = deque([(start_x, start_y)])
    visited: Set[Tuple[int, int]] = set()
    visited.add((start_x, start_y))

    parent_map = {}

    while queue:
        x, y = queue.popleft()

        # Bereits besucht? Skip
        if (x, y) == (exit_x, exit_y):
            break

        for direction, new_x, new_y in check_valid_moves(maze, x, y, visited):
            visited.add((new_x, new_y))
            parent_map[(new_x, new_y)] = (x, y)
            queue.append((new_x, new_y))

    if (exit_x, exit_y) not in parent_map:
        return None  # Kein Pfad gefunden

    path = []
    current: Tuple[int, int] = (exit_x, exit_y)

    path.append(current)
    while current != (start_x, start_y):
        path.append(current)
        current = parent_map.get(current)  # type: ignore

    path.append((start_x, start_y))
    path.reverse()
    return path


def maze_visualization(
    maze: Maze,
    config: Config,
    solution_path: Optional[Sequence[Tuple[int, int]]],
    animate: bool = True,
    delay: float = 0.01,
) -> Optional[Sequence[Tuple[int, int]]]:
    """
    Löst Maze und markiert den Lösungsweg
    """
    import time

    if solution_path:
        if animate:
            vis.start_live_visualization(maze, config)

        # Markiere den finalen Lösungsweg
        for x, y in solution_path:
            maze[y][x].mark_need_to_solve()

            if animate:
                vis.update_live_visualization(maze, config)
                time.sleep(delay)

        if animate:
            vis.stop_live_visualization()

        return solution_path

    return None


def different_color(
    maze: Maze,
    config: Config,
    solution_path: Optional[Sequence[Tuple[int, int]]],
    animate: bool = True,
    delay: float = 0.01,
) -> Optional[Sequence[Tuple[int, int]]]:
    """
    Löst Maze und markiert den Lösungsweg
    """
    import time

    if solution_path:
        if animate:
            vis.start_live_visualization_different_color(maze, config)

        # Markiere den finalen Lösungsweg
        for x, y in solution_path:
            maze[y][x].mark_need_to_solve()

            if animate:
                vis.update_live_visualization_diff_color(maze, config)
                time.sleep(delay)

        if animate:
            vis.stop_live_visualization()

        return solution_path

    return None
