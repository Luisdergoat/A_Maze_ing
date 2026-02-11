"""
Docstring for main
"""


import os
import mazeparser
import visualize_maze as vizualizer
from mazegen_algo import generat_maze
from output_file import generate_output_file
from solve_maze_algo import maze_solve, maze_visualization


def main():
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
            # os.system("clear")
        except ValueError:
            os.system("clear")
            print("Enter a valid number")
            continue
        if option == 1:
            if result is not None:
                maze, config = result

                # Mit Animation (extrem schnell):
                # animate=True, delay=0.00000000001
                # Ohne Animation (schnell): animate=False
                generat_maze(
                    maze,
                    config,
                    animate=False,
                    delay=0.00000001,
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
                    animate=False,
                    delay=0.01
                )

                # Finale Visualisierung mit allen Details
                vizualizer.visualize_cell_maze(
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
            vizualizer.visualize_cell_maze_different_color(
                    maze,
                    config,
                    clear_screen=True,
                )
            continue
        elif option == 4:
            os.system("clear")
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
