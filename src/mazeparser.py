"""
Hier wir die logik genommen aus der config.txt werden die regel eingesetzt
und in ein maze umgewandelt.
"""
import sys

def read_out_config(file_path) -> dict:
    """
    Nimmt die werte aus der Config.txt
    und gibt sie als dictionary zurueck
    die keys werden dann noch in integer und boolean umgewandelt.
    """
    config = {}

    try:
        #  Versucht die config datei zu oeffnen und die werte in ein Dict macht
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue  # Skip empty lines and comments

                if '=' not in line:
                    continue  # Skip lines without '='

                key, value = line.split('=', 1)
                if value.isdigit():
                    config[key] = int(value)
                elif value.lower() in ['true']:
                    config[key] = True
                else:
                    config[key] = value

        #  checked ob alle Werte auch gegeben wurden
        required_keys = ['WIDTH', 'HEIGHT', 'ENTRY', 'EXIT', 'PERFECT']

        for key in required_keys:
            if key not in config:
                raise ValueError(f"Missing required config key:{key}")

        #  checked ob die werte fuer die groesse des mazes passen
        for i in config:
            if i == "WIDTH":
                width = config[i]
            if i == "HEIGHT":
                height = config[i]
            if i == "ENTRY" or i == "EXIT":
                x, y = config[i].split(',')
                config[i] = (int(x.strip()), int(y.strip()))

        if width < 3 or height < 3:
            raise ValueError("The Maze turned out to small. "
                             "At least 3x3 is required.")
        entry_x, entry_y = config['ENTRY']
        exit_x, exit_y = config['EXIT']
        if not (0 <= entry_x < width and 0 <= entry_y < height):
            raise ValueError("The entry or exit is out of bounds.")
        if not (0 <= exit_x < width and 0 <= exit_y < height):
            raise ValueError("The exit is out of bounds.")
        if config['ENTRY'] == config['EXIT']:
            raise ValueError("The entry and exit points must be different.")

        return config

    except FileNotFoundError:
        print("ERROR: The config.txt file was not found")
    except Exception as e:
        print(f"ERROR: An error occurred while reading the config file: {e}")
    return None


def parse_maze_config(config_path):
    """
    Also die funktion macht die validierung der config werte,
    hier wird sich um die logik des Mazes auf Bit ebene gekuemmert.
    Das Maze wird erst einmal als 2D-Liste von Zellen dargestellt,
    ohne korrekten Weg zzwischen Entry und Exit.
    """

    config = read_out_config(config_path)
    if config is None:
        return None

    #  Initialisiere das Maze als 2D-Liste mit Wänden (1)
    maze = [[1 for _ in range(config['WIDTH'])] for _ in range(config['HEIGHT'])]

    entry_x, entry_y = config['ENTRY']
    exit_x, exit_y = config['EXIT']
    maze[entry_y][entry_x] = 0  # Set entry point
    maze[exit_y][exit_x] = 0    # Set exit point



def main(argv):
    """
    Hauptfunktion zum Testen des Maze-Parsers.
    """
    config_path = 'config.txt'
    Test = parse_maze_config(config_path)
    print(Test)


if __name__ == "__main__":
    main(sys.argv)
