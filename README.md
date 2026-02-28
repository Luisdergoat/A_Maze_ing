*This project has been created as part of the 42 curriculum by lunsold and jdreissi.*

# A_Maze_ing
A Python maze generator, terminal visualizer, and solver driven by a simple `config.txt`.

---

## Description
**A_Maze_ing** generates mazes from a configuration file, renders them in the terminal (using `rich`), and can automatically solve them from **ENTRY** to **EXIT**.

**Goal:** build a configurable maze tool with clear output, reproducibility (seeds), and optional “perfect” mazes (single-solution) vs. imperfect mazes (multiple paths).

---

## Instructions

### Requirements
- Python 3
- `make` (recommended)

### Install
```bash
git clone https://github.com/Luisdergoat/A_Maze_ing.git
cd A_Maze_ing
make install
```

### Run
```bash
make run
```

---

## Config file (complete structure & format)
The project is configured via a **root-level** `config.txt` using `KEY=VALUE` pairs:

```text
# Maze Configuration
WIDTH=20
HEIGHT=15
ENTRY=3, 2
EXIT=7, 13
OUTPUT_FILE=maze.txt
PERFECT=False
42PATTERN=True
SEED=random
```

**Fields**
- `WIDTH` (int): maze width
- `HEIGHT` (int): maze height
- `ENTRY` (`x, y`): start coordinate
- `EXIT` (`x, y`): end coordinate
- `OUTPUT_FILE` (string): output filename (e.g. `maze.txt`)
- `PERFECT` (bool): `True` = perfect maze (unique path), `False` = imperfect (can contain multiple paths)
- `42PATTERN` (bool): enables the optional “42” pattern feature
- `SEED` (int or `random`): fixed seed for reproducibility or random generation

---

## Maze generation algorithm
**Chosen algorithm:** *Recursive Backtracking* (Depth-First carving, implemented with a stack).

### Why this algorithm
- Produces classic “perfect maze” structure naturally (when `PERFECT=True`)
- Simple to implement, debug, and extend
- Fast and works well for many maze sizes
- Easy to animate step-by-step in a terminal UI

---

## Reusable parts (what & how)
- **Parsing/validation** (`src/mazeparser.py`): can be reused for any key-value config-driven tool.
- **Grid/cell representation** (`src/cell.py`): reusable cell model with compact wall encoding (bitmask).
- **Generation & solving logic** (`src/mazegen_algo.py`, `src/solve_maze_algo.py`): algorithms are modular and can be swapped/extended with additional strategies.
- **Visualization layer** (`src/visualize_maze.py`, `src/new_maze_visualizer.py`): can be reused to render other grid-based problems.
- **Export** (`src/output_file.py`): reusable exporter for grid data + metadata (entry/exit).

---

## Team & project management

### Team roles
- **jdreissi**: algorithm work (solver), core integration, config-driven workflow, CLI/menu,  build tooling (Makefile), overall structure
- **lunsold**: algorithm work (solver), visualization, testing/cleanup & refactoring (adapt as needed)

### Planning (expected → actual)
- **Planned:** config parser → generator → visualizer → solver → exporter → polish
- **Evolved:** additional visualization mode(s), optional features (perfect/imperfect, pattern, seed control), improved UX via Makefile + venv automation

### What worked well
- Clear separation of responsibilities (parse / generate / solve / render / export)
- Config-driven workflow simplified testing many maze variants quickly
- Seed support made debugging reproducible

### Tools used
- **Makefile** for install/run/clean workflows
- **Python venv** for dependency isolation
- **rich** for terminal rendering

---

## Advanced / optional features (if enabled)
- Perfect vs. imperfect mazes (`PERFECT`)
- Seed-based reproducibility (`SEED`)
- Optional 42-pattern insertion (`42PATTERN`)
- Multiple visualization approaches (standard + alternative visualizer)

---

## Resources
**Maze generation & pathfinding**
- Recursive backtracker (maze generation): https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_backtracker
- Depth-first search (DFS): https://en.wikipedia.org/wiki/Depth-first_search

**Python & terminal UI**
- Rich documentation: https://rich.readthedocs.io/
- Python venv: https://docs.python.org/3/library/venv.html

### AI usage (required disclosure)
AI was used for:
- README structure and wording (clarity, formatting, and completeness)
- Summarizing the project’s modules and explaining the algorithms in concise documentation form  
AI was **not** used to generate or modify the repository’s source code in this step.