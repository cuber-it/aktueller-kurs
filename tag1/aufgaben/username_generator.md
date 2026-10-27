# Einen Benutzernamen erzeugen

**Schwerpunkt:** Strings zusammensetzen und vereinheitlichen.

## Variante 1: drei Eingaben

Lies Vorname, Nachname und Geburtsjahr getrennt ein. Erzeuge daraus einen Benutzernamen im Format **vorname.nachname.jahr**.

Anforderungen:

- Zwischen den drei Bestandteilen steht jeweils genau ein Punkt.
- Der Benutzername wird vollständig kleingeschrieben.
- Das Geburtsjahr wird unverändert als Text übernommen.
- Gib den fertigen Benutzernamen verständlich beschriftet aus.

Für diese Variante darfst du Namen ohne zusätzliche Leerzeichen voraussetzen.

## Variante 2: eine gemeinsame Eingabe

Lies dieselben Angaben nun in einer einzigen Eingabe ein, beispielsweise `Anna / Schmidt / 1995`.

- Entferne die Leerzeichen.
- Ersetze die Schrägstriche durch Punkte.
- Wandle das Ergebnis in Kleinschreibung um.
- Gib den Benutzernamen aus.

Du darfst voraussetzen, dass genau drei Angaben mit zwei Schrägstrichen eingegeben werden. Eine Prüfung des Geburtsjahrs oder eine Umschreibung von Umlauten ist nicht gefordert.

## Prüfe dein Programm

| Angaben | Erwarteter Benutzername in beiden Varianten |
|---|---|
| Anna / Schmidt / 1995 | anna.schmidt.1995 |
| MAX / MUSTER / 1980 | max.muster.1980 |
| Lea / Müller / 2001 | lea.müller.2001 |

In Variante 1 gibst du die Angaben einzeln ein; in Variante 2 als gemeinsame Zeile.

## Zum Vergleichen

Welche Variante ist bei der Eingabe bequemer? Welche setzt mehr Wissen über das erwartete Eingabeformat voraus?

**Eigene Datei:** `tag1/loesungen/username_generator.py`
