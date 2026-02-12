"""
Maze Visualizer - Zeigt ein Maze mit Wänden auf Bit-Ebene an.

Die Wände werden als 4-Bit-Zahl dargestellt:
- Bit 3 (8): Oben
- Bit 2 (4): Rechts
- Bit 1 (2): Unten
- Bit 0 (1): Links

Beispiel: 1111 (15) = alle Wände geschlossen
         0000 (0) = alle Wände offen
         1010 (10) = oben und unten geschlossen
"""

from __future__ import annotations

from typing import List, Mapping, Optional, Sequence, Tuple, Union

from cell import Cell
import mazeparser
from rich import box
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()

ConfigValue = Union[Tuple[int, int], int, bool, str]
ConfigMapping = Mapping[str, ConfigValue]
CellMaze = Sequence[Sequence[Cell]]


# Globale Variable für Live-Display
_live_display: Optional[Live] = None


def _require_int(config: ConfigMapping, key: str) -> int:
    value = config.get(key)
    if isinstance(value, int):
        return value
    raise ValueError(f"Config key {key} must be int")


def _get_entry_exit(
    config: ConfigMapping,
) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    entry_val = config.get("ENTRY")
    exit_val = config.get("EXIT")
    if isinstance(entry_val, tuple) and len(entry_val) == 2:
        entry = (int(entry_val[0]), int(entry_val[1]))
    else:
        entry = (0, 0)
    if isinstance(exit_val, tuple) and len(exit_val) == 2:
        exit_pos = (int(exit_val[0]), int(exit_val[1]))
    else:
        exit_pos = (0, 0)
    return entry, exit_pos


def start_live_visualization(
    cell_maze: CellMaze,
    config: ConfigMapping,
    current_pos: Optional[Tuple[int, int]] = None,
) -> Optional[Live]:
    """Startet Live-Visualisierung für Animation"""
    global _live_display

    maze = convert_cells_to_maze_array(cell_maze)
    if not maze:
        return None

    height = len(maze)
    width = len(maze[0]) if height > 0 else 0

    has_frame = False
    if cell_maze and cell_maze[0]:
        has_frame = cell_maze[0][0].frame

    entry, exit_pos = _get_entry_exit(config)
    entry_x, entry_y = entry
    exit_x, exit_y = exit_pos

    if has_frame:
        entry_x += 1
        entry_y += 1
        exit_x += 1
        exit_y += 1

    panel = print_maze_visual_rich(
        maze,
        width,
        height,
        entry_x,
        entry_y,
        exit_x,
        exit_y,
        cell_maze=cell_maze,
        has_frame=has_frame,
        current_pos=current_pos,
    )

    # Erstelle eine zentierte Version des Panels
    from rich.align import Align

    centered_panel = Align.center(panel)

    _live_display = Live(
        centered_panel,
        console=console,
        refresh_per_second=120,
    )
    _live_display.start()
    return _live_display


def start_live_visualization_different_color(
    cell_maze: CellMaze,
    config: ConfigMapping,
    current_pos: Optional[Tuple[int, int]] = None,
) -> Optional[Live]:
    """Startet Live-Visualisierung für Animation"""
    global _live_display

    maze = convert_cells_to_maze_array(cell_maze)
    if not maze:
        return None

    height = len(maze)
    width = len(maze[0]) if height > 0 else 0

    has_frame = False
    if cell_maze and cell_maze[0]:
        has_frame = cell_maze[0][0].frame

    entry, exit_pos = _get_entry_exit(config)
    entry_x, entry_y = entry
    exit_x, exit_y = exit_pos

    if has_frame:
        entry_x += 1
        entry_y += 1
        exit_x += 1
        exit_y += 1

    panel = change_maze_color(
        maze,
        width,
        height,
        entry_x,
        entry_y,
        exit_x,
        exit_y,
        cell_maze=cell_maze,
        has_frame=has_frame,
        current_pos=current_pos,
    )

    # Erstelle eine zentierte Version des Panels
    from rich.align import Align

    centered_panel = Align.center(panel)

    _live_display = Live(
        centered_panel,
        console=console,
        refresh_per_second=120,
    )
    _live_display.start()
    return _live_display


