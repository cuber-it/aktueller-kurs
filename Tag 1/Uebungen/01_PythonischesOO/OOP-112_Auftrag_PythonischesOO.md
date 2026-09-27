# OOP-112 · Konfigurations- und Testfallklassen an Python-Konventionen ausrichten

**Typ:** Story
**Komponente:** Testframework Kern
**Priorität:** Hoch

---

## Story

**Als** Entwicklerin im Testautomatisierungsteam
**möchte ich**, dass ungültige Konfigurationswerte beim Setzen auffallen und Testfälle in Protokollen lesbar erscheinen,
**damit** ein Konfigurationsfehler nicht erst im Nachtlauf als Massenausfall sichtbar wird.

---

## Description

Das Testframework wurde 2019 aus einer Java-Codebasis nach Python übertragen. Die Klassen im Modul `configuration.py` folgen weiterhin den Java-Konventionen.

**Bestand:**

| Was | Anzahl |
|---|---|
| Getter/Setter-Paare in `configuration.py` | 37 |
| davon ohne eigene Logik | 29 |
| Aufrufstellen dieser Getter und Setter in der Testsuite | 214 |
| Tests, die über `_TestConfiguration__…` auf Felder zugreifen | 11 |
| Klassen ohne Zustand, nur mit `@staticmethod` | 6 |

**Befund:** Die Setter prüfen keine Werte. Ein Timeout von 0 in einer gemeinsam genutzten Konfiguration lässt jede Warteoperation sofort abbrechen. Betroffen wären alle Tests, die auf ein UI-Objekt warten.

**Befund zur Entstehung:** Die Getter und Setter wurden eingeführt, „damit später Validierung eingebaut werden kann". In sieben Jahren wurde in keinem der 29 logikfreien Paare eine Validierung ergänzt.

**Zweiter Befund:** Im Testprotokoll erscheinen Testfälle als `<configuration.TestCase object at 0x7f3a…>`. Die Methode `toString()` existiert, wird aber von `print()`, Logging und dem Squish-Testprotokoll nicht verwendet.

**Nicht Gegenstand:** Die fachliche Struktur des Testframeworks und die Aufteilung in Module.

## Randbedingungen

- Die 214 Aufrufstellen dürfen einmalig angepasst werden, künftige Validierungen sollen sie nicht mehr berühren.
- Die Testsuite läuft unter Python 3.10, dem Python aus Squish 9.2.
- Testfälle werden in Sets gesammelt, um Duplikate zu erkennen.
- Das Team hat gemischte Erfahrung: drei Entwickler mit Java-Hintergrund, zwei mit Python-Hintergrund.

## Akzeptanzkriterien

- **AK1** – Ein Timeout außerhalb von 1 bis 300 Sekunden wird beim Setzen mit einer aussagekräftigen Exception abgewiesen.
- **AK2** – Lesender und schreibender Zugriff auf Konfigurationswerte sieht an den Aufrufstellen aus wie ein Attributzugriff.
- **AK3** – Eine später ergänzte Validierung für einen weiteren Wert erfordert keine Änderung an Aufrufstellen.
- **AK4** – Kein Test greift auf Namen der Form `_Klasse__feld` zu.
- **AK5** – Testfälle sind in `print()`, Logging und im Squish-Testprotokoll lesbar.
- **AK6** – Gleichheit von Testfällen ist mit `==` prüfbar und mit der Verwendung in Sets verträglich.
- **AK7** – Für die sechs zustandslosen Klassen ist entschieden, ob sie Klassen bleiben, mit Begründung.

## Hinweise

Weitere Getter und Setter mit Validierung zu ergänzen erfüllt AK2 nicht.

AK6 hat eine Falle: Wer `__eq__` definiert, verändert damit auch die Hashbarkeit der Klasse.

AK4 wird unbequem. Die elf Tests greifen nicht aus Nachlässigkeit auf die Felder zu, sondern weil sie für einzelne Läufe Werte setzen wollten, die kein Setter erlaubte.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Welche dieser Strukturen drückt in Python etwas aus – und welche wurde nur mitgebracht?**

---
---

# Addendum · Woran man übertragene Konventionen erkennt

## Im Code

| Signal | Beispiel |
|---|---|
| Getter und Setter ohne eigene Logik | `getTimeout()`, `setTimeout(value)` |
| Doppelte Unterstriche als „private" | `self.__timeout` |
| Klassen nur mit `@staticmethod` | `StringUtils.normalize(...)` |
| Klassen ohne Zustand mit einer Methode | `TimestampFormatter().format(...)` |
| Methoden, die Python-Protokolle nachbauen | `toString()`, `equals()`, `compareTo()` |
| Interfaces für einzelne Aufrufe | `Runnable`, `Callback` mit einer Methode |

## Im Team

| Signal | Beispiel |
|---|---|
| „Das ist sauberes OO" als Begründung | eine Konvention wird mit ihrer Herkunft begründet, nicht mit ihrem Nutzen |
| „Damit wir später …" | vorsorgliche Struktur für einen Fall, der nicht eingetreten ist |
| Tests umgehen die Kapselung | `_Klasse__feld` in Testcode |
| Protokolle sind unlesbar | `<… object at 0x…>` in Logs |

## Was Python an dieser Stelle anbietet

| Mitgebracht | In Python |
|---|---|
| Getter/Setter | öffentliches Attribut; bei Bedarf später eine Property, ohne Änderung der Aufrufer |
| `private` | `_name` als Konvention: „kein Vertrag für fremden Code" |
| `toString()` | `__repr__` für Entwickler und Diagnose, `__str__` für Anzeige |
| `equals()` | `__eq__`, bei Bedarf zusammen mit `__hash__` |
| Klasse mit statischen Methoden | Funktionen auf Modulebene |
| Interface mit einer Methode | Funktionen und gebundene Methoden sind selbst Objekte und können übergeben werden |

## Was doppelte Unterstriche tatsächlich tun

`self.__timeout` wird innerhalb der Klasse zu `self._TestConfiguration__timeout` umbenannt (Name Mangling). Der Zweck ist, Namenskollisionen in Klassenhierarchien zu vermeiden, wenn eine Unterklasse zufällig denselben Namen verwendet.

Ein Zugriffsschutz entsteht dadurch nicht. Wer den umbenannten Namen kennt, kann zugreifen.

## Wann ein Getter trotzdem sinnvoll ist

Eine Methode statt eines Attributs ist in der Regel angemessen, wenn der Zugriff

- spürbar Zeit kostet, etwa weil eine Datei oder ein Dienst gelesen wird,
- Parameter braucht,
- Seiteneffekte hat,
- bei jedem Aufruf ein anderes Ergebnis liefern kann.

Eine Property sollte sich wie ein Attribut verhalten. Wer `config.timeout` liest, rechnet nicht mit einem Netzwerkzugriff.
