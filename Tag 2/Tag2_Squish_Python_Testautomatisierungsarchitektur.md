# Tag 2 -- Testautomatisierungsarchitektur mit Squish & Python

## Rahmen

- Kurszeit: 09:00--17:00
- Mittagspause: 12:15--13:15
- Zwei kurze Pausen
- Zielgruppe: erfahrene Teilnehmer, die bereits mit Squish und der vorhandenen Testautomatisierung arbeiten
- Einheit: ca. 45 Minuten
- Pro Einheit: ca. 20 Minuten Trainerinput + ca. 25 Minuten Teilnehmerarbeit, gemeinsame Analyse oder Übung
- Squish-Grundlagen werden vorausgesetzt.
- Schwerpunkt: Architektur und Design wartbarer GUI-Testautomatisierung mit Squish, Qt und Python
- Ausgangspunkt: eine bereits vorhandene und gewachsene Testautomatisierungsarchitektur
- Didaktischer Grundansatz: vorhandene Lösung verstehen → Konzept bzw. Alternative kennenlernen → Problem, Nutzen und Kosten untersuchen → auf das eigene Projekt beziehen → begründete Entscheidung

## Ziel des Tages

Die Teilnehmer betrachten ihre vorhandene Squish-Testautomatisierung als Softwarearchitektur. Im Mittelpunkt steht nicht die Bedienung von Squish und auch nicht der Entwurf einer neuen Musterarchitektur.

Das bestehende Projekt besitzt bereits wesentliche Architekturbausteine: UI- und Control-Abstraktionen, wiederverwendbare Helper, Verifikationsmechanismen, Target-Abstraktionen, Lifecycle-Mechanismen sowie Regeln für Synchronisation und Testzustand. Diese Strukturen werden sichtbar gemacht und mit etablierten Konzepten und Alternativen verglichen.

Page Objects, Component Objects, Domain APIs, Task-/Workflow-Layer, Screenplay und direkte Squish-Nutzung werden deshalb nicht als Reifegrade oder Zielvorgaben behandelt, sondern als **Katalog möglicher Konzepte**. Für jedes Konzept wird untersucht:

- Welches Problem adressiert es?
- Welche Idee davon ist im Projekt bereits vorhanden?
- Welchen zusätzlichen Nutzen könnte es bringen?
- Welche Komplexität oder Nachteile entstehen?
- Ist es für die bestehende Architektur relevant, bereits gelöst oder bewusst nicht erforderlich?

Die Python-/OO-Prinzipien aus Tag 1 bilden die gemeinsame Sprache für diese Diskussion. Ergebnis des Tages sind begründete projektspezifische Regeln für die Weiterentwicklung der vorhandenen Testautomatisierung.

## Tagesgliederung