def update_live_visualization(
    cell_maze: CellMaze,
    config: ConfigMapping,
    current_pos: Optional[Tuple[int, int]] = None,
) -> None:
    """Aktualisiert Live-Visualisierung"""

    if _live_display is None:
        return

    maze = convert_cells_to_maze_array(cell_maze)
    if not maze:
        return

    height = len(maze)
    width = len(maze[0]) if height > 0 else 0

    has_frame = False
    if cell_maze and cell_maze[0]:
        has_frame = cell_maze[0][0].frame

    entry, exit_pos = _get_entry_exit(config)
    entry_x, entry_y = entry
    exit_x, exit_y = exit_pos

    if has_frame:
        entry_x += 1
        entry_y += 1
        exit_x += 1
        exit_y += 1

    panel = print_maze_visual_rich(
        maze,
        width,
        height,
        entry_x,
        entry_y,
        exit_x,
        exit_y,
        cell_maze=cell_maze,
        has_frame=has_frame,
        current_pos=current_pos,
    )

    from rich.align import Align

    centered_panel = Align.center(panel)
    _live_display.update(centered_panel)


def stop_live_visualization() -> None:
    """Stoppt Live-Visualisierung"""
    global _live_display

    if _live_display is not None:
        _live_display.stop()
        _live_display = None


def update_live_visualization_different_color(
    cell_maze: CellMaze,
    config: ConfigMapping,
    current_pos: Optional[Tuple[int, int]] = None,
) -> None:
    """Aktualisiert Live-Visualisierung"""

    if _live_display is None:
        return

    maze = convert_cells_to_maze_array(cell_maze)
    if not maze:
        return

    height = len(maze)
    width = len(maze[0]) if height > 0 else 0

    has_frame = False
    if cell_maze and cell_maze[0]:
        has_frame = cell_maze[0][0].frame

    entry, exit_pos = _get_entry_exit(config)
    entry_x, entry_y = entry
    exit_x, exit_y = exit_pos

    if has_frame:
        entry_x += 1
        entry_y += 1
        exit_x += 1
        exit_y += 1

    panel = change_maze_color(
        maze,
        width,
        height,
        entry_x,
        entry_y,
        exit_x,
        exit_y,
        cell_maze=cell_maze,
        has_frame=has_frame,
        current_pos=current_pos,
    )

    from rich.align import Align

    centered_panel = Align.center(panel)
    _live_display.update(centered_panel)


def convert_cells_to_maze_array(
    cell_maze: CellMaze,
) -> List[List[int]]:
    """
    Konvertiert ein 2D-Array von Cell-Objekten zu einem Bit-Maze Array.
    Verwendet die Wand-Bits aus Cell.get_wall()
    (Bits: Oben=8, Rechts=4, Unten=2, Links=1).
    Inkludiert alle Zellen inklusive Frame.
    """
    if not cell_maze or not cell_maze[0]:
        return []

    num_rows = len(cell_maze)
    num_cols = len(cell_maze[0]) if num_rows > 0 else 0

    if num_rows == 0 or num_cols == 0:
        return []

    # Create the maze array with all cells including frame
    result_maze: List[List[int]] = []
    for y in range(num_rows):
        row: List[int] = []
        for x in range(num_cols):
            cell = cell_maze[y][x]
            row.append(int(cell.get_wall()))
        result_maze.append(row)

    return result_maze


