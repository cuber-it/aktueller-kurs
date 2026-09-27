# Tag 3 -- KI Engineering für Squish-Testautomatisierung

## Rahmen

-   Kurszeit: 09:00--17:00
-   Mittagspause: 1 Stunde
-   Zwei kurze Pausen
-   Zielgruppe: erfahrene Teilnehmer, die Squish und Claude Code bereits
    einsetzen
-   Die Generierung von Squish-Tests mit Claude Code ist bekannt und
    wird vorausgesetzt.
-   Einheit: ca. 45 Minuten
-   Pro Einheit: ca. 20 Minuten Trainerinput + ca. 25 Minuten
    Teilnehmerarbeit, gemeinsame Analyse, Experiment oder Übung
-   Schwerpunkt: systematischer Einsatz von KI über reine
    Codegenerierung hinaus
-   Didaktischer Grundansatz: bestehender Workflow → strukturierter
    KI-Workflow → Testdesign → Architekturkonformität → Toolzugriff →
    agentischer Workflow

## Ziel des Tages

Die Teilnehmer entwickeln den bestehenden Einsatz von Claude Code zur
Testgenerierung zu einem systematischen KI-gestützten
Testautomatisierungsprozess weiter.

Im Mittelpunkt stehen:

-   Context Engineering für bestehende Squish-Projekte
-   KI-gestützte Testanalyse statt unmittelbarer Codegenerierung
-   Gherkin als strukturierte Zwischendarstellung zwischen Anforderung
    und Implementierung
-   Einhaltung der an Tag 2 entwickelten Testarchitektur
-   Analyse, Review und Refactoring bestehender Testsuiten
-   MCP als Schnittstelle zwischen Claude Code, Squish und weiteren
    Werkzeugen
-   Übergang vom Coding Agent zum Test-Agenten
-   Vorteile, Grenzen und Kontrollmechanismen agentischer
    Testautomatisierung

