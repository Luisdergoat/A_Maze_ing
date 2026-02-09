#!/usr/bin/env python3
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
        self.wall = 15
        self.visited = False
        self.frame = False

    def __repr__(self):
        return f"Cell(x={self.x}, y={self.y}, is_visited={self.visited})"

    def mark_visited(self):
        self.visited = True

    def unvisit(self):
        self.visited = False

    def is_visited(self) -> bool:
        return self.visited

    def set_x(self, x: int) -> None:
        self.x = x

    def set_y(self, y: int) -> None:
        self.y = y

    def set_wall(self, direction: int) -> None:
        self.wall = self.wall & direction

    def get_wall(self) -> int:
        return self.wall

    def mark_as_frame(self):
        self.frame = True
