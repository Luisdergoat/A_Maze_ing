"""
Docstring for cell
"""


class Cell:
    """
    Class representing a cell in the maze.
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.visited = False

    def __repr__(self):
        return f"Cell(x={self.x}, y={self.y}, is_visited={self.visited})"

    def mark_visited(self):
        self.visited = True

    def is_visited(self) -> bool:
        return self.visited
