# 2-1 · Die vorhandene Squish-Architektur sichtbar machen

Die bestehende Testautomatisierung ist keine Sammlung einzelner Squish-Skripte, sondern bereits eine **gewachsene Softwarearchitektur**. Bevor weitere Konzepte bewertet werden, müssen ihre vorhandenen Verantwortlichkeiten und Grenzen sichtbar werden.

- **Testfälle und Abstraktionen** – Tests nutzen bereits Controls, UI-/Screen-Abstraktionen, Helper und gemeinsame Libraries.
- **Control-/Widget-Schicht** – Kapselt elementare Squish-Interaktionen, Zustandsabfragen und Teile der Synchronisation.
- **Verifikation** – Wiederverwendbare Prüfmechanismen standardisieren Beobachtung und Bewertung.
- **Lifecycle und Targets** – Test-Wrapper, AUT-Zustand und Target-Abstraktionen sind ebenfalls Architekturbausteine.
- **Daten und Konfiguration** – Testdaten und Konfiguration besitzen eigene Strukturen und Verantwortlichkeiten.
- **Kopplung** – GUI, Squish Runtime, AUT und Projektcode müssen zusammenarbeiten. Ziel ist nicht Kopplung zu beseitigen, sondern notwendiges Wissen sinnvoll zu konzentrieren.
- **Architekturanalyse** – Entscheidend sind Verantwortung, Abhängigkeiten und Änderungsursachen – nicht die Namen bekannter Patterns.

## Leitgedanke

Neue Architekturkonzepte lassen sich erst sinnvoll beurteilen, wenn verstanden ist, **welche Probleme die vorhandene Architektur bereits löst und wo ihre Grenzen liegen**.

> **Merksatz:** Bevor wir neue Patterns diskutieren, müssen wir verstehen, welche Architektur bereits existiert und warum.