def visualize_cell_maze(
    cell_maze: CellMaze,
    config: ConfigMapping,
    clear_screen: bool = False,
    show_config: bool = True,
    show_table: bool = True,
) -> None:
    """
    Visualisiert ein Maze aus Cell-Objekten.
    Diese Funktion kann aus algo.py aufgerufen werden.
    :param cell_maze: 2D-Array von Cell-Objekten
    :param config: Config-Dictionary mit WIDTH, HEIGHT,
        ENTRY, EXIT
    :param clear_screen: Wenn True, wird der Bildschirm vorher gelöscht
        (für Animation)
    :param show_config: Zeige Config-Info
    :param show_table: Zeige Bit-Tabelle
    """
    if not cell_maze or not config:
        console.print("Fehler: Maze oder Config ist None")
        return

    # Clear screen for animation
    if clear_screen:
        console.clear()

    # Use actual maze dimensions instead of config values
    maze = convert_cells_to_maze_array(cell_maze)
    if not maze:
        console.print("Fehler: Konvertierung des Mazes fehlgeschlagen")
        return

    height = len(maze)
    width = len(maze[0]) if height > 0 else 0

    # Check if cell_maze has frame
    has_frame = False
    if cell_maze and cell_maze[0]:
        has_frame = cell_maze[0][0].frame

    # Adjust entry/exit coordinates if frame exists
    # Config coordinates refer to maze without frame
    entry, exit_pos = _get_entry_exit(config)
    entry_x, entry_y = entry
    exit_x, exit_y = exit_pos

    if has_frame:
        # Add 1 to account for frame border
        entry_x += 1
        entry_y += 1
        exit_x += 1
        exit_y += 1

    # Zeige visuelles Maze
    panel = print_maze_visual_rich(
        maze,
        width,
        height,
        entry_x,
        entry_y,
        exit_x,
        exit_y,
        cell_maze=cell_maze,
        has_frame=has_frame,
    )

    if show_config:
        from rich.align import Align

        config_panel = print_config_info(config)
        console.print(Align.center(config_panel))
        console.print()

    if clear_screen:
        console.clear()

    console.print(panel, justify="center")


def visualize_cell_maze_different_color(
    cell_maze: CellMaze,
    config: ConfigMapping,
    clear_screen: bool = False,
    show_config: bool = True,
    show_table: bool = True,
) -> None:
    """
    Visualisiert ein Maze aus Cell-Objekten.
    Diese Funktion kann aus algo.py aufgerufen werden.
    :param cell_maze: 2D-Array von Cell-Objekten
    :param config: Config-Dictionary mit WIDTH, HEIGHT,
        ENTRY, EXIT
    :param clear_screen: Wenn True, wird der Bildschirm vorher gelöscht
        (für Animation)
    :param show_config: Zeige Config-Info
    :param show_table: Zeige Bit-Tabelle
    """
    if not cell_maze or not config:
        console.print("Fehler: Maze oder Config ist None")
        return

    # Clear screen for animation
    if clear_screen:
        console.clear()

    # Use actual maze dimensions instead of config values
    maze = convert_cells_to_maze_array(cell_maze)
    if not maze:
        console.print("Fehler: Konvertierung des Mazes fehlgeschlagen")
        return

    height = len(maze)
    width = len(maze[0]) if height > 0 else 0

    # Check if cell_maze has frame
    has_frame = False
    if cell_maze and cell_maze[0]:
        has_frame = cell_maze[0][0].frame

    # Adjust entry/exit coordinates if frame exists
    # Config coordinates refer to maze without frame
    entry, exit_pos = _get_entry_exit(config)
    entry_x, entry_y = entry
    exit_x, exit_y = exit_pos

    if has_frame:
        # Add 1 to account for frame border
        entry_x += 1
        entry_y += 1
        exit_x += 1
        exit_y += 1

    # Zeige Config-Info
    # Zeige visuelles Maze
    panel = change_maze_color(
        maze,
        width,
        height,
        entry_x,
        entry_y,
        exit_x,
        exit_y,
        cell_maze=cell_maze,
        has_frame=has_frame,
    )

    if show_config:
        from rich.align import Align

        config_panel = print_config_info(config)
        console.print(Align.center(config_panel))
        console.print()

    if clear_screen:
        console.clear()

    console.print(panel, justify="center")