| Zeit | Einheit | Trainer ca. 20 Min | Teilnehmer / Anwendung ca. 25 Min |
|---|---|---|---|
| **09:00--09:45** | **2-1 Die vorhandene Squish-Architektur sichtbar machen** | Schichten, Verantwortlichkeiten und Kopplungen der vorhandenen Testautomatisierung; Squish Runtime, GUI/AUT, Controls, UI-Modelle, Helper, Verifikation, Lifecycle und Target-Abstraktion | Vorhandene Strukturen einordnen, Verantwortlichkeiten und Änderungsursachen identifizieren |
| **09:45--10:30** | **2-2 UI-Abstraktion: Page Objects, Screen Models & bestehende Lösung** | Page Object als Referenzkonzept; öffentliche Test-API, Object Map/Objektidentifikation, UI- und AUT-Grenzen, Aktionen, Zustandsabfragen und Verifikation | Vorhandene UI-Abstraktion gegen POM-Ideen spiegeln; Gemeinsamkeiten, Unterschiede, Nutzen und Grenzen diskutieren |
| **10:30--10:45** | **Pause** | | |
| **10:45--11:30** | **2-3 Controls, Component Objects & Synchronisation** | generische Controls, Component Objects, wiederverwendbare Qt-Widgets, dünne vs. intelligente Controls, zustandsorientiertes Warten, Interaction+Wait, Diagnosefähigkeit | Vorhandene Controls und UI-Komponenten untersuchen; Verantwortungs- und Synchronisationsgrenzen diskutieren |
| **11:30--12:15** | **2-4 Von technischer Test-API zu fachlicher Testsprache** | vorhandene technische Test-API; Facade, Domain API, Fluent Interface; technische Aktion vs. fachliche Absicht; Nutzen und Kosten zusätzlicher Abstraktion | Bestehende APIs untersuchen und für konkrete Fälle prüfen, ob eine fachlichere API Mehrwert bringt |
| **12:15--13:15** | **Mittagspause** | | |
| **13:15--14:00** | **2-5 Wiederverwendbare Abläufe: Tasks, Workflows & Helper** | vorhandene Helper; UI-Verantwortung vs. Ablaufverantwortung; Tasks, Workflows und Service-Layer als mögliche Konzepte | Bestehende Helper klassifizieren und an konkreten Abläufen alternative Verantwortungsgrenzen vergleichen |
| **14:00--14:45** | **2-6 Architekturvarianten: POM, Tasks, Screenplay & direkte Tests** | POM/Component + Task, Actor--Task--Interaction, direkte Squish-Tests und hybride Ansätze; Flexibilität vs. Boilerplate und Indirektion | Ein konkretes Problem mit verschiedenen Ansätzen modellieren und gegen die vorhandene Lösung halten |
| **14:45--15:00** | **Pause** | | |
| **15:00--15:45** | **2-7 Testzustand, Daten, Lifecycle & Testorakel** | Setup/Cleanup, Test-Wrapper, Testdaten und Konfiguration, Target-Abstraktion, Verifikationsobjekte, Assertions, Diagnose und Resultate | Vorhandene Mechanismen analysieren und mögliche Varianten für Daten, Zustand und Oracles bewerten |
| **15:45--16:30** | **2-8 Architektur-Review am bestehenden Squish-Projekt** | Moderation anhand konkreter Änderungs- und Fehlerfälle | Bestehende Entscheidungen begründen; Alternativen prüfen; bewusst beibehalten, vereinfachen, ergänzen oder offenlassen |
| **16:30--17:00** | **Standards Session** | Erkenntnisse und Trade-offs zusammenführen | Projektspezifische Squish & Test Automation Guidelines als MUST / SHOULD / MAY / DON'T bzw. offene Frage formulieren |

## Vorhandene Architektur als Ausgangspunkt

Das Kundenmaterial zeigt bereits eine geschichtete Testautomatisierungsarchitektur. Für den Workshop besonders relevant sind:

- Control-/Widget-Abstraktionen oberhalb der direkten Squish API
- UI-/Screen-bezogene Abstraktionen
- wiederverwendbare Interaktions- und Test-Helper
- spezialisierte Verifikationsmechanismen und Testorakel
- Target-Abstraktionen
- Test-Wrapper und Lifecycle-Mechanismen
- Testkonfiguration und Testdaten
- zustandsorientierte Synchronisationsmechanismen
- Diagnose-, Logging- und Resultatmechanismen

Diese Strukturen werden **nicht vorsorglich ersetzt**. Sie liefern die konkreten Bezugspunkte, an denen die Architekturkonzepte des Tages diskutiert werden.

## Konzeptkatalog

Im Verlauf des Tages werden insbesondere folgende Konzepte untersucht:

| Konzept | Kernidee | Leitfrage im bestehenden Projekt |
|---|---|---|
| **Direkter Squish-Testcode** | Test verwendet Squish unmittelbar | Wann ist direkte Nutzung die klarste und wirtschaftlichste Lösung? |
| **Control-/Widget-Abstraktion** | elementare UI-Interaktionen werden gekapselt | Wie viel Verhalten und Synchronisation soll ein Control besitzen? |
| **Page / Screen Object** | UI-Bereiche werden hinter einer stabileren API gekapselt | Welche Ideen davon enthält die vorhandene UI-Abstraktion bereits? |
| **Component Object** | wiederverwendbare UI-Komponenten werden separat modelliert | Welche Qt-Komponenten benötigen eine eigene Verantwortung? |
| **Fluent / Domain API** | Tests drücken stärker fachliche Absicht aus | Wann verbessert eine weitere API-Schicht Lesbarkeit und wann erzeugt sie nur Indirektion? |
| **Task / Workflow Layer** | wiederkehrende Abläufe liegen oberhalb einzelner UI-Bereiche | Welche vorhandenen Helper sind bereits Workflows und wo liegen sinnvolle Grenzen? |
| **Screenplay** | Actor → Task → Interaction | Welches konkrete Problem könnte Screenplay besser lösen als die vorhandene Struktur? |
| **Hybrid** | Konzepte werden gezielt kombiniert | Welche Kombination existiert bereits und welche Ergänzungen wären begründbar? |

