# Virtuelle Umgebungen und Pakete

## Worum geht's

`venv` erstellt eine eigene Python-Umgebung für ein Projekt. `pip` installiert darin externe Pakete. Entscheidend ist, welcher Interpreter und welches pip tatsächlich verwendet werden.

Die Themenbeispiele für Tag 3 und Tag 4 kommen mit der Standardbibliothek aus. Die Paketinstallation wird hier am zusätzlichen Beispiel `requests` gezeigt.

## Umgebung anlegen und aktivieren

Linux und macOS, im Projektordner:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows mit PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Die Aktivierung passt den Suchpfad des aktuellen Terminals an. Sie ist keine Voraussetzung für die Verwendung der Umgebung: Ihr Interpreter kann auch direkt über `.venv/bin/python` beziehungsweise `.venv\Scripts\python.exe` gestartet werden.

## Den Interpreter prüfen

```python
import sys

print("Interpreter:", sys.executable)
print("In einer venv:", sys.prefix != sys.base_prefix)
```

`sys.executable` zeigt den Interpreter dieses Prozesses. Unterschiedliche Werte für `prefix` und `base_prefix` kennzeichnen eine mit `venv` erstellte Umgebung.

Im aktivierten Terminal:

```bash
python -m pip --version
```

Der angezeigte pip-Pfad soll ebenfalls zur gewünschten Umgebung gehören. `python -m pip` verwendet pip aus genau diesem Interpreter.

## Pakete installieren und auflisten

```bash
python -m pip install requests
python -m pip list
python -m pip show requests
```

pip verwendet standardmäßig den Python Package Index (PyPI); seine Konfiguration kann andere Quellen festlegen. Installationsname und Importname müssen nicht gleich sein: `PyYAML` wird beispielsweise mit `import yaml` verwendet.

Ohne virtuelle Umgebung hängt das Installationsziel von der Python-Installation und den pip-Optionen ab. Es ist nicht grundsätzlich systemweit.

## Paketversion im Programm abfragen

```python
from importlib.metadata import PackageNotFoundError, version

try:
    print("pip-Version:", version("pip"))
except PackageNotFoundError:
    print("Für diesen Interpreter ist keine pip-Paketinformation vorhanden.")
```

Die Abfrage liest installierte Paketmetadaten. Ein Importname ist dafür nicht immer der richtige Suchname.

## Paketstand festhalten und wiederherstellen

```bash
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```

`freeze` schreibt installierte Paketversionen auf; die Umleitung ersetzt eine vorhandene Datei gleichen Namens. Zur Wiederherstellung wird zunächst eine neue Umgebung angelegt.

Eine Versionsliste allein garantiert noch keine identische Umgebung auf einer anderen Python-Version oder Plattform. `.venv/` wird daher nicht kopiert oder versioniert, sondern neu erzeugt.

Mit `deactivate` endet die Aktivierung im aktuellen Terminal.

## Stolpersteine

- Editor und Terminal können unterschiedliche Interpreter verwenden.
- Ein erfolgreiches `pip install` belegt nur die Installation in der dabei verwendeten Umgebung.
- `ModuleNotFoundError` kann auf eine falsche Umgebung statt auf ein fehlendes Paket hinweisen.
- Eine fehlende pip-Installation ist von einem fehlenden Projektpaket zu unterscheiden.

## Schnellreferenz

| Aufgabe | Befehl |
| --- | --- |
| Umgebung erzeugen | `python3 -m venv .venv` |
| pip zuordnen | `python -m pip --version` |
| Paket installieren | `python -m pip install paketname` |
| Paketstand speichern | `python -m pip freeze > requirements.txt` |
| Paketstand installieren | `python -m pip install -r requirements.txt` |

**Beispiel:** [Interpreter und Paketversion](../../tag4/08_pip_und_pakete.py)  
**Anleitung:** [Virtuelle Umgebungen](../../tag4/VENV.md)
