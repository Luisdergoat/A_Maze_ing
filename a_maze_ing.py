#!/usr/bin/env python3

import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(ROOT_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)


def start_program() -> None:
    """starts the program"""
    import start

    start.main()


if __name__ == "__main__":
    start_program()
