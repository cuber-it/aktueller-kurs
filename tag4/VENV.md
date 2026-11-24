# Virtuelle Umgebungen mit venv

Eine virtuelle Umgebung enthält einen eigenen Python-Interpreter beziehungsweise
einen Verweis darauf und ein eigenes Verzeichnis für installierte Pakete.
Damit lassen sich die Abhängigkeiten verschiedener Projekte getrennt verwalten.

Ohne virtuelle Umgebung hängt das Installationsziel von der Python-Installation
und den pip-Optionen ab. Es kann beispielsweise ein Benutzerverzeichnis oder
ein systemweit genutztes Verzeichnis sein. Manche Distributionen schützen ihre
verwaltete Python-Installation vor direkten Änderungen durch pip.

## Anlegen

Im Projektordner unter Linux oder macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Unter Windows mit PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Die Aktivierung passt den Suchpfad des aktuellen Terminals an.
Prüfe, welcher Interpreter und welches pip verwendet werden:

```bash
python -c "import sys; print(sys.executable)"
python -m pip --version
```

Beide Pfade sollen zur gewählten Umgebung gehören. Eine Aktivierung ist nicht
zwingend: Unter Linux lässt sich der Interpreter auch direkt über
`.venv/bin/python` aufrufen, unter Windows über `.venv\Scripts\python.exe`.

## Pakete verwalten

Die folgenden Befehle verwenden pip aus dem gewählten Interpreter.
`requests` dient als Beispiel für ein externes Paket; die Kursbeispiele für
Tag 3 und Tag 4 brauchen keine zusätzlichen Pakete.

```bash
python -m pip install requests
python -m pip list
python -m pip show requests
python -m pip freeze > requirements.txt
```

`freeze` hält installierte Paketversionen fest. Das erleichtert die
Wiederherstellung; Python-Version, Betriebssystem und verfügbare Pakete
können weiterhin eine Rolle spielen.

## Auf einem anderen Rechner einrichten

Die Datei `requirements.txt` wird mit dem Projekt weitergegeben.
Die Umgebung selbst wird dort neu angelegt:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Unter Windows die oben gezeigten Befehle zum Anlegen und Aktivieren verwenden.
Mit `deactivate` endet die Aktivierung im aktuellen Terminal.

## Repository und Editor

`.venv/` und `__pycache__/` stehen bereits in der `.gitignore`.
Die virtuelle Umgebung wird nicht versioniert.

Im Editor den Interpreter aus `.venv` auswählen. Bei einem bereits geöffneten
Terminal kann zusätzlich eine Aktivierung oder ein neues Terminal nötig sein.
Mit `sys.executable` lässt sich die Auswahl überprüfen.
