# Tag 2 – Datei-Input
#
# Dateien öffnest du mit open(). Das  with  davor sorgt dafür,
# dass die Datei am Ende automatisch wieder geschlossen wird –
# das solltest du dir gleich angewöhnen.
#
# Unsere Beispieldatei liegt im Ordner "materialien/" auf
# Repo-Ebene. Damit das Skript egal aus welchem Verzeichnis
# läuft, bauen wir den Pfad relativ zur Skriptdatei (pathlib).

from pathlib import Path

DATEI = Path(__file__).parent.parent / "materialien" / "beispiel.txt"

# --- Komplette Datei einlesen ---
with open(DATEI, "r", encoding="utf-8") as f:
    inhalt = f.read()
print(inhalt)
print("---")

# --- Zeilenweise einlesen (das ist der Normalfall) ---
with open(DATEI, "r", encoding="utf-8") as f:
    for zeile in f:
        # zeile enthält noch das Zeilenende "\n", strip() entfernt es
        print(f"-> {zeile.strip()}")

# --- Zeilen zählen ---
anzahl = 0
with open(DATEI, "r", encoding="utf-8") as f:
    for _ in f:
        anzahl += 1
print(f"Datei hat {anzahl} Zeilen.")

# Die wichtigsten Modi für open():
#   "r"  = lesen (read)             [Standard]
#   "w"  = schreiben (überschreibt!)
#   "a"  = anhängen (append)
#
# encoding="utf-8" möglichst immer angeben – sonst zicken Umlaute.
#
# Was passiert, wenn die Datei nicht existiert?  -> FileNotFoundError
# Wie man das abfängt, siehst du im nächsten Beispiel.
