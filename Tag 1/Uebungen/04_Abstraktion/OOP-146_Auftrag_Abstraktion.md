# OOP-146 · Verträge an Komponentengrenzen auf den tatsächlichen Bedarf zuschneiden

**Typ:** Story
**Komponente:** Testframework Kern
**Priorität:** Mittel

---

## Story

**Als** Entwickler im Testautomatisierungsteam
**möchte ich**, dass eine Komponente nur die Operationen verlangt, die sie tatsächlich aufruft,
**damit** eine Erweiterung an einer Stelle nicht Implementierungen und Test-Doubles an vielen anderen Stellen bricht.

---

## Description

Im Testframework gilt seit 2020 die Regel: „Jede Komponente bekommt eine abstrakte Basisklasse." Die Regel wurde konsequent umgesetzt.

**Bestand:**

| Was | Anzahl |
|---|---|
| abstrakte Methoden in `Notifier` | 5 |
| Implementierungen von `Notifier` im Framework | 4 |
| davon Methodenrümpfe nur mit `pass` oder `raise NotImplementedError` | 11 von 20 |
| Clients von `Notifier` | 3, alle rufen nur `send()` auf |
| Methoden im Protocol `UiDriver` | 9 |
| Test-Doubles für `UiDriver` | 14, zusammen 126 Methoden |
| davon von einem Test tatsächlich aufgerufen | 38 |
| ABCs mit genau einer Implementierung | 6, darunter `ReportRenderer` (seit 2021) |

**Befund:** Sieben Test-Doubles in anderen Testmodulen erben von `Notifier`. Eine neue abstrakte Methode in `Notifier` macht sie nicht mehr instanziierbar, auch wenn die vier Implementierungen im Framework ergänzt werden.

**Zweiter Befund:** Das Team wollte Ergebnisse über den Chat-Client eines Drittanbieters veröffentlichen. Dessen Klasse besitzt bereits eine Methode `send(message)`, erbt aber nicht von `Notifier`. Es entstand eine Adapterklasse mit fünf Methoden, von denen vier nur `pass` enthalten.

**Dritter Befund:** Seit Einführung von Type Hints gehen Teile des Teams davon aus, dass falsche Objekte nicht mehr übergeben werden können. In der CI läuft bisher kein Type Checker.

**Nicht Gegenstand:** Die Implementierung der Kanäle selbst und der Austausch des GUI-Werkzeugs.

## Randbedingungen

- Python 3.10 (Squish 9.2). Ein Type Checker darf in die CI aufgenommen werden.
- Die Klasse des Drittanbieters kann nicht geändert werden.
- Die Implementierung von `UiDriver` für das GUI-Werkzeug wird von einem anderen Team gepflegt und soll unverändert bleiben.
- Die Test-Doubles liegen verteilt in den Testmodulen der Fachteams.

## Akzeptanzkriterien

- **AK1** – Jeder Client verlangt über seinen Vertrag nur die Operationen, die er aufruft.
- **AK2** – Die Klasse des Drittanbieters ist als Benachrichtigungskanal verwendbar, ohne dass eine Klasse mit wirkungslosen Methoden entsteht.
- **AK3** – Eine neue Operation an einem Kanal erfordert keine Änderung an Clients und Test-Doubles, die sie nicht verwenden.
- **AK4** – Ein Test-Double für `ServiceUnlockFlow` implementiert höchstens die Operationen, die `ServiceUnlockFlow` aufruft.
- **AK5** – Für jede der sechs ABCs mit genau einer Implementierung ist entschieden, ob sie bleibt, mit Begründung.
- **AK6** – Für jede bearbeitete Grenze ist festgehalten, ob Duck Typing, ABC oder Protocol verwendet wird, und warum.
- **AK7** – Es ist dokumentiert, was Type Hints im Team leisten und was nicht.

## Hinweise