def print_config_info(config: ConfigMapping) -> Table:
    """
    Zeigt die Config-Informationen mit Rich an.
    """
    table = Table(
        title=(
            "[bold cyan]Maze "
            "Konfiguration[/bold cyan]"
        ),
        box=box.ROUNDED,
        border_style="cyan",
    )
    table.add_column("Parameter", style="yellow")
    table.add_column("Wert", style="green")

    entry, exit_pos = _get_entry_exit(config)
    table.add_row("Breite", str(config.get("WIDTH", "N/A")))
    table.add_row("Höhe", str(config.get("HEIGHT", "N/A")))
    table.add_row("Entry", f"{entry[0]}, {entry[1]}")
    table.add_row("Exit", f"{exit_pos[0]}, {exit_pos[1]}")
    table.add_row(
        "Perfect",
        str(config.get("PERFECT", "N/A")),
    )

    return table


def print_maze_visual_rich(
    maze: Sequence[Sequence[int]],
    width: int,
    height: int,
    entry_x: int,
    entry_y: int,
    exit_x: int,
    exit_y: int,
    cell_maze: Optional[CellMaze] = None,
    has_frame: bool = False,
    current_pos: Optional[Tuple[int, int]] = None,
) -> Panel:
    """
    Zeigt das Maze visuell mit Rich und farbigen ASCII-Zeichen an.
    Gibt ein Panel zurück für Live-Updates.

    Bits: Oben=8, Rechts=4, Unten=2, Links=1
    """
    # Validate dimensions
    if not maze or not maze[0]:
        return Panel(
            "Fehler: Maze ist leer",
            title="Maze",
            border_style="red",
        )

    actual_height = len(maze)
    actual_width = len(maze[0])

    maze_text = Text()

    # Top border
    line = Text()
    for x in range(actual_width):
        cell = maze[0][x]
        is_frame = False
        if cell_maze is not None:
            cell_obj = cell_maze[0][x]
            is_frame = cell_obj.frame

        color = "white" if is_frame else "white"

        if x == 0:
            line.append("┏", style=color)
        else:
            line.append("┳", style=color)

        if cell & 8:
            line.append("━━━", style=color)
        else:
            line.append("   ")

    line.append("┓", style="white")
    maze_text.append_text(line)
    maze_text.append("\n")

    # Zeichne jede Zeile
    for y in range(actual_height):
        # Content line
        line = Text()

        for x in range(actual_width):
            cell = maze[y][x]

            # Check for frame
            is_frame = False
            is_solving = False
            if cell_maze is not None:
                cell_obj = cell_maze[y][x]
                is_frame = cell_obj.frame
                is_solving = cell_obj.solve_need

            color = "white" if is_frame else "white"

            # Left wall
            if cell & 1:
                line.append("┃", style=color)
            else:
                line.append(" ")

            # Cell content
            if current_pos and (x, y) == current_pos:
                line.append(" ● ", style="bold red")
            elif (x, y) == (entry_x, entry_y):
                line.append(" E ", style="bold green")
            elif (x, y) == (exit_x, exit_y):
                line.append(" X ", style="bold red")
            elif is_frame:
                line.append("███", style="bold red")
            elif is_solving:
                line.append(" ■ ", style="bold blue")

            else:
                line.append("   ")

        # Right wall
        rightmost = maze[y][actual_width - 1]
        is_frame_right = False
        if cell_maze is not None:
            cell_obj = cell_maze[y][actual_width - 1]
            is_frame_right = cell_obj.frame

        color_right = "white" if is_frame_right else "white"
        if rightmost & 4:
            line.append("┃", style=color_right)
        else:
            line.append(" ")

        maze_text.append_text(line)
        maze_text.append("\n")

        # Bottom border line
        line = Text()
        for x in range(actual_width):
            cell = maze[y][x]

            is_frame = False
            if cell_maze is not None:
                cell_obj = cell_maze[y][x]
                is_frame = cell_obj.frame

            color = "white" if is_frame else "white"

            if x == 0:
                if y == actual_height - 1:
                    line.append("┗", style=color)
                else:
                    line.append("┣", style=color)
            else:
                if y == actual_height - 1:
                    line.append("┻", style=color)
                else:
                    line.append("╋", style=color)

            if cell & 2:
                line.append("━━━", style=color)
            else:
                line.append("   ")

        # Right edge
        is_frame_right = False
        if cell_maze is not None:
            cell_obj = cell_maze[y][actual_width - 1]
            is_frame_right = cell_obj.frame

        color_right = "white" if is_frame_right else "white"
        if y == actual_height - 1:
            line.append("┛", style="white")
        else:
            line.append("┫", style=color_right)

        maze_text.append_text(line)
        maze_text.append("\n")

    return Panel(
        maze_text,
        title=(
            "[bold green]Maze "
            "Generation[/bold green]"
        ),
        border_style="green",
        box=box.ROUNDED,
        expand=False,
    )


