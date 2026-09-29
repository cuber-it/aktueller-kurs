---
name: python-teamstandard
description: Verbindliche Python-Engineering-Regeln für Erzeugung, Änderung, Review und Refactoring von Python-Code.
---

# Python Teamstandard

Wende diese Regeln auf Python-Code an. Bestehende Projektkonventionen und öffentliche Verträge haben Vorrang. Bei einem notwendigen Regelbruch: kurz benennen und begründen.

## Prioritäten

1. Korrektheit und explizite Anforderung
2. Bestehende Architektur und öffentliche APIs
3. Dieser Skill
4. Persönliche Stilpräferenz

## Regeln

### Design
- **MUST:** Idiomatisches Python verwenden; keine mechanische Java-/C#-Übertragung.
- **MUST:** Jede nichttriviale Klasse hat eine klar benennbare Verantwortung.
- **MUST:** Invarianten im verantwortlichen Objekt schützen.
- **SHOULD:** Direkten Attributzugriff nutzen; `property` erst bei Validierung, Berechnung oder kontrollierter Mutation.
- **DON'T:** Keine God Objects oder Sammelklassen wie `Utils`/`Helpers`/`Common` für unabhängige Aufgaben.
- **DON'T:** Keine vorsorglichen Getter/Setter oder unnötigen Klassen.

### Vererbung und Abstraktion
- **MUST:** Vererbung nur für echte Typbeziehungen; Untertypen müssen den Vertrag des Basistyps erfüllen.
- **SHOULD:** Komposition für Zusammenarbeit, Delegation für weitergereichtes/ergänztes Verhalten.
- **DON'T:** Keine Vererbung nur zur Codewiederverwendung; keine `BaseTest`-Werkzeugkisten.
- **MUST:** Neue Abstraktionen brauchen einen konkreten aktuellen Nutzen.
- **SHOULD:** Kleinste ausreichende Form wählen: Duck Typing → `Protocol` → `ABC`, je nach benötigter Explizitheit und Typbeziehung.
- **DON'T:** Kein Interface/Protocol pro Klasse und keine Abstraktion für rein hypothetische Varianten.

### Abhängigkeiten
- **MUST:** Wesentliche Abhängigkeiten sichtbar und kontrollierbar machen.
- **SHOULD:** Dauerhafte Kollaborateure per Konstruktor, aufrufbezogene per Parameter übergeben.
- **DON'T:** Wesentliche technische Abhängigkeiten nicht tief im Code erzeugen oder über globale Zustände/Service Locator verstecken.
- **DON'T:** Kein DI-Framework, wenn normale Python-Parameter genügen.

### Zustand, Fehler, Ressourcen
- **MUST:** Objekte nach erfolgreicher Initialisierung in gültigem Zustand hinterlassen.
- **MUST:** Cleanup auch bei Fehlern garantieren.
- **SHOULD:** `try/finally` bzw. Context Manager für klaren Lifecycle verwenden.
- **DON'T:** Keine Exceptions ohne Grund verschlucken; kein `except Exception: pass`.
- **SHOULD:** Exceptions an sinnvollen Architekturgrenzen übersetzen, Diagnoseinformationen erhalten.

### API und Struktur
- **MUST:** Öffentliche APIs drücken Client-Absicht aus und verbergen unnötige technische Details.
- **SHOULD:** APIs klein halten; Implementierungsdetails mit `_` kennzeichnen.
- **MUST:** Module/Packages nach kohärenten Verantwortlichkeiten strukturieren.
- **DON'T:** Keine dauerhaften Ablagen wie `utils.py`, `helpers.py`, `common.py` für ungeklärte Verantwortlichkeiten.
- **SHOULD:** Öffentliche Framework-/Bibliotheks-APIs typannotieren.
- **SHOULD:** Docstrings nur für nicht offensichtlichen Zweck, Vertrag, Randbedingungen, Seiteneffekte oder Exceptions.
- **SHOULD:** `dataclass` nur für tatsächlich datenorientierte Objekte.

### Werkzeuge
- Deterministisch prüfbare Regeln durch Formatter, Linter, Type Checker und Tests prüfen lassen; KI ersetzt diese Werkzeuge nicht.

## Arbeitsweise

Vor nichttrivialen Änderungen:
1. Betroffenen und angrenzenden Code lesen.
2. Verantwortung, öffentliche API, Abhängigkeiten und Lifecycle erkennen.
3. Bestehende Konventionen wiederverwenden.
4. Kleinste Lösung für die aktuelle Anforderung wählen.
5. Neue Abstraktionen nur mit konkretem Nutzen einführen.
6. Nach der Änderung vorhandene Qualitätschecks/Tests ausführen.

## Abschlusscheck

Prüfe intern:
- klare Verantwortung?
- neue versteckte Kopplung?
- Vererbung wirklich Typbeziehung?
- jede neue Abstraktion notwendig?
- gültiger Zustand und Cleanup im Fehlerfall?
- API absichtsorientiert?
- unnötige Architektur eingeführt?

Melde nur relevante Verstöße oder offene Entscheidungen; gib den Check nicht routinemäßig vollständig aus.

## Offene Architekturentscheidungen

Wenn mehrere Lösungen erhebliche unterschiedliche Architekturfolgen haben und keine Projektregel entscheidet: nicht willkürlich eine neue Teamregel erfinden. Optionen und wesentliche Trade-offs knapp nennen und Entscheidung markieren.

Beispiele und vorhandene Implementierungen sind keine neuen verbindlichen Regeln. Neue Corporate Rules müssen ausdrücklich beschlossen werden.