## Tagesgliederung

  ------------------------------------------------------------------------------------------------
  Zeit               Einheit                       Trainer ca. 20 Min          Teilnehmer /
                                                                               Anwendung ca. 25
                                                                               Min
  ------------------ ----------------------------- --------------------------- -------------------
  **09:00--09:45**   **3-1 Bestandsaufnahme:       Bestehende Einsatzformen:   Eigenen bisherigen
                     Claude Code im Testprozess**  Generierung, Änderung und   Workflow zerlegen:
                                                   Analyse von Squish-Tests.   Input → Claude Code
                                                   Vom einzelnen Prompt zum    → Squish-Test →
                                                   systematischen              Review → Ausführung
                                                   Engineering-Workflow        

  **09:45--10:30**   **3-2 Context Engineering für Wie bekommt Claude Code     Gleiche Anforderung
                     Squish**                      Architektur, Object Map,    mit
                                                   vorhandene Tests,           unterschiedlichem
                                                   Konventionen und            Kontext bearbeiten
                                                   Domainwissen?               und Ergebnisse
                                                   Projektregeln, Beispiele    vergleichen
                                                   und                         
                                                   Referenzimplementierungen   

  **10:30--10:45**   **Pause**                                                 

  **10:45--11:30**   **3-3 Von Anforderungen zu    Requirement → Testanalyse → Aus einer
                     Testfällen -- Gherkin als     Szenarien → Gherkin →       fachlichen
                     IR**                          Squish/Python. Gherkin als  Anforderung mit
                                                   strukturierte Intermediate  Claude Code
                                                   Representation statt als    relevante Szenarien
                                                   BDD-Grundkurs               entwickeln und in
                                                                               Gherkin präzisieren

  **11:30--12:15**   **3-4 Von Gherkin zur         Step Definitions vs. Domain Claude Code
                     bestehenden Testarchitektur** API, Tasks, Page und        implementiert
                                                   Component Objects aus Tag   Szenarien unter
                                                   2; Mapping ohne redundante  Einhaltung der
                                                   Step-Definition-Schichten   vorhandenen
                                                                               Testarchitektur

  **12:15--13:15**   **Mittagspause**                                          

  **13:15--14:00**   **3-5 KI für Analyse, Review  Nicht nur Generierung:      Claude Code
                     und Refactoring**             Duplikate,                  analysiert eine
                                                   Architekturverletzungen,    vorhandene
                                                   fehlende Tests, Test-Smells Squish-Suite und
                                                   und Refactoring-Vorschläge  entwickelt
                                                                               begründete
                                                                               Verbesserungen

  **14:00--14:45**   **3-6 Vom Coding Agent zum    Grenzen reinen              Gemeinsam ein
                     Test-Agent -- MCP**           Repository-Zugriffs; MCP,   sinnvolles Toolset
                                                   Tools und Resources; AUT    für einen
                                                   und Squish als zusätzliche  Squish-Agenten
                                                   Wahrnehmungs- und           entwerfen
                                                   Aktionskanäle               

  **14:45--15:00**   **Pause**                                                 

  **15:00--15:45**   **3-7 MCP praktisch -- eigene Einen vorhandenen eigenen   Bestehenden MCP um
                     Lösung**                      Python-MCP-Server live      eine kleine
                                                   untersuchen: Architektur,   Fähigkeit erweitern
                                                   Tooldefinition, Parameter,  bzw. daraus ein
                                                   Rückgaben, Fehlerbehandlung Squish-bezogenes
                                                   und Claude-Code-Anbindung   Tool ableiten

  **15:45--16:30**   **3-8 Agentischer             Minimaler eigener           Requirement →
                     Squish-Workflow**             Squish-MCP und Einordnung   Gherkin →
                                                   gegenüber Qt Squish MCP     Implementierung →
                                                                               Squish ausführen →
                                                                               Ergebnis
                                                                               analysieren → Test
                                                                               korrigieren

  **16:30--17:00**   **Grenzen &                   Vertrauen, Guardrails,      Festlegen, welche
                     Architekturentscheidungen**   Autonomie, Prompt           Schritte autonom
                                                   Injection, deterministische laufen können und
                                                   Tests vs. probabilistischer an welchen Stellen
                                                   Agent, Kosten und           Kontrollpunkte
                                                   Reproduzierbarkeit          erforderlich sind
  ------------------------------------------------------------------------------------------------

## Evolutionsstufen des KI-Einsatzes

Der Tag betrachtet den KI-Einsatz nicht als einzelne Funktion, sondern
als zunehmende Integration in den Testprozess.

### Ebene 1 -- Codegenerierung

``` text
Anforderung
    ↓
Claude Code
    ↓
Squish/Python-Test
    ↓
Menschliches Review
```

Diese Arbeitsweise ist den Teilnehmern bereits bekannt und bildet den
Ausgangspunkt.

### Ebene 2 -- KI im Repository und in der Testarchitektur

``` text
Anforderung
    ↓
Claude Code
    ├── bestehende Tests
    ├── Architekturregeln
    ├── Page / Component Objects
    ├── Tasks / Domain API
    └── Projektkontext
    ↓
architekturkonforme Änderung
```

Die zentrale Frage lautet nicht mehr nur, ob Claude funktionierenden
Code erzeugen kann, sondern ob die Änderung in die bestehende
Testarchitektur passt.

### Ebene 3 -- Strukturierter Testentwurf

``` text
Anforderung
    ↓
Testanalyse
    ↓
Szenarien / Gherkin
    ↓
Review
    ↓
Implementierung
    ↓
Squish-Testarchitektur
```

Die Codegenerierung wird bewusst hinter die Testanalyse verschoben.

### Ebene 4 -- Agentischer Testworkflow

``` text
Anforderung
    ↓
Claude Code
    │
    ├── Repository
    ├── Testarchitektur
    ├── Gherkin / Testfälle
    └── MCP Tools
             │
             ▼
           Squish
             │
             ▼
            AUT
```

Der Agent kann nicht nur Code erzeugen, sondern über Werkzeuge mit der
Testumgebung interagieren, Tests ausführen, Ergebnisse analysieren und
weitere Aktionen daraus ableiten.

