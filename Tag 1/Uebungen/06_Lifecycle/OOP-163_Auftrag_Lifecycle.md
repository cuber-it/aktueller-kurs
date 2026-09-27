# OOP-163 · Testumgebung nach fehlgeschlagenen Tests verlässlich zurücksetzen

**Typ:** Story
**Komponente:** Testumgebung
**Priorität:** Hoch

---

## Story

**Als** Verantwortliche für den Nachtlauf
**möchte ich**, dass ein fehlgeschlagener Test die Umgebung nicht für die folgenden Tests unbrauchbar macht und sein eigener Fehler im Protokoll erscheint,
**damit** nach einem fehlgeschlagenen Test nur dieser eine Fehler im Protokoll steht.

---

## Description

Die Tests der Terminal-Software öffnen je eine Testdatenbank und starten die Anwendung. Beendet werden beide durch Aufrufe am Ende des Tests.

**Bestand:**

| Was | Anzahl |
|---|---|
| Tests im Nachtlauf | 860 |
| davon mit `try/finally` um `start()`/`stop()` | 64 |
| Nächte in den letzten 30 mit Folgefehler-Kaskade | 9 |
| Tickets „Simulator nicht erreichbar" in den letzten sechs Wochen | 41 |

**Befund:** Schlägt eine Prüfung fehl, wird `stop()` nicht mehr erreicht, und die Anwendung läuft weiter. Jeder folgende Test scheitert dann am Start einer zweiten Instanz. Im Protokoll steht ein echter Fehler zwischen vielen Folgefehlern.

**Zweiter Befund:** Bei den 64 abgesicherten Tests tritt ein anderes Problem auf. Stürzt die Anwendung während des Tests ab, schlägt im `finally` der Aufruf `stop()` mit `ProcessLookupError` fehl. Im Protokoll erscheint nur dieser Fehler, der Absturz nicht.

**Dritter Befund:** Die 41 Tickets „Simulator nicht erreichbar" hatten drei Ursachen:

| Ursache | Anzahl |
|---|---|
| Simulator überlastet, Zeitüberschreitung | 17 |
| Simulator nicht gestartet, Verbindung abgewiesen | 15 |
| falscher Hostname in der Konfiguration | 9 |

Die Hilfsfunktion `connect_to_simulation` fängt jede Exception und liefert `False`. Die Ursache musste jedes Mal von Hand ermittelt werden.

**Nicht Gegenstand:** Die Stabilität der Terminal-Software selbst und die Reihenfolge der Tests im Nachtlauf.

## Randbedingungen

- Die 860 Tests dürfen angepasst werden, aber die Anpassung pro Test sollte mechanisch sein.
- Die Anwendung darf je Rechner nur einmal laufen.
- Ein Test, der die Anwendung nicht startet, soll davon nicht betroffen sein.
- Python 3.10, das Python aus Squish 9.2.

## Akzeptanzkriterien

- **AK1** – Nach einem fehlgeschlagenen Test sind Anwendung und Testdatenbank beendet, ohne dass der Test dafür selbst `try/finally` schreiben muss.
- **AK2** – Der ursprüngliche Fehler eines Tests erscheint im Protokoll, auch wenn das Aufräumen danach ebenfalls scheitert.
- **AK3** – Ein Fehler beim Aufräumen geht nicht verloren. Er ist im Protokoll erkennbar.
- **AK4** – Ein Aufruf von `send()` an eine nicht gestartete Anwendung schlägt mit einer eindeutigen Meldung fehl.
- **AK5** – Eine Anwendung kann nicht ohne Testdatenbank gestartet werden.
- **AK6** – Die drei Ursachen für „Simulator nicht erreichbar" sind für den Aufrufer unterscheidbar, und die technische Ursache bleibt für die Diagnose erhalten.
- **AK7** – Die Reihenfolge des Aufräumens ist festgelegt: erst die Anwendung, dann die Datenbank.

## Hinweise

`try/finally` in allen 860 Tests erfüllt AK1 nicht. Die 64 abgesicherten Tests sind der Beleg: Sie verlagern das Problem, und AK2 verletzen sie.

AK3 und AK2 ziehen in verschiedene Richtungen. Wer den Cleanup-Fehler wirft, verdrängt den Originalfehler. Wer ihn verschluckt, verliert ihn.

AK6 verlangt keine Exception je Ursache. Entscheidend ist, auf welche Unterschiede ein Aufrufer reagieren kann.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Wer beendet diesen Zustand – und was passiert, wenn zwischen Start und Ende ein Fehler auftritt?**

---
---

# Addendum · Woran man ungeklärten Lifecycle erkennt

## Im Code

| Signal | Beispiel |
|---|---|
| `start()` und `stop()` als getrennte Aufrufe im Client | `app.start()` … `app.stop()` ohne Absicherung |
| Methoden, die in bestimmten Zuständen still Unsinn tun | `send()` vor `start()` sendet an `None` |
| Objekte, die nach dem Konstruktor noch nicht verwendbar sind | `configure()` muss vor `start()` aufgerufen werden |
| `except Exception: return False` | drei Ursachen, eine Antwort |
| `except Exception: pass` im Cleanup | Fehler beim Aufräumen verschwinden |
| Cleanup-Code nach dem letzten Prüfschritt | läuft nur, wenn alle Prüfungen bestehen |

## Im Testbetrieb

| Signal | Beispiel |
|---|---|
| Fehler-Kaskaden | ein echter Fehler, hunderte Folgefehler |
| Fehler hängen von der Reihenfolge ab | Test besteht einzeln, scheitert im Nachtlauf |
| Die gemeldete Ursache passt nicht zum Symptom | `ProcessLookupError` statt Absturz |
| Aufräumen von Hand vor dem nächsten Lauf | „vorher alle Terminal-Prozesse beenden" |
| Tickets mit derselben Meldung und verschiedenen Ursachen | „Simulator nicht erreichbar" |

## Drei Python-Regeln, die hier zählen

**Eine Exception im `finally` ersetzt die ursprüngliche.** Die ursprüngliche hängt dann nur noch als `__context__` an der neuen und erscheint im Traceback als „During handling of the above exception, another exception occurred". Wer nur die Meldung der letzten Exception protokolliert, verliert sie.

**`__exit__` wird nicht aufgerufen, wenn `__enter__` scheitert.** Was `__enter__` bis zum Fehler aufgebaut hat, muss es selbst wieder abbauen.

**Gibt `__exit__` einen wahren Wert zurück, wird die Exception unterdrückt.** Ein Context Manager, der versehentlich `True` liefert, lässt fehlgeschlagene Tests bestehen.

## Wann ein Context Manager passt

Ein Context Manager drückt eine **begrenzte Lebensdauer** aus: Etwas wird geöffnet, gestartet oder gesperrt und muss verlässlich wieder geschlossen werden. Er ist angemessen, wenn

- es einen klaren Anfang und ein klares Ende gibt,
- das Ende auch im Fehlerfall erreicht werden muss,
- der Nutzer das Ende nicht vergessen können soll.

Gibt es kein Ende, das garantiert werden muss, ist ein Context Manager zusätzliche Struktur ohne Aussage.
