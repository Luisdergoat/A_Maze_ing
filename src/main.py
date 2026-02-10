"""
Docstring for main
"""


from mazegen_algo import generat_maze, generate_output_file
import mazeparser
from solve_maze_algo import solve_maze_with_visualization
import visualize_maze as vizualizer


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
            animate=True,
            delay=0.000000001,
        )
        # Löse das Maze und markiere den Lösungsweg
        solution = solve_maze_with_visualization(
            maze,
            config,
            animate=True,
            delay=0.1,
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