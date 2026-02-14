"""
Docstring for main
"""

from __future__ import annotations

import os
from typing import Dict, List, Optional, Tuple, Union

from cell import Cell
from option_menu import play_option_menu
from intro_animation import play_intro
import mazeparser
from mazegen_algo import generat_maze
from output_file import generate_output_file
from pyfiglet import figlet_format
from solve_maze_algo import different_color, maze_solve, maze_visualization
import visualize_maze as vizualizer

ConfigValue = Union[int, bool, str, Tuple[int, int]]
Config = Dict[str, ConfigValue]
Maze = List[List[Cell]]


def main() -> None:
    os.system("clear")  # clear before intro animation
    play_intro()  # Optional: Intro Animation fuer den WoW Effect in der eval
    os.system("clear")
    color = "default"
    maze: Optional[Maze] = None
    config: Optional[Config] = None
    while True:
        result = mazeparser.parse_maze_config()
        option = play_option_menu()
        try:
            option = int(chr(option))
        except (ValueError, TypeError):
            option = None
        if option == 1:
            os.system("clear")
            if result is None:
                print("Config konnte nicht gelesen werden.")
                continue

            maze, config = result
            generat_maze(
                maze,
                config,
                animate=True,
                delay=0.1,
                color=color,
            )
            solution = maze_solve(maze, config)
            os.system("clear")

            if color == "default":
                maze_visualization(
                    maze,
                    config,
                    solution,
                    animate=True,
                    delay=0.1,
                )
                vizualizer.visualize_cell_maze(
                    maze,
                    config,
                    clear_screen=True,
                )
            else:
                different_color(
                    maze,
                    config,
                    solution,
                    animate=True,
                    delay=0.1,
                )
                vizualizer.visualize_cell_maze_different_color(
                    maze,
                    config,
                    clear_screen=True,
                )
            generate_output_file(maze, config, solution)
            input()
        elif option == 2:
            os.system("nvim config.txt")
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
                )
            elif maze is not None and color == "default":
                vizualizer.visualize_cell_maze(
                    maze,
                    config,
                    clear_screen=True,
                )
            else:
                os.system("clear")
                print(
                    figlet_format(
                        "Generate a maze first to change the color",
                        font="big"
                    )
                )
            continue
        elif option == 4:
            os.system("clear")
            print(figlet_format("Try Again!", font="slant"))
            return
        elif option == 5:
            os.system("clear")
            os.system("make fclean")
            return
        else:
            os.system("clear")
            print("Enter a valid number, not:", option)
            continue


if __name__ == "__main__":
    main()