## Architektur nicht als Reifegrad

Die folgende Darstellung ist **kein Entwicklungspfad**, sondern zeigt unterschiedliche mögliche Schnitte.

Eine minimale Struktur kann völlig ausreichend sein:

```text
Test
  ↓
Squish
```

Eine UI-Abstraktion kann technische Details kapseln:

```text
Test
  ↓
UI-Abstraktion
  ↓
Squish
```

In einer anderen Lösung können Komponenten und Workflows getrennte Verantwortungen besitzen:

```text
Test
  ↓
Task / Workflow
  ↓
UI-/Screen-Abstraktion
  ↓
Controls / Components
  ↓
Squish
  ↓
Qt-AUT
```

Eine alternative Modellierung kann sich beispielsweise am Screenplay Pattern orientieren:

```text
Actor
  ↓
Task
  ↓
Interaction
  ↓
Squish
  ↓
Qt-AUT
```

Keine dieser Darstellungen ist automatisch „weiter entwickelt“. Jede zusätzliche Schicht muss ein konkretes Problem lösen und ihren Preis rechtfertigen.

## Querschnittsthemen

### Objektidentifikation und Object Map

Objektidentifikation ist nicht nur Implementierungsdetail. Sie beeinflusst Kopplung, Wartbarkeit und Diagnosefähigkeit der gesamten UI-Abstraktion.

Zu untersuchen sind insbesondere:

- Verantwortlichkeit für Objektnamen und Identifikationswissen
- stabile versus fragile Eigenschaften
- Container- und Kontextbeziehungen
- Verhältnis zwischen Object Map, Controls und UI-Abstraktionen
- Auswirkungen von Änderungen der Qt-Oberfläche

### Synchronisation

Synchronisation wird als eigenständiges Architekturthema behandelt.

Fragen sind:

- Wo ist der relevante Zustand bekannt?
- Welche Ebene soll auf diesen Zustand warten?
- Wann ist Interaction + Wait sinnvoll?
- Welche Synchronisation darf ein Control intern übernehmen?
- Welche Wartevorgänge müssen für Test und Diagnose sichtbar bleiben?
- Wie werden AUT-Wechsel und Neustarts behandelt?

### Testdaten und Zustand

- Konfiguration und Testdaten
- Fixtures und Zustandsaufbau
- datenorientierte Objekte, Enums und mögliche Builder
- Setup über UI versus andere verfügbare Schnittstellen
- Isolation zwischen Tests
- Lifecycle und Cleanup

### Verifikation und Testorakel

- direkte Verifikation im Test
- wiederverwendbare Verifikationsobjekte
- UI- versus fachliche Assertions
- Trennung von Aktion, Beobachtung und Bewertung
- Fehlermeldungen und Diagnosekontext

### Diagnose

Eine Abstraktion ist nur dann hilfreich, wenn Fehler weiterhin lokalisierbar bleiben.

Dazu gehören:

- aussagekräftige Fehlergrenzen
- Logging und Reporting
- Resultatartefakte
- relevante Zustandsinformationen
- Unterscheidung zwischen Testfehler, Infrastruktur-/Umgebungsproblem und AUT-Fehler

## Verbindung zu Tag 1

Die Python- und OO-Konzepte aus Tag 1 werden nicht als neue Architekturvorgaben verwendet. Sie bilden die gemeinsame Sprache, mit der die vorhandene Architektur und mögliche Alternativen untersucht werden:

