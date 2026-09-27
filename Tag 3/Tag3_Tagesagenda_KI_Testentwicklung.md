# Tag 3 – KI Engineering für Squish-Testautomatisierung

## Vom bestehenden KI-Einsatz zum gemeinsamen AI-assisted Test Engineering Standard

**09:00–17:00 Uhr · Mittagspause 12:15–13:15 Uhr**

### Tagesziel

Wir entwickeln den bestehenden Einsatz von Claude Code zur Testgenerierung zu einem systematischen KI-gestützten Testautomatisierungsprozess weiter.

Ausgangspunkt sind der reale Projektkontext, die vorhandene Squish-Testarchitektur und die an Tag 1 und Tag 2 erarbeiteten Standards. Wir untersuchen Context Engineering, strukturierten Testentwurf, architekturkonforme Implementierung, Analyse und Refactoring sowie den Übergang vom Coding Agent zum Test-Agenten über MCP.

Ziel ist ein belastbarer Workflow, in dem KI nicht isoliert Code erzeugt, sondern bestehende Projektstrukturen berücksichtigt, Tests ausführen kann und Ergebnisse in den weiteren Engineering-Prozess zurückführt.

---

## 09:00–09:45 · 3-1 – Bestandsaufnahme: Claude Code im Testprozess

Wie sieht der bestehende KI-gestützte Testworkflow tatsächlich aus – und wo liegen seine Grenzen?

- vorhandene Einsatzformen von Claude Code
- Testgenerierung, Änderung und Analyse
- Input → Claude Code → Squish-Test → Review → Ausführung
- welche Projektinformationen stehen Claude Code zur Verfügung?
- welche Entscheidungen trifft der Mensch, welche die KI?
- Medienbrüche und manuelle Rückkopplungen
- vom einzelnen Prompt zum Engineering-Workflow

**Merksatz:** Wir optimieren nicht den Prompt, sondern den gesamten Testentwicklungsprozess.

---

## 09:45–10:30 · 3-2 – Context Engineering für Squish

Wie bekommt Claude Code genau den Projektkontext, den es für architekturkonforme Änderungen benötigt?

- Projektstruktur und relevante Testbereiche
- vorhandene Tests als Kontext
- Architekturregeln aus Tag 2
- Page und Component Objects
- Tasks und Domain APIs
- Object Map und Namenskonventionen
- Testdaten-, Assertion-, Setup- und Cleanup-Regeln
- Referenzimplementierungen und gute Beispiele
- dauerhafter Projektkontext versus aufgabenspezifischer Kontext
- Nutzen und Kosten zusätzlichen Kontexts

**Merksatz:** Projektwissen gehört in den Projektkontext – die Aufgabe liefert nur den jeweils notwendigen Zusatzkontext.

---

### 10:30–10:45 · Pause

---

## 10:45–11:30 · 3-3 – Von Anforderungen zu Testfällen: Gherkin als Intermediate Representation

Wie bringen wir zwischen fachlicher Anforderung und Implementierung eine explizite, überprüfbare Testbeschreibung?

- Requirement → Testanalyse → Szenarien
- relevante Testfälle vor der Implementierung identifizieren
- Gherkin als strukturierte Intermediate Representation
- fachliche Absicht von technischer Umsetzung trennen
- Szenarien gemeinsam mit Claude Code entwickeln
- Mehrdeutigkeiten und fehlende Informationen sichtbar machen
- Review vor der Codegenerierung
- Gherkin nicht als Selbstzweck oder BDD-Grundkurs

**Merksatz:** Erst den Test präzisieren, dann den Testcode erzeugen.

---

## 11:30–12:15 · 3-4 – Von Gherkin zur bestehenden Testarchitektur

Wie wird aus einem fachlichen Szenario eine Implementierung, ohne eine zweite Testarchitektur zu erzeugen?

- Szenarien auf vorhandene Testarchitektur abbilden
- Domain API und Tasks wiederverwenden
- Page und Component Objects aus Tag 2 nutzen
- Step Definitions versus bestehende Abstraktionen
- redundante Step-Definition-Schichten vermeiden
- Objektidentifikation und Synchronisation in den richtigen Schichten belassen
- Claude Code auf Architekturkonformität ausrichten
- generierten Code gegen bestehende Projektregeln prüfen

**Merksatz:** Gherkin beschreibt das Verhalten – die bestehende Testarchitektur bestimmt die technische Umsetzung.

---

### 12:15–13:15 · Mittagspause

---

## 13:15–14:00 · 3-5 – KI für Analyse, Review & Refactoring

Welche Aufgaben kann Claude Code im bestehenden Testprojekt jenseits der Generierung übernehmen?

