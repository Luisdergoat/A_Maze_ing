"""
Docstring for main
"""


import mazeparser
import visualize_maze as vizualizer
from mazegen_algo import generat_maze
from output_file import generate_output_file
from solve_maze_algo import maze_solve, maze_visualization


def main():
    result = mazeparser.parse_maze_config()
    if result is not None:
        maze, config = result

        # Mit Animation (extrem schnell):
        # animate=True, delay=0.00000000001
        # Ohne Animation (schnell): animate=False
        generat_maze(
            maze,
            config,
            animate=False,
            delay=0.000000001,
        )
        # Löse das Maze und markiere den Lösungsweg
        solution = maze_solve(
            maze,
            config,
        )
        maze_visualization(
            maze,
            config,
            solution,
            animate=False,
            delay=0.00000001
        )

        # Finale Visualisierung mit allen Details
        vizualizer.visualize_cell_maze(
            maze,
            config,
            clear_screen=True,
        )

        # Ausgabe der maze.txt Datei
        generate_output_file(maze, config)


if __name__ == "__main__":
    main()