## Gherkin als Intermediate Representation

Gherkin wird nicht primär als BDD-Syntax vermittelt. Die Teilnehmer
kennen Testautomatisierung bereits; interessant ist die Rolle einer
expliziten, strukturierten Zwischenrepräsentation.

Der Workflow lautet:

``` text
Anforderung
     │
     ▼
Claude: Testanalyse
     │
     ▼
Szenarien / Gherkin
     │
     ▼
Review
     │
     ▼
Claude: Implementierung
     │
     ▼
Tasks / Domain API
     │
     ▼
Page / Component Objects
     │
     ▼
Squish
```

Dadurch lassen sich zwei getrennte Fragen behandeln:

1.  Haben wir die richtigen Tests entworfen?
2.  Haben wir diese Tests technisch richtig implementiert?

Die Teilnehmer untersuchen, ob diese Trennung gegenüber unmittelbarer
Codegenerierung Vorteile bei Nachvollziehbarkeit, Testabdeckung, Review
und Wartbarkeit bietet.

## Vergleichsexperiment: Drei Wege zum Squish-Test

Dasselbe Requirement wird mit drei unterschiedlichen Vorgehensweisen
bearbeitet.

### Variante A -- Direkte Generierung

``` text
Requirement → Claude Code → Squish-Test
```

### Variante B -- Testanalyse vor Implementierung

``` text
Requirement
    ↓
Testanalyse
    ↓
Gherkin
    ↓
Review
    ↓
Claude Code
    ↓
Squish-Test
```

### Variante C -- Architektur- und Tool-gestützter Workflow

``` text
Requirement
    ↓
Testanalyse / Gherkin
    ↓
Claude Code
    ├── Architekturkontext
    ├── bestehende Tests
    └── Projektregeln
    ↓
Implementierung
    ↓
MCP
    ↓
Squish / AUT
    ↓
Ergebnis
    ↓
Analyse / Korrektur
```

Verglichen werden unter anderem:

-   Testabdeckung
-   Nachvollziehbarkeit
-   Architekturkonformität
-   Wartbarkeit
-   Fehlinterpretationen
-   notwendiger menschlicher Review-Aufwand
-   Aufwand und Geschwindigkeit
-   Reproduzierbarkeit

## Context Engineering für Squish-Projekte

Claude Code benötigt für qualitativ hochwertige Änderungen mehr als die
unmittelbare Aufgabenbeschreibung.

Relevanter Kontext kann umfassen:

-   Projektstruktur
-   Architekturregeln
-   bestehende Page und Component Objects
-   Tasks und Domain APIs
-   Object Map und Namenskonventionen
-   Referenztests
-   Testdatenkonventionen
-   Regeln für Assertions
-   Setup und Cleanup
-   Logging und Reporting
-   bekannte technische Einschränkungen der AUT

Untersucht wird, welcher Kontext tatsächlich benötigt wird und wann
zusätzlicher Kontext nur Kosten und Komplexität erhöht.

## KI jenseits der Testgenerierung

Claude Code kann im Testprozess weitere Aufgaben übernehmen:

-   bestehende Tests analysieren
-   redundante Tests oder Abläufe erkennen
-   Test-Smells identifizieren
-   Architekturverletzungen finden
-   Refactoring-Vorschläge entwickeln
-   Page und Component Objects konsolidieren
-   Anforderungen gegen vorhandene Tests abgleichen
-   mögliche Testlücken identifizieren
-   vorhandene Tests an Architekturänderungen anpassen

Dabei bleibt die fachliche Bewertung der Ergebnisse ein eigener Schritt.

## MCP -- vom Coding Agent zum Test-Agenten

Repository-Zugriff ermöglicht Claude Code, Testcode zu verstehen und zu
verändern. Für einen echten Test-Agenten reicht dies nicht aus.

Über MCP können zusätzliche Fähigkeiten bereitgestellt werden.