def change_maze_color(
    maze: Sequence[Sequence[int]],
    width: int,
    height: int,
    entry_x: int,
    entry_y: int,
    exit_x: int,
    exit_y: int,
    cell_maze: Optional[CellMaze] = None,
    has_frame: bool = False,
    current_pos: Optional[Tuple[int, int]] = None,
) -> Panel:
    """
    Zeigt das Maze visuell mit Rich und farbigen ASCII-Zeichen an.
    Gibt ein Panel zurück für Live-Updates.

    Bits: Oben=8, Rechts=4, Unten=2, Links=1
    """
    # Validate dimensions
    if not maze or not maze[0]:
        return Panel(
            "Fehler: Maze ist leer",
            title="Maze",
            border_style="pink",
        )

    actual_height = len(maze)
    actual_width = len(maze[0])

    maze_text = Text()

    # Top border
    line = Text()
    for x in range(actual_width):
        cell = maze[0][x]
        is_frame = False
        if cell_maze is not None:
            cell_obj = cell_maze[0][x]
            is_frame = cell_obj.frame

        color = "pink" if is_frame else "blue"

        if x == 0:
            line.append("┏", style=color)
        else:
            line.append("┳", style=color)

        if cell & 8:
            line.append("━━━", style=color)
        else:
            line.append("   ")

    line.append("┓", style="bold grey")
    maze_text.append_text(line)
    maze_text.append("\n")

    # Zeichne jede Zeile
    for y in range(actual_height):
        # Content line
        line = Text()

        for x in range(actual_width):
            cell = maze[y][x]

            # Check for frame
            is_frame = False
            is_solving = False
            if cell_maze is not None:
                cell_obj = cell_maze[y][x]
                is_frame = cell_obj.frame
                is_solving = cell_obj.solve_need

            color = "pink" if is_frame else "bold grey"

            # Left wall
            if cell & 1:
                line.append("┃", style=color)
            else:
                line.append(" ")

            # Cell content
            if current_pos and (x, y) == current_pos:
                line.append(" ● ", style="bold red")
            elif (x, y) == (entry_x, entry_y):
                line.append(" E ", style="bold green")
            elif (x, y) == (exit_x, exit_y):
                line.append(" X ", style="bold red")
            elif is_frame:
                line.append("███", style="bold cyan")
            elif is_solving:
                line.append(" ■ ", style="bold blue")
            else:
                line.append("   ")

        # Right wall
        rightmost = maze[y][actual_width - 1]
        is_frame_right = False
        if cell_maze is not None:
            cell_obj = cell_maze[y][actual_width - 1]
            is_frame_right = cell_obj.frame

        color_right = "pink" if is_frame_right else "bold grey"
        if rightmost & 4:
            line.append("┃", style=color_right)
        else:
            line.append(" ")

        maze_text.append_text(line)
        maze_text.append("\n")

        # Bottom border line
        line = Text()
        for x in range(actual_width):
            cell = maze[y][x]

            is_frame = False
            if cell_maze is not None:
                cell_obj = cell_maze[y][x]
                is_frame = cell_obj.frame

            color = "pink" if is_frame else "bold grey"

            if x == 0:
                if y == actual_height - 1:
                    line.append("┗", style=color)
                else:
                    line.append("┣", style=color)
            else:
                if y == actual_height - 1:
                    line.append("┻", style=color)
                else:
                    line.append("╋", style=color)

            if cell & 2:
                line.append("━━━", style=color)
            else:
                line.append("   ")

        # Right edge
        is_frame_right = False
        if cell_maze is not None:
            cell_obj = cell_maze[y][actual_width - 1]
            is_frame_right = cell_obj.frame

        color_right = "pink" if is_frame_right else "bold grey"
        if y == actual_height - 1:
            line.append("┛", style="bold grey")
        else:
            line.append("┫", style=color_right)

        maze_text.append_text(line)
        maze_text.append("\n")

    return Panel(
        maze_text,
        title=(
            "[bold green]Maze "
            "Generation[/bold green]"
        ),
        border_style="red",
        box=box.ROUNDED,
        expand=False,
    )


