"""
Docstring for main
"""


import os
from intro_animation import play_intro
import mazeparser
import visualize_maze as vizualizer
from mazegen_algo import generat_maze
from output_file import generate_output_file
from solve_maze_algo import maze_solve, maze_visualization, different_color
from pyfiglet import figlet_format


def main():
    os.system("clear")  # mach fuer die animation ein pre clear, damit cleaner
    play_intro()  # Optional: Intro Animation fuer den WoW Effect in der eval
    os.system("clear")
    color = "default"
    while True:
        result = mazeparser.parse_maze_config()
        print("Choose on of the options")
        print("1: generate Maze")
        print("2: edit config")
        print("3: change colour (geht nicht)")
        print("4: exit")
        print("5: exit with cleanup")
        try:
            option = int(input("Choose option: "))
            os.system("clear")
        except ValueError:
            os.system("clear")
            print("Enter a valid number")
            continue
        if option == 1:

            if result is not None:
                if color == "default":
                    maze, config = result

                    # Mit Animation (extrem schnell):
                    # animate=True, delay=0.00000000001
                    # Ohne Animation (schnell): animate=False
                    generat_maze(
                        maze,
                        config,
                        animate=True,
                        delay=0.00000001,
                        color=color,
                    )
                    # Löse das Maze und markiere den Lösungsweg
                    solution = maze_solve(
                        maze,
                        config,
                    )
                    # os.system("clear")
                    maze_visualization(
                        maze,
                        config,
                        solution,
                        animate=True,
                        delay=0.01,
                    )

                    # Finale Visualisierung mit allen Details
                    vizualizer.visualize_cell_maze(
                        maze,
                        config,
                        clear_screen=True,
                    )

                elif color == "changed":
                    maze, config = result

                    # Mit Animation (extrem schnell):
                    # animate=True, delay=0.00000000001
                    # Ohne Animation (schnell): animate=False
                    generat_maze(
                        maze,
                        config,
                        animate=True,
                        delay=0.00000001,
                        color=color,
                    )
                    # Löse das Maze und markiere den Lösungsweg
                    solution = maze_solve(
                        maze,
                        config,
                    )
                    # os.system("clear")
                    different_color(
                        maze,
                        config,
                        solution,
                        animate=True,
                        delay=0.01,
                    )

                    # Finale Visualisierung mit allen Details
                    vizualizer.visualize_cell_maze_different_color(
                        maze,
                        config,
                        clear_screen=True,
                    )

                # Ausgabe der maze.txt Datei
                generate_output_file(maze, config)

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
            print("Enter a valid number")
            continue


if __name__ == "__main__":
    main()
