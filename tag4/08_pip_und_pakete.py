# Tag 4 – Interpreter und Pakete prüfen
# Die Installation gehört ins Terminal; die Anleitung steht in VENV.md.

from importlib.metadata import PackageNotFoundError, version
import sys


def main():
    """Zeigt, auf welchen Interpreter sich die Paketprüfung bezieht."""
    print("Interpreter:", sys.executable)
    print("In einer venv:", sys.prefix != sys.base_prefix)
    try:
        print("Installierte pip-Version:", version("pip"))
    except PackageNotFoundError:
        print("Für diesen Interpreter wurde keine pip-Installation gefunden.")


if __name__ == "__main__":
    main()
