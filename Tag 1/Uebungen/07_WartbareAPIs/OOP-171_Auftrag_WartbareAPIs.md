# OOP-171 · Öffentliche Schnittstelle des gemeinsamen Testframeworks festlegen

**Typ:** Story
**Komponente:** Testframework Plattform
**Priorität:** Hoch

---

## Story

**Als** Entwickler im Plattformteam
**möchte ich** wissen, welche Teile des Frameworks andere Teams verwenden dürfen,
**damit** ich interne Details ändern kann, ohne Nachtläufe anderer Teams zu brechen.

---

## Description

Das Testframework wird vom Plattformteam (drei Entwickler) gepflegt und von vier Suite-Teams verwendet. Es umfasst rund 2.100 Zeilen in fünf Modulen.

**Bestand:**

| Was | Anzahl |
|---|---|
| Module im Framework | 5 |
| davon mit Namen `common`, `utils`, `helpers`, `test_helpers` | 4 |
| Zugriffe der Suite-Teams auf Namen mit führendem Unterstrich | 87 |
| Dateien der Suite-Teams mit solchen Zugriffen | 41 |
| öffentliche Methoden ohne Type Hints | 112 von 131 |
| Review-Kommentare im letzten Quartal | 420 |
| davon zu Formatierung, Importreihenfolge und Leerzeilen | 160 |

**Befund:** `ResultCollector._write_json` gilt wegen des Unterstrichs als intern, wird aber von drei Suite-Teams direkt aufgerufen. Eine Umbenennung oder ein neuer Parameter bricht deren Nachtläufe, und wer die Methode wo verwendet, ist nirgends festgehalten.

**Befund zur Entstehung:** Es gibt keine festgelegte öffentliche Schnittstelle. Eine Wiki-Seite „Public API" von 2022 nennt 14 Funktionen, von denen 5 nicht mehr existieren. Die Suite-Teams haben verwendet, was sie in der IDE gefunden haben.

**Zweiter Befund:** Rund 38 % der Review-Kommentare betreffen Fragen, die ein Formatter oder Linter entscheiden könnte. Für Designfragen bleibt in den Reviews wenig Zeit.

**Nicht Gegenstand:** Die Architektur der Testfälle in den Suite-Teams und die Einführung von Page Objects.

## Randbedingungen

- Die 87 Zugriffe dürfen nicht einfach verboten werden. Sie zeigen, was die Teams brauchen.
- Das Framework läuft unter Python 3.10, dem Python aus Squish 9.2.
- Die CI läuft für alle Repositories auf derselben Pipeline-Vorlage.
- Die Suite-Teams übernehmen neue Framework-Versionen im Mittel nach drei Wochen.

## Akzeptanzkriterien

- **AK1** – Für jedes Modul ist festgelegt und im Code erkennbar, welche Namen öffentlich sind.
- **AK2** – Jeder der 87 Zugriffe ist bewertet: Er wird durch eine öffentliche Funktion ersetzt, oder es ist begründet, warum das Bedürfnis nicht bedient wird.
- **AK3** – Öffentliche Funktionen und Methoden sind typannotiert.
- **AK4** – Docstrings der öffentlichen API beschreiben den Vertrag: Zweck, Bedeutung der Parameter, Seiteneffekte, Exceptions. Docstrings, die nur den Namen wiederholen, sind entfernt oder ersetzt.
- **AK5** – Modulnamen lassen die Verantwortung erkennen.
- **AK6** – Testergebnisse sind nach dem Erfassen nicht mehr von außen veränderbar.
- **AK7** – Formatierung, Importreihenfolge und die vereinbarten Lint-Regeln werden in der CI geprüft, nicht im Review.
- **AK8** – Die daraus abgeleiteten Teamregeln sind als MUST, SHOULD, MAY oder DON'T eingeordnet, jeweils mit Angabe, ob ein Werkzeug oder ein Review sie prüft.

## Hinweise

Die Wiki-Seite zu aktualisieren erfüllt AK1 nicht. Sie war schon einmal richtig und ist veraltet, weil nichts sie mit dem Code verbindet.

Alle Namen mit Unterstrich öffentlich zu machen erfüllt AK2 nicht. Damit würde jedes Implementierungsdetail zum Vertrag.

AK2 wird unbequem: Einige der 87 Zugriffe zeigen Bedürfnisse, die das Plattformteam nicht bedienen will, etwa das Verändern bereits erfasster Ergebnisse über interne Datenstrukturen.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Worauf darf sich fremder Code verlassen – und woran erkennt er das?**

---
---

# Addendum · Woran man eine fehlende öffentliche Schnittstelle erkennt

## Im Code

| Signal | Beispiel |
|---|---|
| Fremder Code greift auf `_`-Namen zu | `collector._write_json(...)` |
| Methoden geben interne Datenstrukturen heraus | `get_results()` liefert das interne Dictionary |
| Namen beschreiben Technik statt Absicht | `add(n, s, d)`, `proc`, `do_export` |
| Docstrings wiederholen den Namen | `"""Returns the results."""` |
| Module heißen nach Art statt nach Aufgabe | `utils.py`, `helpers.py`, `common.py` |
| Ergebnisse als Dictionaries mit Konventionsschlüsseln | `{"status": ..., "duration": ...}` |

## Im Team

| Signal | Beispiel |
|---|---|
| „Das war doch privat" | der Unterstrich war bekannt, die Nutzer nicht |
| Eine Wiki-Seite beschreibt die API | und ist veraltet |
| Reviews diskutieren Leerzeilen | Designfragen kommen zu kurz |
| Jede Framework-Version bricht irgendetwas | niemand weiß vorher, was |

## Was zur öffentlichen Schnittstelle gehört

| Mittel | Was es ausdrückt |
|---|---|
| Name ohne Unterstrich | darauf darf sich fremder Code verlassen |
| `_name` | Implementierungsdetail, kann sich ohne Ankündigung ändern |
| `__all__` | welche Namen das Modul nach außen anbietet; wirkt technisch auf `from modul import *`, wird aber auch von Werkzeugen und Lesern ausgewertet |
| Type Hints | welche Werte hineingehen und herauskommen |
| Docstring | Zweck, Vertrag, Randbedingungen, Exceptions |
| Modulname | welche Verantwortung hier liegt |

## Was eine Maschine entscheiden kann und was nicht

| Frage | Entscheidet |
|---|---|
| Zeilenlänge, Einrückung, Leerzeilen | Formatter |
| Importreihenfolge, unbenutzte Importe | Linter |
| `snake_case` für Funktionen | Linter mit Naming-Regeln |
| fehlende Type Hints | Linter oder Type Checker |
| fehlender Docstring | Linter |
| ob ein Docstring den Vertrag beschreibt | Mensch |
| ob ein Name die Absicht trifft | Mensch |
| ob eine Methode öffentlich sein sollte | Mensch |
| in welches Modul eine Funktion gehört | Mensch |

## Vom Stil zur Teamregel

| Kategorie | Bedeutung |
|---|---|
| **MUST** | verbindlich, Abweichung wird nicht akzeptiert |
| **SHOULD** | Standard, begründete Ausnahme möglich |
| **MAY** | zulässige Option |
| **DON'T** | bewusst vermeiden |

Eine Regel ist in der Regel nur dann tragfähig, wenn klar ist, **wer sie prüft**. Eine MUST-Regel, die niemand prüft, wird mit der Zeit zu einer MAY-Regel.
