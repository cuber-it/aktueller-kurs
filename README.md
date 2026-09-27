# Gesamtbild -- Python · Test-Automation · KI

## Ziel

In den drei Tagen entwickelt das Team schrittweise einen gemeinsamen
Engineering-Standard für Python-basierte Testautomatisierung mit Squish
und macht diesen Standard anschließend für den unterstützenden Einsatz
von KI nutzbar.

Der rote Faden:

**Python-/OO-Best-Practices →
Squish-/Testautomatisierungs-Best-Practices → gemeinsamer Standard →
Integration und Bereitstellung für KI**

------------------------------------------------------------------------

## Tag 1 -- Python + OO

### Schwerpunkt

**OO verstehen, vertiefen und einen gemeinsamen Python-/OO-Standard
entwickeln.**

### Inhalte

-   Objektorientierung in Python
-   Klassen und Verantwortlichkeiten
-   Kapselung
-   Vererbung vs. Komposition und Delegation
-   Abstraktionen in Python
-   Duck Typing, ABC und Protocol
-   Abhängigkeiten und Testbarkeit
-   Objektzustand und Lifecycle
-   Pythonische OO-Werkzeuge
-   Wartbare APIs
-   Module und Pakete
-   Type Hints
-   PEP 8
-   Docstrings
-   Naming-Konventionen
-   Magic Methods, soweit sinnvoll
-   Bestandscode analysieren und refactoren

### Arbeitsweise

Die Themen werden anhand von Code, Gegenbeispielen, Alternativen und
Übungen untersucht. Aus den Ergebnissen leitet das Team eigene Best
Practices und Regeln ab.

### Ergebnis

**Unser Python-/OO-Standard**

-   Coding Guidelines
-   Style Guide
-   OO- und Designregeln
-   Naming und Struktur
-   gemeinsame Best Practices

------------------------------------------------------------------------

## Tag 2 -- Testautomatisierung + Squish

### Schwerpunkt

**Die Python-/OO-Prinzipien auf die Testautomatisierung übertragen und
einen gemeinsamen Squish-/Testautomatisierungsstandard entwickeln.**

### Inhalte

-   Testautomatisierung als Disziplin
-   Was automatisieren -- und was nicht?
-   Kopplung und Änderungsursachen
-   Testarchitektur und Schichten
-   Trennung von Testlogik und technischer Umsetzung
-   Page Objects
-   Component Objects
-   Domain APIs
-   Tasks und Workflows
-   alternative Architekturansätze, einschließlich Screenplay
-   robuste Objektidentifikation
-   Synchronisation und stabile GUI-Interaktion
-   Setup und Teardown
-   Testdaten
-   Testorakel und Assertions
-   Wiederverwendung
-   Suites und automatisierte Ausführung
-   Reporting und Diagnostizierbarkeit
-   Umgang mit instabilen Tests
-   bestehende Tests auf den gemeinsamen Standard umbauen

### Arbeitsweise

Unterschiedliche Lösungs- und Architekturansätze werden nicht als Dogma
vermittelt, sondern anhand konkreter Probleme verglichen. Das Team
bewertet Nutzen, Kosten und Einsatzgrenzen und entscheidet, welche
Ansätze für die eigene Umgebung sinnvoll sind.

### Ergebnis

**Unser Python-/Squish-Testautomatisierungsstandard**

Der Python-/OO-Standard aus Tag 1 wird mit den Entscheidungen aus Tag 2
zusammengeführt:

-   Python Coding Guidelines
-   Squish Best Practices
-   Testarchitektur
-   Testdesign-Regeln
-   Regeln für Robustheit und Wartbarkeit
-   gemeinsame Konventionen für Testcode

------------------------------------------------------------------------

## Tag 3 -- KI als Supporting Tool

### Schwerpunkt

**Untersuchen, wo KI den bestehenden Testprozess sinnvoll unterstützen
kann, was technisch möglich ist und wie der gemeinsame Standard für die
KI nutzbar gemacht wird.**

KI übernimmt nicht den Testprozess. Sie wird gezielt als unterstützendes
Werkzeug eingesetzt.

