# Tag 1 -- Python & Objektorientierung

## Vom guten OO-Design zum gemeinsamen Python-Standard

**09:00--17:00 Uhr · Mittagspause 12:15--13:15 Uhr**

### Tagesziel

Wir untersuchen, wie objektorientierter Python-Code für eine wartbare
Testautomatisierung gestaltet werden kann. Dabei vergleichen wir
unterschiedliche Entwurfsentscheidungen, arbeiten mit konkretem Code und
leiten daraus gemeinsam **Python-/OO-Best-Practices und Teamregeln** ab.

------------------------------------------------------------------------

## 09:00--09:45 · 1-1 -- Objektorientierung in Python

Pythonisches Objektmodell und Besonderheiten objektorientierter
Entwicklung in Python.

-   Klassen und Objekte in Python
-   Pythonisches OO statt übertragener Java-/C#-Konventionen
-   Verantwortlichkeiten von Objekten
-   Magic Methods dort, wo sie einen konkreten Nutzen haben

**Merksatz:** Gutes OO-Design in Python nutzt die Möglichkeiten und
Konventionen von Python, statt andere Sprachen nachzubauen.

------------------------------------------------------------------------

## 09:45--10:30 · 1-2 -- Verantwortlichkeiten & Kapselung

Wie schneiden wir Klassen und Verantwortlichkeiten so, dass Code
verständlich und veränderbar bleibt?

-   Verantwortlichkeiten und Kohäsion
-   Kapselung und Information Hiding
-   Zuständigkeiten sinnvoll schneiden
-   typische Ursachen überladener Klassen

**Merksatz:** Eine Klasse braucht eine klare Verantwortung -- nicht nur
gemeinsame Daten.

------------------------------------------------------------------------

### 10:30--10:45 · Pause

------------------------------------------------------------------------

## 10:45--11:30 · 1-3 -- Vererbung, Komposition & Delegation

Unterschiedliche Möglichkeiten, Verhalten und Zusammenarbeit zwischen
Objekten zu modellieren.

-   Vererbung sinnvoll einsetzen
-   Komposition als Alternative
-   Delegation
-   Kopplung und Wiederverwendung
-   Auswirkungen auf Erweiterbarkeit und Testbarkeit

**Merksatz:** Vererbung modelliert eine echte Beziehung; Komposition
kombiniert Verhalten.

------------------------------------------------------------------------

## 11:30--12:15 · 1-4 -- Abstraktion in Python

Wie viel formale Abstraktion brauchen wir -- und welche Möglichkeiten
bietet Python?

-   Duck Typing
-   Abstract Base Classes
-   Protocols
-   nominale und strukturelle Typisierung
-   Type Hints als Unterstützung für Verständlichkeit und
    Werkzeugunterstützung

**Merksatz:** Abstrahiert wird benötigtes Verhalten -- nicht vorsorglich
jede Implementierung.

------------------------------------------------------------------------

### 12:15--13:15 · Mittagspause

------------------------------------------------------------------------

## 13:15--14:00 · 1-5 -- Abhängigkeiten & Testbarkeit

Wie beeinflussen Abhängigkeiten Wartbarkeit, Austauschbarkeit und
Testbarkeit?

-   explizite und versteckte Abhängigkeiten
-   Dependency Injection in Python
-   Kopplung reduzieren
-   austauschbare Implementierungen
-   testbares Design

**Merksatz:** Gute Abhängigkeiten sind sichtbar, kontrollierbar und
austauschbar.

------------------------------------------------------------------------

## 14:00--14:45 · 1-6 -- Zustand, Lifecycle & Ressourcen

Objekte leben nicht isoliert: Sie besitzen Zustand, verwenden Ressourcen
und können fehlschlagen.

-   Objektzustand und gültige Zustände
-   Initialisierung und Cleanup
-   Context Manager
-   Ressourcen sicher verwalten
-   Fehler und Exceptions als Teil des Designs

**Merksatz:** Zustand, Fehlerbehandlung und Cleanup sind Teil des
Objektdesigns.

------------------------------------------------------------------------

### 14:45--15:00 · Pause

------------------------------------------------------------------------

## 15:00--15:45 · 1-7 -- Wartbarer Python-Code & APIs

Aus einzelnen OO-Entscheidungen wird ein konsistenter, wartbarer
Python-Stil.

-   öffentliche Schnittstellen und Implementierungsdetails
-   API-Design
-   Module und Packages
-   Naming-Konventionen
-   PEP 8
-   Docstrings und Type Hints
-   `dataclass`, Properties und weitere Python-Werkzeuge dort, wo sie
    einen konkreten Nutzen bringen

**Merksatz:** Eine gute API macht den richtigen Gebrauch einfach und
hält Implementierungsdetails austauschbar.

------------------------------------------------------------------------

## 15:45--16:30 · 1-8 -- OO Design Challenge

Das Gelernte wird auf gewachsenen Testcode angewendet.

-   Verantwortlichkeiten und Kopplungen identifizieren
-   problematische Strukturen erkennen
-   geeignete Abstraktionen auswählen
-   Code schrittweise refactoren
-   unterschiedliche Lösungen und ihre Trade-offs vergleichen

**Merksatz:** OO-Architektur zeigt ihren Wert bei Änderungen -- nicht im
Klassendiagramm.

------------------------------------------------------------------------

## 16:30--17:00 · Standards Session

### Was wollen wir künftig gemeinsam so machen?

Die Erkenntnisse des Tages werden zu einem ersten gemeinsamen
**Python-/OO-Standard** konsolidiert.

-   Welche Regeln wollen wir verbindlich festlegen?
-   Was ist eine Empfehlung?
-   Was soll bewusst offenbleiben?
-   Welche Anti-Patterns wollen wir vermeiden?
-   Welche Regeln sollen später auch für KI-generierten Code gelten?

### Ergebnis des Tages

**Erste Version unserer Python Coding & OO Guidelines**

Diese bildet am zweiten Tag die Grundlage für die gemeinsame Squish- und
Testautomatisierungsarchitektur.
