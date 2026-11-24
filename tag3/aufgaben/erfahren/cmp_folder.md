# Zwei Ordner vergleichen

**Schwerpunkt:** Dateien nach Namen und Inhalt zuordnen.

## Aufgabe

1. Frage zwei vorhandene, unterschiedliche Ordner ab.
2. Untersuche die unmittelbar enthaltenen Dateien. Unterordner werden nicht durchsucht.
3. Melde gleiche Dateinamen unabhängig davon, ob ihre Inhalte übereinstimmen.
4. Gruppiere Dateien nach einer SHA-256-Prüfsumme. Vergleiche Kandidaten mit gleicher Prüfsumme zusätzlich inhaltlich und melde die passenden Paare aus Ordner A und B.
5. Lies Dateien binär; berechne die Prüfsumme blockweise. Gib den Bericht erst aus, wenn beide Ordner verarbeitet wurden.

## Prüfe dein Programm

- Gleicher Name, unterschiedlicher Inhalt: nur beim Namensvergleich melden.
- Unterschiedliche Namen, gleicher Inhalt: beim Inhaltsvergleich melden.
- Gleicher Name und gleicher Inhalt: in beiden Ergebnissen melden.
- Leere Ordner erzeugen keine Treffer.
- Ungültige Pfade oder derselbe Ordner in beiden Eingaben werden verständlich abgewiesen.

## Referenz

- [Referenzlösung](../../loesungen/erfahren/cmp_folder.py)
