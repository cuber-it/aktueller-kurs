# Fallbeispiel · Eine Klasse, zwei Wachstumsrichtungen

**Situationstyp:** Eine Klasse wächst in zwei Richtungen zugleich. Jede neue Variante in einer Richtung trifft alle Stellen der anderen.

---

## Ausgangslage

Eine Klasse geht alle Menüs eines Geräts in den Maschineneinstellungen durch und bearbeitet jeden Parameter: Geometrie, Geschwindigkeiten, GNSS und weitere, für Traktor und Anbaugeräte.

## Wie es gewachsen ist

Zuerst sollte sie nur Werte auslesen und in eine CSV schreiben; für jeden Control-Typ entstand eine Methode. Dann sollten Werte mit einer Referenz verglichen werden, jede Methode bekam einen Zweig. Später sollten Werte auf die Referenz gesetzt werden, jede Methode bekam einen weiteren Zweig. Welcher Zweig läuft, bestimmt `self.action`.

## Was auffällt

**Die Klasse ist Weg, Aktion und Zugriff zugleich.** Wer eine Aktion ändert, liest alle Control-Typen; wer einen Control-Typ ändert, liest alle Aktionen.

**Eine neue Aktion trifft fünf Methoden.** Auf Werkswerte zurücksetzen hieße fünf neue Zweige.

**Der Weg durch die Menüs kennt die Aktion.** Beim Setzen braucht ein Untermenü Fokus, also prüft der Weg `self.action`.

**Ergebnisse stehen als Text in Attributen.** `self.names += ";" + …`; für einen Bericht werden sie wieder zerlegt.

## Naheliegende Ansätze

**Eine Basisklasse für Aktionen.** Verschiebt die Zweige, beseitigt sie nicht.

**Kommentare je Zweig.** Hilfreich beim Lesen, nicht beim Ändern.

## Diskussionsfragen

1. Welche Änderung ist häufiger: neue Aktion oder neuer Control-Typ?
2. Warum hilft eine Basisklasse für Aktionen wenig?
3. Wer sollte wissen, wie man einen Schalter liest: die Aktion oder der Control-Typ?
4. Wo haben Sie so etwas?
