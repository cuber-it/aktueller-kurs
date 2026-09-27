# Pro und Contra · Eine Landkarte der vorhandenen Architektur

Bewertet wird der Vorschlag aus dem Lösungspapier: eine einseitige Übersicht der Schichten mit Verantwortung, typischen Änderungen und versteckten Aufgaben, ohne Bewertung.

---

## Pro

**Änderungen finden ihren Ort**
Mit einer Zeile in der Übersicht („Real Names: UI-Module“) beginnt die Suche nach einem umbenannten Objekt am richtigen Ort.

**Versteckte Aufgaben werden bekannt**
Dass `Control.wait()` den Kontext wechselt und neu verbindet, gehört in jede Fehlersuche. Aufgeschrieben muss es nicht jeder selbst herausfinden.

**Die Stärken des Bestands werden sichtbar**
Die Trennung von Test und Squish ist konsequent umgesetzt. Eine Übersicht zeigt das auch denen, die sonst zuerst die Probleme sehen.

**Grundlage für Werkzeuge**
Dieselbe Übersicht kann Claude Code als Kontext dienen (Tag 3).

---

## Contra

**Eine Übersicht veraltet**
Kommt eine Schicht hinzu oder verschiebt sich eine Verantwortung, muss jemand die Seite anpassen. Ohne feste Zuständigkeit wird sie bald falsch.

**Beschreiben ohne Bewerten ist schwer**
Wer die Übersicht schreibt, hat Meinungen. Formulierungen wie „leider“ oder „historisch“ schleichen sich ein.

**Eine Seite ist knapp**
Ein Framework mit 1.975 Zeilen allein in `controls.py` lässt sich nicht vollständig auf einer Seite beschreiben. Die Übersicht zeigt Schichten, nicht Methoden.

**Sie löst nichts**
D2 und D5 ziehen weiter bis in den Testfall. Die Übersicht macht das sichtbar, ändert es aber nicht.

---

## Bewertung

Die Übersicht trägt, weil **die Struktur gut ist, aber nirgends beschrieben**.

Gegenprobe – *nur die Fehlermeldung verbessern („objectName nicht gefunden“), keine Übersicht, bleiben Nachteile?* Ja: Die Meldung hilft bei diesem Fehler. Wo Wartezeiten, Kontextwechsel oder Menüwege liegen, bliebe unbekannt.

**Die Grenzen:**

1. **Pflege.** Die Übersicht braucht eine Zuständigkeit und einen Anlass zur Aktualisierung, etwa jeden Review einer neuen Schicht.
2. **Tiefe.** Für Controls und Wartemethoden reicht eine Zeile nicht. Dafür gibt es einen eigenen Abschnitt oder Docstrings.
3. **Bewertung folgt später.** Was die Landkarte an Befunden zeigt, gehört in den Review (Übung 08).

---

## Diskussionsfragen

1. Wer soll die Übersicht pflegen, und bei welchem Anlass?
2. Welche versteckte Aufgabe in Ihrem Framework kostet heute bei der Fehlersuche am meisten Zeit?
3. Reicht eine Seite, oder braucht die Control-Schicht eine eigene?
4. Was müsste in der Übersicht stehen, damit Claude Code eine Änderung an der richtigen Stelle vornimmt?
