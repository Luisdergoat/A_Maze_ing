## This project has been created as part of the 42 curriculum by lunsold and jdreissi

# A_Maze_ing

![42 Badge](https://img.shields.io/badge/42-Project-blue) ![Language](https://img.shields.io/badge/Language-Python-orange) ![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

Ein vollständiges Python-Projekt zur **Generierung, Visualisierung und Lösung von Labyrinthen** basierend auf Konfigurationsdateien mit optionalem 42-Pattern.

---

## 📋 Projektübersicht

A_Maze_ing ist ein ausgereiftes Labyrinth-Generierungstool, das Labyrinthe basierend auf einer `config.txt` Datei erstellt, visualisiert und automatisch löst. Das Projekt nutzt einen rekursiven Backtracking-Algorithmus zur Generierung und bietet eine hochwertige Terminal-Visualisierung mit der `rich`-Library.

---

## ✨ Features

### ✅ Vollständig implementiert

- **🎯 Maze-Generierung**
  - Rekursiver Backtracking-Algorithmus
  - Perfekte und unperfekte Labyrinthe (PERFECT-Flag)
  - Optionales 42-Pattern für die Projektnummer
  - Seed-basierte Generierung für reproduzierbare Ergebnisse

- **🖼️ Visualisierung**
  - Terminal-basierte Live-Visualisierung mit `rich`
  - Bit-basierte Wanddarstellung (4-Bit System)
  - Farbcodierte Elemente (Entry, Exit, Wände, Pfade)
  - Optionale Animation während der Generierung
  - Zwei Visualizer (Standard + New Visualizer)

- **🧭 Maze-Solving**
  - Automatischer Pathfinding-Algorithmus
  - Visualisierung des Lösungswegs
  - Markierung besuchter Zellen

- **📄 Dateiausgabe**
  - Exportiert Labyrinth als `maze.txt` in hexadezimalem Format
  - Enthält Entry/Exit-Koordinaten

- **🔧 Build-System**
  - Vollständiges Makefile mit Zielsteuerung
  - Automatische Virtual Environment-Verwaltung
  - Dependency-Management

---

## 🏗️ Projektstruktur

```
A_Maze_ing/
├── Makefile                    # Build-System mit install, run, clean
├── README.md                   # Diese Datei
├── config.txt                  # Konfigurationsdatei für Labyrinth-Parameter
├── requirements.txt            # Python-Dependencies (auto-generiert)
└── src/
    ├── main.py                 # ✅ Hauptprogramm mit CLI-Menü
    ├── cell.py                 # ✅ Cell-Klasse für Labyrinth-Zellen
    ├── mazeparser.py           # ✅ Config-Parser und Validierung
    ├── mazegen_algo.py         # ✅ Maze-Generierungsalgorithmus
    ├── solve_maze_algo.py      # ✅ Maze-Solving-Algorithmus
    ├── visualize_maze.py       # ✅ Rich-basierte Maze-Visualisierung
    ├── new_maze_visualizer.py  # ✅ Alternativer Visualizer
    └── output_file.py          # ✅ Dateiausgabe-Generator
```

---

## 🚀 Installation & Verwendung

### Installation

```bash
# Repository klonen
git clone https://github.com/Luisdergoat/A_Maze_ing.git
cd A_Maze_ing

# Dependencies installieren (erstellt automatisch Virtual Environment)
make install
```

### Programm ausführen

```bash
# Maze-Generator starten
make run
```

### Manuelle Ausführung

```bash
# Virtual Environment aktivieren
source venv/bin/activate

# Programm starten
python3 src/main.py
```

---

## 🎮 Interaktives CLI-Menü

Nach dem Start bietet das Programm folgende Optionen:

```
Choose one of the options:
1: generate Maze       - Generiert und löst ein neues Labyrinth
2: edit config         - Öffnet config.txt in nvim zum Bearbeiten
3: change colour       - Farbschema ändern (experimentell)
4: exit                - Programm beenden
5: exit with cleanup   - Beenden + generierte Dateien löschen (make fclean)
```

---

## 📝 Config-Datei Format

Die `config.txt` definiert alle Parameter für die Labyrinth-Generierung:

```text name=config.txt url=https://github.com/Luisdergoat/A_Maze_ing/blob/main/config.txt
# Maze Configuration 
WIDTH=15
HEIGHT=22
ENTRY=0, 0
EXIT=14, 21
OUTPUT_FILE=maze.txt
PERFECT=False
42PATTERN=True
SEED=random
```

### Parameter-Beschreibung

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| **WIDTH** | Integer | Breite des Labyrinths (min. 3) |
| **HEIGHT** | Integer | Höhe des Labyrinths (min. 3) |
| **ENTRY** | Tuple | Startpunkt (x,y) |
| **EXIT** | Tuple | Ausgangspunkt (x,y) |
| **OUTPUT_FILE** | String | Name der generierten Ausgabedatei |
| **PERFECT** | Boolean | `True` = ein Lösungsweg, `False` = mehrere Wege möglich |
| **42PATTERN** | Boolean | `True` = Fügt 42-Pattern ein |
| **SEED** | String/Integer | `random` oder fester Seed für Reproduzierbarkeit |

---

## 🛠️ Technologie-Stack

- **Python 3.x**
- **rich** >= 13.0.0 - Terminal-UI und Visualisierung
- **pytest** >= 7.0.0 - Testing (vorbereitet)

---

## 🧩 Modulbeschreibungen

### `cell.py` - Cell-Klasse

Repräsentiert eine einzelne Zelle im Labyrinth.

**Attribute:**
- `x, y` - Koordinaten
- `wall` - 4-Bit-Integer für Wände (Bit 0-3: West, Süd, Ost, Nord)
- `visited` - Besuchsstatus während Generierung
- `frame` - Markierung für Rahmen-Zellen
- `solve_need` - Flag für Lösungsweg

**Wanddarstellung:**
```
Bit 3 (8): Nord  ↑
Bit 2 (4): Ost   →
Bit 1 (2): Süd   ↓
Bit 0 (1): West  ←

Beispiele:
15 (1111) = Alle Wände geschlossen
0  (0000) = Alle Wände offen
10 (1010) = Nord und Süd geschlossen
```

### `mazeparser.py` - Configuration Parser

Liest und validiert die `config.txt`:
- Parst Key-Value-Paare
- Konvertiert Datentypen (int, bool, tuple)
- Validiert Koordinaten innerhalb der Grenzen
- Prüft Mindestgröße (3x3)

### `mazegen_algo.py` - Maze-Generator

Implementiert den Labyrinth-Generierungsalgorithmus:
- **Algorithmus:** Recursive Backtracking mit Stack
- **Funktionen:**
  - `check_moves()` - Prüft gültige Bewegungen
  - `check_walls()` - Wall-Validierung
  - `generat_maze()` - Hauptgenerierungsfunktion
- **Features:** Live-Animation, Frame-Handling, 42-Pattern-Integration

### `solve_maze_algo.py` - Maze-Solver

Löst das generierte Labyrinth:
- **Algorithmus:** Depth-First Search (DFS) mit Stack
- **Funktionen:**
  - `check_valid_moves()` - Findet mögliche Bewegungen basierend auf Bit-Masken
  - `maze_solve()` - Findet Pfad von Entry zu Exit
  - `maze_visualization()` - Visualisiert den Lösungsweg

### `visualize_maze.py` - Rich-Visualizer

Hochwertige Terminal-Visualisierung:
- Nutzt `rich`-Library für farbige Ausgabe
- Live-Update während Generierung und Lösung
- Zeigt Entry (grün), Exit (rot), Pfade und Wände
- Refresh-Rate: 120 FPS

### `output_file.py` - File Export

Generiert `maze.txt` mit:
- Hexadezimale Wandkodierung (ein Zeichen pro Zelle)
- Entry/Exit-Koordinaten am Dateiende

**Beispiel-Output:**
```
ffffff...
f0a3b...
...
0,0
14,21
```

---

## 📊 Makefile-Targets

| Target | Beschreibung |
|--------|--------------|
| `make all` | Alias für `make run` |
| `make install` | Erstellt venv und installiert Dependencies |
| `make run` | Startet das Programm |
| `make clean` | Löscht generierte Dateien (maze.txt, etc.) |
| `make fclean` | Clean + löscht venv |
| `make re` | Rebuild (fclean + all) |

---

## 🎨 Visualisierungs-Modi

### Standard-Modus (ohne Animation)
```python
generat_maze(maze, config, animate=False)
```

### Animations-Modus
```python
generat_maze(maze, config, animate=True, delay=0.01)
```

### Solving-Visualisierung
```python
maze_visualization(maze, config, solution, animate=True, delay=0.01)
```

---

## 🧪 Beispiel-Workflow

1. **Config anpassen:**
   ```bash
   nvim config.txt  # oder Option 2 im Menü
   ```

2. **Maze generieren:**
   ```bash
   make run
   # Dann Option 1 wählen
   ```

3. **Output prüfen:**
   - Terminal: Live-Visualisierung
   - Datei: `maze.txt` (hexadezimale Repräsentation)

4. **Cleanup:**
   ```bash
   make clean   # Nur generierte Dateien
   make fclean  # Alles inkl. venv
   ```

---

## 🔍 Algorithmus-Details

### Maze-Generierung (Recursive Backtracking)

1. Starte bei zufälliger Zelle
2. Markiere aktuelle Zelle als besucht
3. Wähle zufällige unbesuchte Nachbarzelle
4. Entferne Wand zwischen aktueller und gewählter Zelle
5. Rekursiv auf neue Zelle
6. Bei Sackgasse: Backtrack zum letzten Fork

### Maze-Solving (DFS)

1. Starte bei ENTRY-Koordinaten
2. Prüfe verfügbare Bewegungen (keine Wand, nicht besucht)
3. Stack-basierte Exploration
4. Markiere Pfad bis EXIT erreicht
5. Visualisiere Lösungsweg

---

## 🤝 Contributing

Contributions sind willkommen! 

**Entwickelt von:**
- [@Luisdergoat](https://github.com/Luisdergoat) (lunsold)
- jdreissi

**Pull Requests:** Gerne für Verbesserungen und neue Features.

---

## 📄 Lizenz

Noch nicht festgelegt - Teil des 42 Curriculum.

---

## 🐛 Bekannte Limitationen

- Option 3 (change colour) ist noch experimentell
- `new_maze_visualizer.py` ist in Entwicklung (nicht voll integriert)
- Testing-Framework vorbereitet, aber Tests noch nicht implementiert

---

## 💡 Tipps & Tricks

### Sehr große Labyrinthe generieren
```text
WIDTH=100
HEIGHT=100
PERFECT=True
SEED=42  # Für Reproduzierbarkeit
```

### Schnelle Generierung ohne Animation
Im Code (main.py):
```python
generat_maze(maze, config, animate=False)
maze_visualization(maze, config, solution, animate=False)
```

### Custom Seeds für reproduzierbare Labyrinthe
```text
SEED=12345  # Statt "random"
```

---

## 📚 Weiterführende Informationen

**Algorithmen:**
- [Recursive Backtracking (Wikipedia)](https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_backtracker)
- [Depth-First Search (Wikipedia)](https://en.wikipedia.org/wiki/Depth-first_search)

**Libraries:**
- [Rich Documentation](https://rich.readthedocs.io/)
- [Python venv](https://docs.python.org/3/library/venv.html)

---