### Inhalte

-   KI im bestehenden Entwicklungs- und Testworkflow
-   Claude Code als Coding Assistant
-   standardkonformes Erzeugen und Ändern von Python-/Squish-Code
-   Context Engineering
-   Bereitstellung von Corporate Rules, Style Guides und
    Architekturregeln
-   Referenzimplementierungen und Projektkontext
-   KI-Unterstützung beim Testdesign
-   Requirements analysieren
-   Testfälle und Grenzfälle ableiten
-   Gherkin als mögliche strukturierte Zwischenrepräsentation
-   KI als Reviewer und Sparringspartner
-   Refactoring und Konsistenzprüfung
-   Erkennen von Test Smells und Architekturverletzungen
-   Unterstützung bei Wartung und Fehleranalyse
-   technische Grenzen von LLM und Repositoryzugriff
-   MCP als kontrollierte Erweiterung um Werkzeuge und Fähigkeiten
-   eigener MCP-Server als praktische Live-Demo
-   mögliche Squish-Integration
-   Grenzen, Kontrolle und Datenschutz
-   gemeinsames Experimentieren: Was funktioniert technisch tatsächlich?

### Arbeitsweise

Die Teilnehmer untersuchen unterschiedliche Unterstützungsstufen
praktisch:

**Requirement → Testdesign → Implementierung → Review → Ausführung →
Analyse**

Für jede Stufe wird betrachtet:

-   Wo hilft KI?
-   Welchen Kontext benötigt sie?
-   Welche Teamregeln muss sie kennen?
-   Welche Werkzeuge benötigt sie?
-   Wo muss der Mensch entscheiden oder kontrollieren?
-   Was wollen wir tatsächlich in unserem Prozess einsetzen?

### Ergebnis

**KI-Unterstützung auf Basis unseres eigenen Engineering-Standards**

Der in Tag 1 und Tag 2 entwickelte Standard wird so aufbereitet, dass
Menschen und KI auf derselben Grundlage arbeiten können.

------------------------------------------------------------------------

## Gesamtentwicklung über die drei Tage

``` text
TAG 1
PYTHON + OO
────────────────────────
OO verstehen und vertiefen
Pythonische Best Practices
Coding-/Style-Konventionen
Bestandscode untersuchen
         │
         ▼
   UNSER PYTHON-
   OO-STANDARD
         │
         ▼
TAG 2
TESTAUTOMATISIERUNG + SQUISH
────────────────────────
Automatisierungsstrategie
Architektur
Page / Component / Task
Robustheit
Testdaten / Testorakel
CI / Diagnose / Flaky Tests
         │
         ▼
   UNSER PYTHON-
   SQUISH-STANDARD
         │
         ▼
TAG 3
KI ALS SUPPORTING TOOL
────────────────────────
Generieren und Ändern
Testdesign unterstützen
Reviewen
Refactoren
Analysieren
Corporate Rules / Context
MCP / technische Möglichkeiten
Grenzen / Datenschutz
         │
         ▼
 WIE MACHEN WIR UNSEREN
 STANDARD FÜR KI NUTZBAR?
```

------------------------------------------------------------------------

## Durchgängiges Workshop-Prinzip

Jede Einheit adressiert ein klar abgegrenztes Thema und verbindet
Trainerinput mit praktischer Arbeit und Diskussion.

``` text
Problem / Fragestellung
        ↓
Trainerinput
        ↓
Beispiele und Alternativen
        ↓
Teilnehmerarbeit
        ↓
Diskussion und Abwägung
        ↓
Merksatz
        ↓
Konsequenz für unseren Teamstandard
```

Jede Einheit besitzt einen **Merksatz**, der die zentrale fachliche
Erkenntnis festhält. Aus diesen Erkenntnissen entwickelt das Team seine
konkreten Standards, Best Practices und Corporate Rules.

Die Standards werden damit nicht vorgegeben, sondern während des
Workshops fachlich hergeleitet, diskutiert, entschieden und anschließend
gemeinsam gelebt.