- bestehende Squish-Testsuiten analysieren
- redundante Tests und Abläufe erkennen
- Test-Smells identifizieren
- Architekturverletzungen finden
- fehlende oder inkonsistente Abstraktionen erkennen
- Page und Component Objects konsolidieren
- Refactoring-Vorschläge entwickeln
- Anforderungen gegen vorhandene Tests abgleichen
- mögliche Testlücken identifizieren
- Änderungen gegen die Standards aus Tag 1 und Tag 2 prüfen

**Merksatz:** Der Projektstandard ist die Review-Grundlage – nicht der Geschmack des Modells.

---

## 14:00–14:45 · 3-6 – Vom Coding Agent zum Test-Agenten: MCP

Was fehlt einem Coding Agent, um tatsächlich mit der Testumgebung arbeiten zu können?

- Grenzen des reinen Repository-Zugriffs
- Model Context Protocol als Werkzeugschnittstelle
- Tools und Resources
- Squish und AUT als zusätzliche Wahrnehmungs- und Aktionskanäle
- mögliche Fähigkeiten: Test starten, Suite starten, Ergebnis lesen, Logs auswerten, AUT-Zustand erfassen
- Tool Contracts und strukturierte Rückgaben
- notwendige versus unnötige Fähigkeiten
- Berechtigungen und Begrenzung des Aktionsraums
- vom Codegenerator zum Test-Agenten

**Merksatz:** Ein Test-Agent braucht nicht nur Projektwissen, sondern kontrollierten Zugriff auf die Testumgebung.

---

### 14:45–15:00 · Pause

---

## 15:00–15:45 · 3-7 – MCP praktisch: vom eigenen Server zur Squish-Anbindung

Wie wird aus dem MCP-Konzept eine konkrete, kontrollierbare Werkzeuganbindung?

- bestehende und selbst gebaute MCP-Server vergleichen
- Aufbau des Servers
- Tooldefinitionen
- Parameter und Rückgabewerte
- Fehlerbehandlung
- Tool Contracts
- Anbindung an Claude Code
- Berechtigungen und Begrenzung der Fähigkeiten
- kleine Fähigkeit exemplarisch erweitern oder ableiten
- Übertragung des Prinzips auf Squish
- Einordnung gegenüber einer produktionsfähigen Squish-MCP-Integration

**Merksatz:** Gute Agentenwerkzeuge sind klein, eindeutig, überprüfbar und auf ihren Zweck begrenzt.

---

## 15:45–16:30 · 3-8 – Agentischer Squish-Workflow

Die bisherigen Bausteine werden zu einem geschlossenen KI-gestützten Testworkflow verbunden.

- Requirement analysieren
- Szenarien und Gherkin entwickeln
- vorhandene Testarchitektur berücksichtigen
- Squish/Python-Test implementieren
- Squish über Werkzeuge ansprechen
- Test ausführen
- Ergebnis und Logs analysieren
- Fehlerursache bestimmen
- Test oder Implementierung korrigieren
- erneut ausführen und verifizieren
- menschliche Kontrollpunkte festlegen

**Merksatz:** Aus Testgenerierung wird Test Engineering, wenn Ausführung und Ergebnis wieder in den Arbeitsprozess zurückfließen.

---

## 16:30–17:00 · Standards Session

### Wie wollen wir KI künftig in unserer Testautomatisierung einsetzen?

Die Erkenntnisse des Tages werden mit den Standards aus Tag 1 und Tag 2 zu einem gemeinsamen KI-gestützten Engineering-Vorgehen konsolidiert.

- Welchen Projektkontext stellen wir dauerhaft bereit?
- Welche Rolle spielt Gherkin bzw. eine strukturierte Testrepräsentation?
- Welche Regeln muss KI-generierter Code erfüllen?
- Welche Review- und Refactoring-Aufgaben wollen wir KI-gestützt durchführen?
- Welche Tools benötigt ein Test-Agent?
- Welche Fähigkeiten wollen wir bewusst nicht freigeben?
- Welche Schritte dürfen autonom ausgeführt werden?
- Wo sind menschliche Kontrollpunkte erforderlich?
- Wie behandeln wir Vertrauen, Guardrails und Prompt Injection?
- Wie sichern wir Reproduzierbarkeit und nachvollziehbare Ergebnisse?

### Ergebnis des Tages

**Erste Version unserer AI-assisted Test Engineering Guidelines**

Diese verbindet die Ergebnisse aller drei Tage:

**Python-/OO-Standard → Squish-/Testautomatisierungsstandard → KI-gestützter Test-Engineering-Workflow**

Der resultierende Workflow reicht damit von der Anforderung und Testanalyse über die architekturkonforme Implementierung bis zur kontrollierten Ausführung, Ergebnisanalyse und Korrektur durch einen toolgestützten Test-Agenten.
