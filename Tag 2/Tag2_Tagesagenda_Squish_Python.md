# Tag 2 – Testautomatisierungsarchitektur mit Squish & Python

## Die bestehende Architektur verstehen, vergleichen und gemeinsam weiterentwickeln

**09:00–17:00 Uhr · Mittagspause 12:15–13:15 Uhr**

### Tagesziel

Wir betrachten die vorhandene Squish-Testautomatisierung als gewachsene Softwarearchitektur. Ausgangspunkt ist ausdrücklich **nicht** die Annahme, dass eine neue Architektur eingeführt werden muss: Im bestehenden Projekt sind bereits UI- und Control-Abstraktionen, wiederverwendbare Test- und Workflow-Helper, Target-Abstraktionen, Lifecycle-Mechanismen sowie Regeln für Synchronisation und Verifikation vorhanden.

Diese Strukturen machen wir zunächst sichtbar und ordnen sie ein. Anschließend vergleichen wir sie mit etablierten Architekturkonzepten wie Page/Component Objects, Domain APIs, Task-/Workflow-Layern und Screenplay. Dabei geht es jeweils um das konkrete Problem, das ein Ansatz löst, seinen Nutzen, seine Kosten und seine Grenzen.

Die Python-/OO-Prinzipien aus Tag 1 dienen dabei als gemeinsame Entwurfsgrundlage. Ziel des Tages ist **keine Musterarchitektur**, sondern ein begründeter gemeinsamer Squish-/Testautomatisierungsstandard für das vorhandene Projekt.

---

## 09:00–09:45 · 2-1 – Die vorhandene Squish-Architektur sichtbar machen

Welche Architektur steckt bereits in unserer Testautomatisierung – und welche Probleme löst sie?

- Testfälle, UI-Modelle, Controls, Test-Helper und gemeinsame Libraries
- technische Squish-Schicht versus projektspezifische Abstraktionen
- UI-/Screen-Abstraktion und AUT-Grenzen
- wiederverwendbare Verifikationsobjekte
- Test-Wrapper, Lifecycle und Target-Abstraktion
- vorhandene Testdaten- und Konfigurationsmechanismen
- Kopplungen an GUI, Squish Runtime, AUT und Projektarchitektur
- Qualitätsziele: Wartbarkeit, Stabilität, Diagnosefähigkeit und Verständlichkeit
- Architektur nicht nach Pattern-Namen, sondern nach Verantwortlichkeiten untersuchen

**Merksatz:** Bevor wir neue Patterns diskutieren, müssen wir verstehen, welche Architektur bereits existiert und warum.

---

## 09:45–10:30 · 2-2 – UI-Abstraktion: Page Objects, Screen Models & bestehende Lösung

Welche Verantwortung soll eine UI-Abstraktion übernehmen – und wie verhält sich das zu unserer vorhandenen Struktur?

- Page Object als Referenzkonzept, nicht als Zielvorgabe
- vorhandene UI-/Screen-Helper und ihre Verantwortlichkeiten
- öffentliche Test-API versus technische Squish-Details
- Object Map, Objektidentifikation und UI-Struktur
- visuelle Navigation versus technische AUT-/Fenstergrenzen
- Aktionen, Zustandsabfragen und Verifikation
- große versus fokussierte UI-Objekte
- Nutzen, Grenzen und typische Fehlentwicklungen des Page-Object-Ansatzes
- Vergleich: Was davon haben wir bereits, was bewusst anders?

**Merksatz:** Entscheidend ist nicht, ob etwas „Page Object“ heißt, sondern ob seine Verantwortung und Grenze sinnvoll gewählt sind.

---

### 10:30–10:45 · Pause

---

## 10:45–11:30 · 2-3 – Controls, Component Objects & Synchronisation

Wo gehört elementares UI-Verhalten hin – und wie intelligent darf eine UI-Komponente werden?