Alle ABCs durch Protocols zu ersetzen erfüllt AK1 nicht. Ein Protocol mit neun Methoden koppelt genauso stark wie eine ABC mit neun Methoden.

AK2 hat eine Falle: `Notifier.register(VendorChatClient)` lässt `isinstance` zustimmen, prüft aber keine einzige Methode.

AK7 wird unbequem, solange kein Type Checker läuft. Annotationen, die niemand prüft, dokumentieren eine Erwartung. Durchgesetzt wird sie nicht.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Was braucht dieser Client von seinem Gegenüber – und wie ausdrücklich muss das festgehalten werden?**

---
---

# Addendum · Woran man einen unpassenden Vertrag erkennt

## Im Code

| Signal | Beispiel |
|---|---|
| Methodenrümpfe mit `pass` oder `raise NotImplementedError` | `ConsoleNotifier.send_attachment` |
| Clients rufen einen kleinen Teil des Vertrags auf | `ResultPublisher` nutzt eine von fünf Methoden |
| Test-Doubles sind länger als der Test | neun Methoden, damit zwei aufgerufen werden |
| Adapter, die nur Leermethoden ergänzen | Adapter für eine fremde Klasse, die bereits passt |
| Abstraktion mit genau einer Implementierung und ohne absehbare zweite | `ReportRenderer` seit 2021 |
| Eine Erweiterung bricht Klassen, die sie nicht verwenden | neue abstrakte Methode, sieben Test-Doubles defekt |

## Im Team

| Signal | Beispiel |
|---|---|
| Eine Form wird zur Regel erhoben | „jede Komponente bekommt eine ABC" |
| Eine Form gilt als moderner | „Protocols statt ABCs" |
| Annotationen gelten als Absicherung | „mit Type Hints kann nichts Falsches übergeben werden" |

## Die drei Formen im Vergleich

| | Duck Typing | ABC | Protocol |
|---|---|---|---|
| Vertrag steht | in Verwendung und Dokumentation | in der Basisklasse | im Protocol |
| Zugehörigkeit durch | vorhandenes Verhalten | Erben oder `register` | vorhandene Struktur |
| Fremde Klassen passen | ja, wenn das Verhalten stimmt | nur über Adapter oder `register` | ja, wenn die Struktur stimmt |
| Prüfung beim Instanziieren | keine | fehlende abstrakte Methoden werden gemeldet | keine |
| Prüfung durch Type Checker | nur mit Annotation | ja, nominal | ja, strukturell |
| `isinstance` | kein Typ, gegen den geprüft werden kann | möglich | nur mit `@runtime_checkable`, prüft nur Vorhandensein |
| gemeinsame Implementierung | nicht vorgesehen | möglich | nicht üblich |

## Was Type Hints leisten

Python wertet Annotationen zur Laufzeit nicht aus. `ServiceUnlockFlow("kein Treiber")` wird ohne Fehler erzeugt. Der Fehler zeigt sich erst beim ersten Aufruf von `type_text`, als `AttributeError`.

Ein Type Checker wie mypy meldet denselben Fehler vor dem Lauf, wenn er ausgeführt wird. Type Hints sind damit ein Vertrag für Werkzeuge und Leser. Ob sie im Team eine Absicherung sind, hängt davon ab, ob ein Werkzeug sie prüft.

## Wann eine Abstraktion ihren Preis wert ist

Eine Abstraktion ist in der Regel gerechtfertigt, wenn mindestens eines zutrifft:

- Es gibt mehrere Implementierungen, oder eine zweite ist konkret absehbar.
- Tests brauchen einen Ersatz für eine langsame oder technische Abhängigkeit.
- Die Grenze trennt Verantwortlichkeiten, die sich unabhängig ändern sollen.
- Fremder Code soll an einer Stelle eingesetzt werden können.

Trifft keiner dieser Punkte zu, kostet die Abstraktion einen zusätzlichen Begriff und einen Sprung beim Lesen, ohne etwas zurückzugeben.