- **Verantwortlichkeiten und Kapselung** für Controls, UI-Abstraktionen, Helper und Oracles
- **Komposition und Delegation** für die Zusammenarbeit vorhandener Komponenten
- **Duck Typing, Protocol und andere Abstraktionsformen** dort, wo tatsächlich ein Vertrag benötigt wird
- **sichtbare und kontrollierbare Abhängigkeiten** für technische Komponenten und Targets
- **Lifecycle, Zustand und Cleanup** für AUT, Testumgebung und Ressourcen
- **API-Design** für verständliche und stabile Testinterfaces
- **MUST / SHOULD / MAY / DON'T** zur Formulierung gemeinsamer Teamregeln

Damit dient Tag 1 nicht als Baukasten, aus dem möglichst viele OO-Techniken eingebaut werden, sondern als Entscheidungsgrundlage.

## Didaktische Leitlinie

Nicht:

> Page Object ist Best Practice, deshalb verwenden wir Page Objects.

Auch nicht:

> Die vorhandene Architektur entspricht nicht Pattern X und muss deshalb umgebaut werden.

Sondern:

> Welches Problem löst die vorhandene Struktur? Welche Alternativen gäbe es? Was würden wir durch eine Änderung gewinnen und was würde sie kosten?

Die vorhandene Testautomatisierung ist deshalb der wichtigste Referenzpunkt. Externe Patterns und Architekturkonzepte liefern Vergleichsmodelle und zusätzliche Optionen.

## Architektur-Review

Zum Abschluss wird keine künstliche Zielarchitektur entworfen. Die Teilnehmer betrachten ausgewählte Teile bzw. Problemstellungen ihrer bestehenden Squish-Testautomatisierung.

Mögliche Analysefragen:

1. Welche Verantwortung besitzt die betrachtete Komponente heute?
2. Welche Änderungen treffen sie typischerweise?
3. Welche Kopplungen sind notwendig und welche vermeidbar?
4. Wo liegen Objektidentifikation und Synchronisationswissen?
5. Sind UI-Interaktion, Workflow und Verifikation nachvollziehbar getrennt?
6. Welche vorhandenen Abstraktionen funktionieren gut und warum?
7. Wo entsteht unnötige Indirektion oder versteckte Testlogik?
8. Welches alternative Konzept könnte ein konkretes Problem lösen?
9. Welche zusätzliche Komplexität würde dadurch entstehen?

Das mögliche Ergebnis einer Diskussion ist ausdrücklich nicht nur „ändern“. Zulässige Entscheidungen sind:

- **beibehalten**
- **vereinfachen**
- **ergänzen**
- **gezielt umbauen**
- **bewusst nicht übernehmen**
- **offenlassen und weitere Evidenz sammeln**

## Standards Session

Die Ergebnisse werden in eine erste Version der **Squish & Test Automation Guidelines** überführt.

Mögliche Regelbereiche:

- Verantwortlichkeiten der vorhandenen Abstraktionsschichten
- direkte Nutzung der Squish API
- Object Map und Objektidentifikation
- Controls und wiederverwendbare UI-Komponenten
- Synchronisation und zulässige Wait-Strategien
- Helper, Tasks und Workflows
- Testdaten und Zustandsaufbau
- Lifecycle und Cleanup
- Verifikation und Testorakel
- Diagnose und Logging
- Regeln für neue Abstraktionen
- Umgang mit begründeten Ausnahmen

Nicht jede Erkenntnis wird automatisch verbindliche Regel. Wie an Tag 1 wird unterschieden zwischen:

- **MUST**
- **SHOULD**
- **MAY**
- **DON'T**
- **offene Frage**

## Übergang zu Tag 3

Am Ende steht nicht die Frage, wie eine KI eine neu entworfene Testarchitektur erzeugen soll, sondern:

> Welche Informationen, Regeln, Fähigkeiten und Werkzeuge benötigt Claude Code, um die vorhandene und gemeinsam verstandene Testarchitektur korrekt zu nutzen und innerhalb ihrer vereinbarten Regeln weiterzuarbeiten?

Damit entsteht der Übergang von der explizit verstandenen Testautomatisierungsarchitektur zu KI-gestütztem Engineering mit Squish.