- generische Controls als Abstraktion über Squish
- Component Objects für wiederverwendbare Qt-Widgets und UI-Bausteine
- Dialoge, Listen, Tabellen, Trees, Toolbars und Custom Widgets
- dünner Wrapper versus „Smart Control“
- Interaction + Wait als gemeinsame Operation
- zustandsorientiertes Warten statt pauschaler Sleeps
- Synchronisation auf Control-, Component-, Page- oder Testebene
- AUT-Wechsel, Restart und Application Context als Architekturthema
- Wiederverwendung versus versteckte Nebenwirkungen
- Diagnosefähigkeit trotz Kapselung

**Merksatz:** Synchronisation gehört dorthin, wo der relevante Zustand verstanden wird – aber sie darf Verhalten nicht unsichtbar machen.

---

## 11:30–12:15 · 2-4 – Von technischer Test-API zu fachlicher Testsprache

Wie weit sollten wir Squish-Technik kapseln – und wann hilft eine Domain API wirklich?

- vorhandene technische Test-API und wiederverwendbare Libraries
- technische Aktion versus fachliche Absicht
- Facade und intention-revealing API
- Domain-specific Test API
- Fluent Interfaces als mögliche Ausdrucksform
- Object Map, Synchronisation und technische Details hinter geeigneten Grenzen
- Assertions und Rückgabewerte: was bleibt für den Test sichtbar?
- Lesbarkeit versus zusätzliche Indirektion
- direkte Squish-Nutzung als legitime Option
- YAGNI: keine Abstraktion ohne konkretes Problem

**Merksatz:** Eine zusätzliche API-Schicht lohnt sich nur, wenn sie relevante Testabsicht klarer ausdrückt oder echte technische Komplexität kapselt.

---

### 12:15–13:15 · Mittagspause

---

## 13:15–14:00 · 2-5 – Wiederverwendbare Abläufe: Tasks, Workflows & Helper

Wann wird aus wiederverwendetem Testcode eine eigene Workflow-Abstraktion?

- vorhandene bereichsspezifische Test-Helper untersuchen
- UI-Verantwortung versus Ablaufverantwortung
- Tasks und Workflows über mehrere UI-Bereiche
- wiederkehrende Navigation und fachliche Abläufe
- technische Helper versus fachliche Tasks
- Zustand und Lifecycle über längere Abläufe
- Komposition vorhandener UI- und Control-Abstraktionen
- Wiederverwendung versus versteckte Testlogik
- Service-Layer als mögliche Variante – und wann er keinen Mehrwert bringt
- Verantwortungsgrenzen mit den OO-Prinzipien aus Tag 1 prüfen

**Merksatz:** Wiederverwendung allein rechtfertigt keine neue Schicht – ein Workflow braucht eine eigene, erkennbare Verantwortung.

---

## 14:00–14:45 · 2-6 – Architekturvarianten: POM, Tasks, Screenplay & direkte Tests

Welche Architekturansätze stehen uns zur Verfügung – und welches Problem müsste eine Änderung überhaupt lösen?

- vorhandene Architektur als Ausgangspunkt
- Page/Component Objects + Task Layer als eine mögliche Kombination
- Screenplay: Actor – Task – Interaction
- Unterschiede zur bestehenden Control-/Helper-Struktur
- direkter Testcode als bewusste Minimalarchitektur
- hybride Ansätze
- zusätzliche Flexibilität versus Boilerplate und Indirektion
- Auswirkungen auf Navigation, Fehlersuche und Wartung
- Migration versus evolutionäre Ergänzung
- Entscheidung anhand konkreter Änderungs- und Fehlerfälle

**Merksatz:** Architekturvarianten sind Werkzeuge – keine Reifegrade. Entscheidend ist das Problem, das sie besser lösen sollen.

---

### 14:45–15:00 · Pause

---

## 15:00–15:45 · 2-7 – Testzustand, Daten, Lifecycle & Testorakel

