"""
Dieser maze visualizer hat lunsold geschrieben er ist unfassbar krass
und mega geil, 
{dieser Docstring entstand, bevor der visualizer geschrieben wurde}
"""

from __future__ import annotations

from typing import List, Mapping, Optional, Sequence, Tuple, cast

import mazeparser
from rich import box
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


# TODO: visualisierung des maze und die visualisierung der buit tabele in einem
# fenster, fuer die bytes tabelle
# visualisierung der maze config

# Globale Variable fuer Live-Darstellung
console = Console()