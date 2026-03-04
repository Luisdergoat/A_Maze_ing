"""
Docstring for main
"""

from __future__ import annotations

import os
import sys
import termios
import tty
from typing import Dict, List, Optional, Tuple, Union

from mazegen.cell import Cell
from option_menu import play_option_menu
from intro_animation import play_intro
import mazeparser
from mazegen.mazegen_algo import generat_maze, check_42 
from output_file import generate_output_file
from pyfiglet import figlet_format
from solve_maze_algo import different_color, maze_solve, maze_visualization
import visualize_maze as vizualizer
try:
    import visualize_maze
except ImportError:
    pass

ConfigValue = Union[int, bool, str, Tuple[int, int]]
Config = Dict[str, ConfigValue]
Maze = List[List[Cell]]


def wait_for_keypress(prompt: str = "Press any key to return...") -> None:
    if prompt:
        print(prompt, end="", flush=True)
    if not sys.stdin.isatty():
        input()
        return
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def main() -> None:
    os.system("clear")  # clear before intro animation
    play_intro()  # Optional: Intro Animation fuer den WoW Effect in der eval
    os.system("clear")
    color = "default"
    maze: Optional[Maze] = None
    config: Optional[Config] = None
    show_path = True
    color = "default"
    while True:
        result = mazeparser.parse_maze_config()
        option: int = play_option_menu()
        try:
            option = int(chr(option))
        except (ValueError, TypeError):
            option = 0

        if option == 1:
            if result is None:
                wait_for_keypress()
                continue
            maze, config = result
            os.system("clear")
            generat_maze(
                maze,
                config,
                animate=True,
                delay=0.001,
                color=color,
            )

            if check_42(maze, config) is False:
                print("ERROR: entry or exit is in 42 pattern.")
                wait_for_keypress()
                continue

            solution = maze_solve(maze, config)
            os.system("clear")

            if color == "default":
                maze_visualization(
                    maze,
                    config,
                    solution,
                    animate=show_path,
                    delay=0.1,
                )
                vizualizer.visualize_cell_maze(
                    maze,
                    config,
                    clear_screen=True,
                    has_path=show_path,
                )
            else:
                different_color(
                    maze,
                    config,
                    solution,
                    animate=show_path,
                    delay=0.1,
                )
                vizualizer.visualize_cell_maze_different_color(
                    maze,
                    config,
                    clear_screen=True,
                    has_path=show_path,
                )
            generate_output_file(maze, config, solution)
            wait_for_keypress()
        elif option == 2:
            os.system(f"nvim {sys.argv[1]}")
            continue

        elif option == 3:
            if color == "default":
                color = "changed"
            elif color == "changed":
                color = "default"

            if maze is not None and color == "changed":
                vizualizer.visualize_cell_maze_different_color(
                    maze,
                    config,
                    clear_screen=True,
                    has_path=show_path,
                )
            elif maze is not None and color == "default":
                vizualizer.visualize_cell_maze(
                    maze,
                    config,
                    clear_screen=True,
                    has_path=show_path,
                )
            else:
                os.system("clear")
                print(
                    figlet_format(
                        "Generate a maze first to see it",
                        font="big"
                    )
                )
            wait_for_keypress()

        elif option == 4:
            os.system("clear")
            try:
                if show_path is True:
                    show_path = False
                    if color == "default":
                        vizualizer.visualize_cell_maze(
                            maze,
                            config,
                            clear_screen=True,
                            has_path=show_path,
                        )
                    else:
                        vizualizer.visualize_cell_maze_different_color(
                            maze,
                            config,
                            clear_screen=True,
                            has_path=show_path,
                        )
                elif show_path is False:
                    show_path = True
                    if color == "default":
                        vizualizer.visualize_cell_maze(
                            maze,
                            config,
                            clear_screen=True,
                            has_path=show_path,
                        )
                    else:
                        vizualizer.visualize_cell_maze_different_color(
                            maze,
                            config,
                            clear_screen=True,
                            has_path=show_path,
                        )

            except Exception:
                print(
                    figlet_format(
                        "Generate a maze first to to toggle the path",
                        font="big"
                    )
                )
            wait_for_keypress()

        elif option == 5:
            os.system("clear")
            print(figlet_format("Try Again!", font="slant"))
            return

        elif option == 6:
            os.system("clear")
            os.system("make fclean")
            return

        else:
            os.system("clear")
            print("Enter a valid number, not:", option)
            continue


if __name__ == "__main__":
    main()