Was muss eine belastbare Testarchitektur außer UI-Interaktion kontrollieren?

- Test-Wrapper, Setup, Cleanup und Lifecycle
- Ausgangszustand und Isolation
- Testdaten und Konfiguration
- Enums, Config Objects, Builder und datengetriebene Ansätze als Varianten
- UI-basierter Zustandsaufbau versus andere Schnittstellen
- Target-Abstraktion und externe Beobachtung
- Verifikationsobjekte und spezialisierte Testorakel
- Assertions: Testfall, UI-Abstraktion oder Oracle-Schicht?
- Fehlerdiagnose, Logging und Resultatartefakte
- Testfehler, Umgebungsfehler und AUT-Fehler unterscheidbar halten

**Merksatz:** Testarchitektur organisiert nicht nur Aktionen – sie kontrolliert Zustand, Daten, Beobachtung und Diagnose.

---

## 15:45–16:30 · 2-8 – Architektur-Review am bestehenden Squish-Projekt

Wir wenden die Konzepte nicht auf eine künstliche Zielarchitektur an, sondern auf die vorhandene Lösung.

- vorhandene Schichten und Verantwortlichkeiten gemeinsam einordnen
- bewährte Strukturen identifizieren und begründen
- unklare oder überlappende Verantwortlichkeiten diskutieren
- Control, Component, UI-Modell, Helper, Workflow und Oracle unterscheiden
- konkrete Änderungs- und Fehlerszenarien durchspielen
- prüfen, wo bestehende Abstraktionen tragen
- alternative Lösungen für ausgewählte Problemstellen vergleichen
- bewusst entscheiden: beibehalten, vereinfachen, ergänzen oder offenlassen
- Trade-offs dokumentieren statt „Best Pattern“ wählen

**Merksatz:** Gute Architekturarbeit beginnt im Brownfield mit Verstehen und begründeten Entscheidungen – nicht mit dem Austausch funktionierender Strukturen.

---

## 16:30–17:00 · Standards Session

### Was wollen wir künftig gemeinsam so machen?

Aus der Analyse der vorhandenen Architektur und dem Vergleich der Alternativen entsteht ein erster gemeinsamer **Squish-/Testautomatisierungsstandard**.

- Welche vorhandenen Architekturentscheidungen wollen wir ausdrücklich beibehalten?
- Welche Verantwortlichkeiten gehören in Controls, UI-/Component-Objekte, Tasks und Tests?
- Wann darf direkt auf Squish zugegriffen werden?
- Welche Regeln gelten für Object Map und Objektidentifikation?
- Wo kapseln wir Synchronisation und wie vermeiden wir pauschale Wartezeiten?
- Wie behandeln wir AUT-Wechsel, Restart und Application Context?
- Wo gehören Assertions und Testorakel hin?
- Wie behandeln wir Testdaten, Zustand, Setup und Cleanup?
- Wann rechtfertigt Wiederverwendung eine neue Abstraktion – und wann nicht?
- Welche Regeln sind verbindlich, welche Empfehlungen und welche Fragen bleiben bewusst offen?
- Welche dieser Regeln müssen später auch für KI-generierten Testcode explizit verfügbar sein?

### Ergebnis des Tages

**Erste Version unserer Squish & Test Automation Guidelines**

Sie dokumentiert nicht eine neu erfundene Zielarchitektur, sondern die gemeinsam verstandenen und begründeten Regeln für die Weiterentwicklung der vorhandenen Testautomatisierung.

Sie baut auf den Python Coding & OO Guidelines aus Tag 1 auf und bildet die technische Grundlage für den KI-gestützten Engineering-Workflow an Tag 3.

### Übergang zu Tag 3

Wenn diese Architekturregeln für Menschen nachvollziehbar und explizit sind: **Welchen Projektkontext, welche Regeln und welche Werkzeuge benötigt Claude Code, um innerhalb genau dieser Architektur zuverlässig arbeiten zu können?**
