# Eine E-Mail-Adresse zerlegen

**Schwerpunkt:** Strings zerlegen und Teilergebnisse ausgeben.

## Grundaufgabe

Schreibe ein Programm, das eine E-Mail-Adresse einliest und in zwei Teile zerlegt:

- den **lokalen Teil** vor dem `@`,
- die **Domain** nach dem `@`.

Gib beide Teile mit einer verständlichen Beschriftung getrennt aus. Für diesen ersten Schritt darfst du eine Eingabe mit genau einem `@` voraussetzen.

## Prüfe dein Programm

| Eingabe | Lokaler Teil | Domain |
|---|---|---|
| info@example.org | info | example.org |
| anna.schmidt@example.net | anna.schmidt | example.net |
| support+kurs@example.org | support+kurs | example.org |

Der lokale Teil bleibt vollständig erhalten, auch wenn er einen Punkt oder ein Pluszeichen enthält.

## Erweiterung: einfache Eingabeprüfung

Sobald du `if` kennengelernt hast:

1. Prüfe, ob die Eingabe **genau ein** `@` enthält.
2. Bei keinem oder mehreren `@`: Gib eine Fehlermeldung mit der ursprünglichen Eingabe aus.
3. Zerlege die Eingabe nur, wenn diese Prüfung erfolgreich war.

Probiere `info.example.org` und `info@@example.org` aus. Beide Eingaben müssen in dieser Erweiterung eine Fehlermeldung ergeben.

Diese Prüfung zählt nur die `@`-Zeichen. Sie ist keine vollständige Prüfung, ob eine E-Mail-Adresse gültig ist.

## Hinweis

Du kannst entweder die Position des Trennzeichens ermitteln und mit Slices arbeiten oder die String-Methode zum Aufteilen verwenden.

**Eigene Datei:** `tag1/loesungen/email_splitter.py`