def visualize_maze(config_path: str) -> None:
    """
    Liest die Config-Datei und visualisiert das Maze mit Rich.
    """
    config = mazeparser.read_out_config(config_path)
    if config is None:
        console.print("Fehler beim Lesen der Config-Datei.")
        return

    width = _require_int(config, "WIDTH")
    height = _require_int(config, "HEIGHT")
    entry, exit_pos = _get_entry_exit(config)
    entry_x, entry_y = entry
    exit_x, exit_y = exit_pos

    # Erstelle ein 2D-Array für die Wände
    # (standard alle Wände zu = 15)
    maze = [
        [15 for _ in range(width)]
        for _ in range(height)
    ]

    # Beispiel: Öffne einige Wände für einen Pfad
    # Du kannst dies anpassen oder einen Algorithmus verwenden
    # Bits: Oben=8, Rechts=4, Unten=2, Links=1

    # Entry-Punkt: Beispielwert beibehalten
    if 0 <= entry_y < height and 0 <= entry_x < width:
        maze[entry_y][entry_x] = 15

    # Exit-Punkt: Beispielwert für alle Wände offen
    if 0 <= exit_y < height and 0 <= exit_x < width:
        maze[exit_y][exit_x] = 0

    # Zeige Config-Info
    console.print(print_config_info(config))
    console.print()

    # Zeige visuelles Maze
    print_maze_visual_rich(
        maze,
        width,
        height,
        entry_x,
        entry_y,
        exit_x,
        exit_y,
    )


def load_maze_from_file(file_path: str) -> Optional[List[List[int]]]:
    """
    Lädt ein Maze aus einer Datei, wo jede Zelle als Bit-Zahl
    gespeichert ist.
    Format: Jede Zeile enthält die Werte einer Reihe,
    getrennt durch spaces.
    """
    try:
        maze = []
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    row = [int(x) for x in line.split()]
                    maze.append(row)
        return maze
    except FileNotFoundError:
        console.print(f"Datei {file_path} nicht gefunden.")
        return None
    except Exception as exc:  # pragma: no cover - defensive
        console.print(
            f"Fehler beim Lesen der Datei: {exc}"
        )
        return None


def main() -> None:
    """
    Hauptfunktion zum Visualisieren des Mazes.
    """
    import sys

    console.print("\n")
    console.rule("Maze Visualizer mit Rich")
    console.print("\n")

    if len(sys.argv) > 1:
        # Wenn eine Datei angegeben wird, lade das Maze daraus
        maze_file = sys.argv[1]
        console.print(f"Lade Maze aus: {maze_file}")
        maze = load_maze_from_file(maze_file)
        if maze:
            height = len(maze)
            width = len(maze[0]) if height > 0 else 0
            print_maze_visual_rich(
                maze,
                width,
                height,
                0,
                0,
                width - 1,
                height - 1,
            )
    else:
        # Ansonsten verwende die Config-Datei
        config_path = "config.txt"
        console.print(f"Lade Config aus: {config_path}\n")
        visualize_maze(config_path)

    console.print("\n")
    console.rule("Fertig!")
    console.print("\n")


if __name__ == "__main__":
    main()
