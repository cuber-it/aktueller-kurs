# Tag 1 -- Python/OOP für Testautomatisierung

## Rahmen

-   Kurszeit: 09:00--17:00
-   Mittagspause: 1 Stunde
-   Zwei kurze Pausen
-   Zielgruppe: erfahrene Entwickler, die Python kennen
-   Ziel des Tages: eine gefestigte Basis und ein gemeinsames Verständnis
    der OO-Teile von Python für alle Teilnehmer
-   Einheit: ca. 45 Minuten
-   Pro Einheit: ca. 20 Minuten Trainerinput + ca. 25 Minuten
    Teilnehmerarbeit, gemeinsame Analyse oder Übung
-   Didaktischer Grundansatz: Problem → Analyse →
    Python-Lösungsrichtungen → Anwendung → Konsequenzen
-   Material: Beispiele als vorher/nachher-Paare aus dem Testframework
    des Teams (`Tag 1/Beispiele/`), Übungen je Einheit
    (`Tag 1/Uebungen/`), Python 3.10 wie in Squish 9.2

## Tagesgliederung

  -----------------------------------------------------------------------------------------
  Zeit               Einheit              Trainer ca. 20 Min        Teilnehmer / Anwendung
                                                                    ca. 25 Min
  ------------------ -------------------- ------------------------- -----------------------
  **09:00--09:45**   **1-1 Objekt-        Getter/Setter gegen       Übung 01: Konfiguration
                     orientierung in      Property, Magic Methods   aus einem Java-Port
                     Python**             als Protokolle            pythonisch machen
                                          (`NumValueDTO`)

  **09:45--10:30**   **1-2 Verantwort-    Änderungsgründe,          Übung 02: Helper-Klasse
                     lichkeiten &         Invarianten schützen      und Anbaugerät nach
                     Kapselung**          (Testkonfiguration,       Verantwortung schneiden
                                          `NumValueDTO`)

  **10:30--10:45**   **Pause**                                      

  **10:45--11:30**   **1-3 Vererbung,     Hierarchie der Test-      Übung 03: BaseTest,
                     Komposition &        konfiguration, Kontext-   Mixins und Ergebnis-
                     Delegation**         verwaltung als            klassen beurteilen
                                          Kollaborateur

  **11:30--12:15**   **1-4 Abstraktion    ABC ohne Vertrag, großer  Übung 04: dieselbe
                     in Python**          gegen kleiner Vertrag,    Grenze als Duck Typing,
                                          Type Hints                ABC und Protocol

  **12:15--13:15**   **Mittagspause**                               

  **13:15--14:00**   **1-5 Abhängigkeiten `test_exec_helper`,       Übung 05: Workflow ohne
                     & Testbarkeit**      globale Konfiguration,    Prüfstand testbar
                                          DI ohne Container         machen

  **14:00--14:45**   **1-6 Zustand,       Cleanup-Kette gegen       Übung 06: Terminal-App
                     Lifecycle &          `ExitStack`, geteilter    und Datenbank als
                     Ressourcen**         Zustand, Exceptions       Context Manager

  **14:45--15:00**   **Pause**                                      

  **15:00--15:45**   **1-7 Wartbarer      Public API, Schalter-     Übung 07: öffentliche
                     Python-Code &        Parameter, Namen,         API eines geteilten
                     APIs**               Automatisierung           Frameworks festlegen

  **15:45--16:30**   **1-8 OO Design      Einführung und            Section-Control-Test
                     Challenge**          Moderation                analysieren, Entwurf   
                                                                    entwickeln, vergleichen

  **16:30--17:00**   **Standards          Rule Board                erste Python-/OO-
                     Session**            konsolidieren             Guidelines festlegen
  -----------------------------------------------------------------------------------------

Die Übungen enthalten mehr Aufgaben, als in 25 Minuten zu schaffen
sind. Sie dienen als Auswahl für den Trainer, als Referenz und zum
Selbststudium.

## Roter Faden

``` text
eigener Code des Teams (Kundenframework)
              ↓
   Objektmodell und Protokolle
              ↓
   Verantwortung und Invarianten
              ↓
   Vererbung / Komposition / Delegation
              ↓
   Verträge: Duck Typing, ABC, Protocol
              ↓
   sichtbare Abhängigkeiten
              ↓
   Lifecycle, Cleanup, Fehler
              ↓
   wartbare API
              ↓
   Design Challenge am eigenen Muster
              ↓
   Python-/OO-Standard als Grundlage für Tag 2
```

Die Beispiele stammen aus dem Testframework des Teams und behalten
dessen Namen. Die Übungen spielen in der Domäne des Kunden, ohne
Anspruch auf fachliche Richtigkeit, und stehen jeweils für sich.

## Didaktische Leitlinie

Die Python-Konzepte werden nicht isoliert als Sprachfeatures behandelt,
sondern aus konkreten Problemen der Testautomatisierung hergeleitet.

Beispiel:

> `NumValueDTO` hält einen Wert zweimal, als Zahl und als Text. Nach
> `dto.value = 9` liefert `get_input_value()` weiterhin den alten Text.
> Welche Möglichkeiten bietet Python, das zu verhindern?

Erst aus dieser Problemstellung werden Property, Invariante und
Kapselung entwickelt und miteinander verglichen.

SOLID, Generics und weitere fortgeschrittene Konzepte werden nicht als
separate Lehrblöcke behandelt. Sie werden dort eingebracht, wo sie für
eine konkrete Entwurfsentscheidung relevant sind.

## Übergang zu Tag 2

Der an Tag 1 erarbeitete Python-/OO-Standard bildet die Grundlage für
die Arbeit mit Squish an Tag 2. Tag 2 greift die bestehende
Testarchitektur des Teams auf (Controls, UI-Module, Target-Abstraktion,
Test-Wrapper) und diskutiert sie mit denselben Kategorien:
Verantwortung, Abhängigkeit, Lifecycle und öffentliche API.
