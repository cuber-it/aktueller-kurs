# OOP-139 · Testfähigkeiten aus der gemeinsamen Basisklasse lösen

**Typ:** Story
**Komponente:** Testframework Kern
**Priorität:** Hoch

---

## Story

**Als** Testarchitektin
**möchte ich**, dass jede Testklasse nur die Fähigkeiten besitzt, die sie tatsächlich verwendet,
**damit** eine Änderung an einer Fähigkeit nur die Tests betrifft, die diese Fähigkeit nutzen.

---

## Description

Alle GUI-Tests der Bediensoftware erben von `BaseTest`. Die Klasse wurde 2016 mit sechs Methoden angelegt und seither von allen Teams erweitert.

**Bestand:**

| Was | Anzahl |
|---|---|
| Methoden in `BaseTest` | 46 |
| Zeilen in `base_test.py` | 1.120 |
| Testklassen, die von `BaseTest` erben | 212 |
| im Mittel genutzte Methoden je Testklasse | 7 von 46 |
| Mixins im Projekt | 5 |
| Testklassen, die mindestens zwei Mixins kombinieren | 14 |
| Methoden, die in Unterklassen mit `NotImplementedError` stillgelegt werden | 4, alle in `ServiceMenuTest` |

**Befund:** Alarmtests und Section-Control-Tests teilen den Default-Timeout von `wait_for_screen()` (10 s). Die Section-Control-Tests setzen ihn nie selbst, ihre Bildschirmwechsel dauern bis zu 8 s. Wird der Default für schnellere Alarmtests gesenkt, trifft das die Section-Control-Tests.

**Zweiter Befund:** 23 Tests prüfen nur exportierte TaskData-Dateien auf dem Dateisystem. Sie erben trotzdem `setup()` und belegen dafür jeweils ein Gerät auf dem Testrack. Bei rund 2 Minuten Gerätezeit je Test sind das 46 Minuten Rackbelegung pro Nacht ohne Gerätebezug.

**Dritter Befund:** `ServiceMenuTest` legt `reset_device_database()` mit `NotImplementedError` still. Der Nachtlauf enthält deshalb die Zeile `if not isinstance(test, ServiceMenuTest)`.

**Nicht Gegenstand:** Die Testfälle selbst, ihre Abläufe und ihre Prüfungen.

## Randbedingungen

- Die 212 Testklassen können nicht in einem Schritt umgestellt werden.
- Der Testrunner ruft je Test `setup()`, `run()` und `teardown()` auf.
- Für die Konformitätsprüfung muss künftig jede Bedienaktion protokolliert werden (OOP-142).
- Die Ergebnisklassen `PassedResult` und `FailedResult` werden von drei Auswertungen verwendet.

## Akzeptanzkriterien

- **AK1** – An jeder umgestellten Testklasse ist ohne Lesen der Basisklasse erkennbar, welche Fähigkeiten sie verwendet.
- **AK2** – Ein Test ohne Gerätebezug läuft ohne Geräteverbindung.
- **AK3** – Der Timeout für Bildschirmwechsel kann für eine Gruppe von Tests geändert werden, ohne andere Tests zu beeinflussen.
- **AK4** – Keine Testklasse legt geerbte Methoden mit `NotImplementedError` still. Der Runner enthält keine Typprüfung auf einzelne Testklassen.
- **AK5** – Die Protokollierung aller Bedienaktionen (OOP-142) wird ergänzt, ohne Testklassen oder den Gerätetreiber zu ändern.
- **AK6** – Für jede verbleibende Vererbungsbeziehung ist begründet, welche Typbeziehung sie modelliert.
- **AK7** – Die Voraussetzungen, die ein Mixin an `self` stellt, sind sichtbar dokumentiert oder das Mixin ist ersetzt.

## Hinweise

`BaseTest` in mehrere kleinere Basisklassen aufzuteilen erfüllt AK1 nur teilweise. Das Wissen, welche Fähigkeit woher kommt, verteilt sich dann über eine Hierarchie.

AK6 bedeutet nicht, dass Vererbung verschwinden muss. Die Ergebnisklassen sind ausdrücklich zu prüfen, nicht umzubauen.

AK4 wird unbequem. `ServiceMenuTest` hat die Methode nicht aus Nachlässigkeit stillgelegt: Ein Reset der Gerätedatenbank löscht die Kalibrierwerte, die der Test prüft.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Ist diese Klasse eine spezielle Form ihrer Basisklasse – oder möchte sie nur deren Werkzeuge benutzen?**

---
---

# Addendum · Woran man eine Werkzeugkiste in Form einer Basisklasse erkennt

## Im Code

| Signal | Beispiel |
|---|---|
| Unterklassen nutzen nur einen kleinen Teil der Basisklasse | 7 von 46 Methoden |
| Methoden werden in Unterklassen stillgelegt | `raise NotImplementedError` in einer geerbten Methode |
| Typprüfungen auf einzelne Unterklassen im aufrufenden Code | `if not isinstance(test, ServiceMenuTest)` |
| Mixins greifen auf Attribute zu, die sie nicht selbst setzen | `self.driver`, `self.test_id` |
| Basisklassen mit Namen ohne Fachbegriff | `BaseTest`, `CommonTest`, `AbstractHelper` |
| Defaults in der Basisklasse, auf die sich Unterklassen stillschweigend verlassen | `timeout=10` |

## Im Team

| Signal | Beispiel |
|---|---|
| „Das packen wir in die Basisklasse, dann haben es alle" | Wiederverwendung als einziges Argument |
| Änderungen an der Basisklasse brauchen Abstimmung mit allen Teams | jede Änderung trifft 212 Klassen |
| Niemand weiß, welche Tests eine Methode nutzen | Suche nach Aufrufern liefert Treffer über `self.` in allen Klassen |

## Zwei verschiedene Beziehungen

| | Vererbung | Komposition |
|---|---|---|
| Aussage | „ist ein" | „arbeitet zusammen mit" |
| Sichtbar | an der Klassendeklaration | am Konstruktor oder an den Attributen |
| Umfang | alles, was die Basisklasse hat | nur, was übergeben wird |
| Austausch | Unterklasse bilden | anderen Kollaborateur übergeben |
| Vertrag | Unterklasse muss überall anstelle der Basisklasse verwendbar sein | Kollaborateur muss die genutzten Methoden anbieten |

## Wann Vererbung trägt

Vererbung ist in der Regel die passende Beziehung, wenn

- eine stabile Typbeziehung besteht, die auch ein Fachfremder so benennen würde,
- der Vertrag der Basisklasse für jede Unterklasse ohne Ausnahme gilt,
- Aufrufer mit der Basisklasse arbeiten und die konkrete Unterklasse nicht kennen müssen,
- die gemeinsame Implementierung zur Typbeziehung gehört und nicht nur zufällig gleich ist.

Ein `FailedResult` ist ein `TestResult`. Ein `AlarmTest` ist in erster Linie ein Test, der ein Gerät, eine Warteoperation und einen Bericht benutzt.

## Delegation

Ein Objekt nimmt einen Aufruf entgegen, ergänzt etwas und reicht die eigentliche Arbeit an ein anderes Objekt weiter. Die äußere Schnittstelle bleibt gleich, das Verhalten wird erweitert. Delegation ist der übliche Weg, Verhalten zu ergänzen, ohne die ursprüngliche Klasse zu ändern oder von ihr zu erben.
