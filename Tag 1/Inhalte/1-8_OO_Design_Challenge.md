# 1-8 · OO Design Challenge

Die bisherigen Einheiten betrachten einzelne Entwurfsfragen. In der Design Challenge werden sie **gemeinsam auf gewachsenen Testcode angewendet**. Ziel ist nicht, möglichst viele Techniken einzubauen, sondern begründete Designentscheidungen zu treffen.

## Ausgangslage

Ein gewachsener Testbereich enthält typischerweise eine Mischung aus:

- Testablauf und technischen Details,
- mehreren Verantwortlichkeiten in einzelnen Klassen,
- direkter Erzeugung konkreter Abhängigkeiten,
- gemeinsamem Verhalten über Basisklassen,
- wiederholten Hilfsfunktionen,
- implizitem Zustand und Cleanup,
- uneinheitlichen Namen und Schnittstellen,
- schwer isolierbaren Komponenten.

## Analyse

Vor dem Refactoring wird untersucht:

1. **Welche Verantwortlichkeiten existieren?**
2. **Welche Änderungsursachen sind erkennbar?**
3. **Wo entsteht unnötige Kopplung?**
4. **Welche Abhängigkeiten sind versteckt?**
5. **Welche Vererbung modelliert tatsächlich eine Typbeziehung?**
6. **Wo wäre Komposition oder Delegation geeigneter?**
7. **Welche Abstraktionen werden wirklich benötigt?**
8. **Welche Zustände und Lifecycle-Regeln müssen sichtbar werden?**
9. **Wie sollte die öffentliche API aussehen?**

## Refactoring

Das Ziel ist kein vorgegebenes Klassendiagramm. Unterschiedliche Lösungen sind möglich, sofern ihre Entscheidungen begründet werden können.

Mögliche Maßnahmen sind:

- Verantwortlichkeiten aufteilen,
- Abhängigkeiten explizit machen,
- Vererbung durch Komposition ersetzen,
- kleine Verträge über Protocols oder ABCs ausdrücken,
- Lifecycle und Cleanup kapseln,
- öffentliche APIs vereinfachen,
- Naming und Modulstruktur konsolidieren.

## Vergleich der Lösungen

Eine Lösung wird nicht danach bewertet, wie viele OO-Techniken sie verwendet, sondern danach, wie sie auf erwartbare Änderungen reagiert:

- Was muss geändert werden, wenn eine technische Implementierung ausgetauscht wird?
- Welche Teile bleiben stabil?
- Wie leicht lässt sich Verhalten isoliert testen?
- Welche zusätzliche Komplexität erzeugt die Lösung?
- Welche Regeln daraus wären für den gesamten Testcode sinnvoll?

## Transfer in den Teamstandard

Die Challenge liefert die Kandidaten für die anschließende Standards Session. Dabei wird zwischen allgemeiner Erkenntnis und konkreter Teamregel unterschieden.

> **Merksatz:** OO-Architektur zeigt ihren Wert bei Änderungen – nicht im Klassendiagramm.