Ein minimalistischer Squish-bezogener MCP könnte beispielsweise
Fähigkeiten anbieten wie:

``` text
run_test(...)
run_suite(...)
get_test_result(...)
get_log(...)
start_aut(...)
get_aut_state(...)
```

Je nach gewünschtem Autonomiegrad können weitere Interaktionen
hinzukommen.

Die zentrale Architekturfrage lautet:

> Welche Fähigkeiten benötigt der Agent wirklich und welche Fähigkeiten
> sollten bewusst nicht freigegeben werden?

## Eigener MCP-Server -- Live-Demo

Als praktische Grundlage wird ein bereits vorhandener eigener
Python-MCP-Server verwendet.

Die Teilnehmer verfolgen den Weg:

``` text
Claude Code
    │
    │ MCP
    ▼
eigener MCP-Server
    │
    ├── Tool A
    ├── Tool B
    └── Tool C
         │
         ▼
    reale Funktion
```

Betrachtet werden:

-   Aufbau des Servers
-   Tooldefinitionen
-   Parameter und Rückgabewerte
-   Fehlerbehandlung
-   Tool Contracts
-   Anbindung an Claude Code
-   Berechtigungen und Begrenzung der Fähigkeiten

Anschließend wird untersucht, wie aus demselben Prinzip ein kleiner
Squish-MCP entstehen kann.

## Vom eigenen MCP zu Squish MCP

Der selbst entwickelte bzw. demonstrierte Ansatz wird anschließend mit
dem offiziellen Squish-MCP-Ansatz eingeordnet.

Dabei geht es nicht darum, eine vollständige Alternative zu
implementieren.

Die interessante Frage lautet:

> Welche zusätzlichen Probleme muss eine produktionsfähige
> MCP-Integration für GUI-Testautomatisierung lösen?

Dazu gehören beispielsweise:

-   Zustand der AUT erfassen
-   UI-Objekte adressierbar machen
-   geeignete Informationen für das LLM bereitstellen
-   Toolergebnisse kompakt und eindeutig strukturieren
-   Fehlerzustände behandeln
-   Synchronisation
-   Kontext- und Tokenbedarf
-   Berechtigungen
-   reproduzierbare Ausführung

## Vorteile und Caveats

Vorteile und Risiken werden nicht nur am Ende behandelt, sondern auf
jeder Evolutionsstufe betrachtet.

### Mehr Kontext

**Vorteil:** bessere Kenntnis von Projekt und Architektur.

**Caveat:** höherer Tokenbedarf, potenziell irrelevanter Kontext und
mögliche Weitergabe zusätzlicher Informationen.

### Mehr Toolzugriff

**Vorteil:** der Agent kann reale Zustände untersuchen und Aktionen
ausführen.

**Caveat:** größere Fehler- und Angriffsfläche sowie stärkere
Auswirkungen falscher Entscheidungen.

### Mehr Autonomie

**Vorteil:** komplette Arbeitsabläufe können automatisiert werden.

**Caveat:** weniger unmittelbare menschliche Kontrolle und schwierigere
Reproduzierbarkeit.

### Generative KI in deterministischer Testautomatisierung

Besonders betrachtet wird der Unterschied zwischen:

``` text
deterministischer Testausführung
```

und

``` text
probabilistischer Entscheidungsfindung des Agenten
```

Daraus ergibt sich die Frage, welche Teile des Testprozesses weiterhin
deterministisch bleiben sollten und an welchen Stellen KI sinnvoll
eingesetzt werden kann.

## Abschlussfrage

Der Tag endet nicht mit der Frage:

> Was kann Claude Code alles?

Sondern mit:

> Welche Aufgaben unserer Testautomatisierung wollen wir an KI
> delegieren, welche Informationen und Werkzeuge benötigt sie dafür und
> welche Kontrollmechanismen brauchen wir?

Damit verbindet Tag 3 die Python-Architektur aus Tag 1 und die
Testautomatisierungsarchitektur aus Tag 2 mit einem systematischen KI-
und Agentenansatz.
