## This project has been created as part of the 42 curriculum by lunsold and jdreissi

# A_Maze_ing

# ![42 Badge](https://img.shields.io/badge/42-Project-blue)    ![Language](https://img.shields.io/badge/Language-python-orange)


Ein Python-Projekt zur Generierung und Visualisierung von Labyrinthen basierend auf Konfigurationsdateien.

## 📋 Projektübersicht

Dieses Projekt erstellt Labyrinthe basierend auf einer config.txt Datei mit definierten Parametern wie Breite, Höhe, Ein- und Ausgang.

## 🚀 Aktueller Status

### ✅ Implementiert
- ✅ Maze Parser (`src/mazeparser.py`)
  - Config-Datei Einlesen und Validierung
  - Fehlerbehandlung für fehlende/ungültige Werte
  - Maze-Initialisierung als 2D-Liste

### ❌ Noch zu implementieren

#### 1. **Maze-Generierung vervollständigen**
- [ ] Algorithmus zur Pfadgenerierung zwischen Entry und Exit implementieren
- [ ] PERFECT-Flag Logik umsetzen (perfektes vs. unperfektes Labyrinth)
- [ ] Maze-Lösung/Pfadfindung implementieren

#### 2. **Dateien & Dokumentation erstellen**
- [ ] `config.txt` - Beispiel-Konfigurationsdatei erstellen
- [ ] `requirements.txt` - Python-Dependencies auflisten
- [ ] `.gitignore` - Python-spezifische Ignores hinzufügen
- [ ] `LICENSE` - Lizenz hinzufügen

#### 3. **Hauptprogramm entwickeln**
- [ ] `main.py` oder `src/main.py` - Entry Point erstellen
- [ ] Command-line Interface (CLI) implementieren
- [ ] Maze-Ausgabe/Visualisierung implementieren

#### 4. **Testing**
- [ ] Unit Tests für mazeparser.py schreiben
- [ ] Test-Config-Dateien erstellen
- [ ] Edge Cases testen

#### 5. **Features**
- [ ] ASCII-Visualisierung des Labyrinths
- [ ] Grafische Visualisierung (optional: pygame, matplotlib)
- [ ] Export-Funktionen (PNG, SVG, TXT)
- [ ] Pfad-Highlighting im Labyrinth

## 📦 Installation

```bash
# Repository klonen
git clone https://github.com/Luisdergoat/A_Maze_ing.git
cd A_Maze_ing

# Dependencies installieren (requirements.txt noch zu erstellen)
pip install -r requirements.txt
```

## 🔧 Verwendung

```bash
# Programm ausführen (noch zu implementieren)
python main.py config.txt
```

## 📝 Config-Datei Format

Beispiel `config.txt` (noch zu erstellen):
```
# Labyrinth-Konfiguration
WIDTH=10
HEIGHT=10
ENTRY=0,0
EXIT=9,9
PERFECT=True
```

**Parameter:**
- `WIDTH`: Breite des Labyrinths (min. 3)
- `HEIGHT`: Höhe des Labyrinths (min. 3)
- `ENTRY`: Startpunkt (x,y)
- `EXIT`: Ausgangspunkt (x,y)
- `PERFECT`: True = ein Weg, False = mehrere Wege

## 🏗️ Projektstruktur

```
A_Maze_ing/
├── README.md
├── src/
│   └── mazeparser.py       # ✅ Config-Parser und Validierung
├── config.txt              # ❌ Noch zu erstellen
├── requirements.txt        # ❌ Noch zu erstellen
├── main.py                 # ❌ Noch zu erstellen
└── tests/                  # ❌ Noch zu erstellen
```

## 🛠️ Technologie Stack

- Python 3.x
- (Weitere Dependencies folgen)

## 🤝 Contributing

Contributions sind willkommen! Bitte erstelle einen Pull Request.

## 📄 Lizenz

Noch nicht festgelegt - bitte Lizenz hinzufügen.

## 👤 Autor

[@Luisdergoat](https://github.com/Luisdergoat)

---

## 🎯 Nächste Schritte (Priorität)

1. **config.txt Beispieldatei erstellen**
2. **Maze-Generierungsalgorithmus fertigstellen** (z.B. Depth-First Search, Prim's Algorithm)
3. **main.py mit CLI erstellen**
4. **ASCII-Visualisierung implementieren**
5. **requirements.txt und .gitignore hinzufügen**