# Skill: Python Teamstandard – Proposal

> **Status:** Vorschlag für den Workshop.  
> Dieses Dokument ist kein fertiger Corporate Standard. Die Regeln werden mit dem Team geprüft, geändert, ergänzt und anschließend verbindlich beschlossen.

## Zweck

Dieser Skill definiert Leitplanken für Python-Code in diesem Projekt. Er richtet sich gleichermaßen an Entwickler und KI-Coding-Assistenten wie Claude Code.

Bei der Erzeugung, Änderung, Erweiterung oder beim Refactoring von Python-Code sind diese Regeln zu berücksichtigen.

Ziel ist nicht maximale Formalisierung, sondern Code, der:

- pythonisch und verständlich ist,
- klare Verantwortlichkeiten besitzt,
- Abhängigkeiten sichtbar macht,
- kontrollierbare Zustände und Lebenszyklen besitzt,
- stabile öffentliche APIs anbietet,
- testbar und wartbar bleibt,
- unnötige Abstraktionen vermeidet.

---

## 1. Verbindlichkeit

Die Regeln verwenden vier Stufen:

- **MUST** – verbindlich; nur ändern, wenn die Anforderung sonst nicht erfüllbar ist.
- **SHOULD** – Standardentscheidung; Abweichungen benötigen einen konkreten Grund.
- **MAY** – zulässige Option, wenn sie im Kontext einen Vorteil bringt.
- **DON'T** – bewusst zu vermeidendes Vorgehen.

Für eine KI gilt:

> Bei einem Konflikt zwischen einer expliziten Aufgabenanforderung und diesem Skill darf die Anforderung Vorrang haben. Die Abweichung ist sichtbar zu machen und darf nicht stillschweigend erfolgen.

---

# 2. Pythonisches OO-Design

## MUST

- Python-Sprachmittel und Python-Konventionen verwenden, statt Strukturen anderer OO-Sprachen mechanisch nachzubauen.
- Öffentliche und interne API bewusst unterscheiden.
- Bestehende öffentliche APIs respektieren, sofern ihre Änderung nicht Teil der Aufgabe ist.

## SHOULD

- Direkten Attributzugriff verwenden, solange kein zusätzlicher Vertrag erforderlich ist.
- Properties verwenden, wenn Zugriff kontrolliert, validiert oder berechnet werden muss.
- Magic Methods nur einsetzen, wenn das Objekt das entsprechende Python-Protokoll tatsächlich sinnvoll erfüllt.

## DON'T

- Keine vorsorglichen Java-artigen Getter und Setter.
- Kein Name Mangling mit `__name` als allgemeinen Ersatz für Kapselung.
- Keine Klassen ausschließlich deshalb erzeugen, weil „OO“ verlangt wird.

---

# 3. Verantwortlichkeiten und Kapselung

## MUST

- Jede Klasse benötigt eine klar benennbare Verantwortung.
- Invarianten eines Objekts dürfen nicht davon abhängen, dass fremder Code interne Zustände korrekt manipuliert.
- Fachlich oder technisch zusammengehöriges Verhalten dort kapseln, wo die dafür erforderliche Information liegt.

## SHOULD

Vor Einführung oder Erweiterung einer Klasse prüfen:

1. Welche Verantwortung besitzt sie?
2. Welche Ereignisse führen zu ihrer Änderung?
3. Gehören diese Änderungsgründe zusammen?

## DON'T

- Keine Sammelklassen wie `Utils`, `Helpers` oder `Common`, wenn sie unabhängige Verantwortlichkeiten bündeln.
- Keine God Objects.
- Internen Zustand nicht unnötig veröffentlichen.
- Keine Logik außerhalb eines Objekts platzieren, die dessen internen Zustand ausliest, interpretiert und anschließend wieder verändert, wenn das Verhalten sinnvoll zum Objekt gehört.

---

# 4. Vererbung, Komposition und Delegation

## MUST

Vererbung nur einsetzen, wenn eine echte und stabile Typbeziehung modelliert wird.

Eine Unterklasse muss sinnvoll überall dort verwendbar sein, wo der Basistyp erwartet wird.

## SHOULD

Komposition bevorzugen, wenn ein Objekt lediglich Fähigkeiten oder Dienste anderer Objekte benötigt.

Delegation verwenden, wenn eine öffentliche API stabil bleiben soll, die konkrete Arbeit aber ein Kollaborateur übernimmt.

## DON'T

- Vererbung nicht ausschließlich zur Wiederverwendung von Code einsetzen.
- Keine großen `BaseTest`- oder vergleichbaren Basisklassen als Werkzeugkiste.
- Keine tiefen Vererbungshierarchien ohne fachlich oder technisch klar begründete Typstruktur.
- Mixins nicht verwenden, wenn ihre Voraussetzungen an `self` verborgen oder schwer nachvollziehbar sind.

---

# 5. Abstraktionen

## Grundregel

> Abstrahiert wird benötigtes Verhalten – nicht vorsorglich jede Implementierung.

## SHOULD

Die kleinste ausreichende Form der Abstraktion wählen:

1. Duck Typing, wenn der Vertrag lokal und offensichtlich ist.
2. `Protocol`, wenn ein struktureller Vertrag explizit und statisch prüfbar sein soll.
3. `ABC`, wenn bewusst eine nominale Typfamilie modelliert wird oder gemeinsame Implementierung Teil des Entwurfs ist.

Abstraktionen aus Sicht des Clients formulieren: Welche Fähigkeit benötigt er tatsächlich?

## DON'T

- Kein Interface/Protocol für jede Klasse.
- Keine ABC allein deshalb, weil „gegen Interfaces programmiert werden soll“.
- Keine Abstraktion für hypothetische Varianten ohne erkennbaren Änderungs- oder Austauschbedarf.
- Keine großen Verträge, wenn der Client nur einen kleinen Teil davon benötigt.

---

# 6. Abhängigkeiten und Testbarkeit

## MUST

Wesentliche Abhängigkeiten müssen im Design erkennbar und kontrollierbar sein.

## SHOULD

- Dauerhafte Kollaborateure über den Konstruktor übergeben.
- Aufrufbezogene Kollaborateure über Methodenparameter übergeben.
- Technische Abhängigkeiten an geeigneten Grenzen austauschbar halten.
- Testbarkeit als Signal für die Qualität des Designs verwenden.

## DON'T

- Wesentliche technische Abhängigkeiten nicht tief in Methoden versteckt erzeugen.
- Keine globalen Singletons oder Service Locator als bequemen Ersatz für explizite Abhängigkeiten.
- Kein DI-Framework einführen, wenn normale Python-Parameter das Problem lösen.
- Nicht jede triviale Funktion künstlich injizieren.
- Keine Abstraktion ausschließlich erzeugen, damit sie gemockt werden kann.

---

# 7. Zustand, Lifecycle und Ressourcen

## MUST

- Ressourcen müssen auch im Fehlerfall zuverlässig freigegeben werden.
- Objekte dürfen nach erfolgreicher Initialisierung keinen unbeabsichtigt halbfertigen Zustand besitzen.
- Fehler dürfen nicht ohne nachvollziehbaren Grund verschluckt werden.

## SHOULD

- `try/finally` verwenden, wenn explizites Cleanup notwendig ist.
- Context Manager verwenden, wenn ein klar begrenzter Lifecycle modelliert wird.
- Ungültige Zustandsübergänge über die öffentliche API verhindern.
- Exceptions an sinnvollen Architekturgrenzen behandeln oder übersetzen.
- Für Diagnose relevante Informationen beim Übersetzen von Exceptions erhalten.

## DON'T

- Kein Cleanup nur im Happy Path.
- Kein pauschales `except Exception: pass`.
- Keine booleschen Rückgabewerte als Ersatz für unterschiedliche, diagnostisch relevante Fehlerursachen.

---

# 8. Öffentliche APIs

## MUST

Öffentliche APIs sollen die Absicht des Clients ausdrücken und unnötige Implementierungsdetails verbergen.

Bevorzugt:

```python
customers.select_customer(customer_id)
```

statt:

```python
table = screen.find("customerTable")
row = table.find_row("customerId", customer_id)
table.select_row(row)
```

wenn die technischen Schritte kein Bestandteil der fachlichen Aussage des Clients sind.

## SHOULD

- Öffentliche APIs klein halten.
- Methoden nach Verhalten bzw. Absicht benennen.
- Implementierungsdetails mit führendem Unterstrich kennzeichnen.
- APIs so schneiden, dass wahrscheinliche technische Änderungen möglichst lokal bleiben.

---

# 9. Type Hints, Docstrings und Datenobjekte

## SHOULD

- Öffentliche Framework- und Bibliotheks-APIs typannotieren.
- Type Hints verwenden, wenn sie Vertrag, Tool-Unterstützung oder Refactoring verbessern.
- Docstrings dort schreiben, wo Zweck, Vertrag, Randbedingungen, Seiteneffekte oder Exceptions nicht bereits offensichtlich sind.
- `dataclass` für tatsächlich datenorientierte Objekte erwägen.

## DON'T

- Keine Docstrings, die lediglich den Namen der Funktion in Prosa wiederholen.
- Keine Type Hints nur zur Dekoration.
- Nicht jede Klasse in eine `dataclass` verwandeln.

---

# 10. Module und Packages

## MUST

Die Projektstruktur soll Verantwortlichkeiten sichtbar machen.

## SHOULD

Module und Packages nach fachlichen oder technischen Verantwortlichkeiten strukturieren.

Beispielsweise:

```text
ui/
testdata/
workflows/
reporting/
configuration/
```

statt einer wachsenden Sammlung:

```text
helpers.py
utils.py
common.py
misc.py
```

## DON'T

Generische Sammelmodule nicht als dauerhaften Ablageort für Code verwenden, dessen Verantwortung nicht geklärt wurde.

---

# 11. Automatisierbare Regeln

Stilregeln, die deterministische Werkzeuge prüfen können, sollen nicht primär durch menschliche oder KI-Code-Reviews entschieden werden.

Dazu können gehören:

- Formatierung,
- Importreihenfolge,
- Naming-Regeln,
- Linting,
- Type Checking.

> KI ersetzt keinen Formatter, Linter oder Type Checker.

Die konkrete Toolchain wird separat im Teamstandard festgelegt.

---

# 12. Vorgehen für KI-Coding-Assistenten

Vor jeder nichttrivialen Änderung:

1. Bestehende Architektur und angrenzenden Code lesen.
2. Verantwortlichkeit der betroffenen Komponenten bestimmen.
3. Bestehende öffentliche APIs und Konventionen identifizieren.
4. Änderungsursache und benötigte Variabilität bestimmen.
5. Die einfachste Lösung wählen, die die Anforderung erfüllt.
6. Erst dann neue Abstraktionen, Klassen oder Framework-Schichten einführen.

Bei Änderungen gilt:

> Bestehende Architektur verstehen → lokal passende Änderung entwerfen → implementieren → gegen diesen Skill prüfen.

Nicht:

> Aufgabe erkennen → bekanntes Pattern auswählen → Code darum herum bauen.

---

# 13. Selbstprüfung vor Abschluss einer Änderung

Ein KI-Coding-Assistent MUSS vor Abschluss einer relevanten Änderung prüfen:

### Verantwortung
- Hat jede neue oder geänderte Klasse eine klare Verantwortung?
- Habe ich unabhängige Änderungsgründe vermischt?

### Kopplung
- Habe ich neue versteckte Abhängigkeiten eingeführt?
- Kenne ich konkrete Implementierungen, die der Client nicht kennen müsste?

### Vererbung
- Modelliert neue Vererbung tatsächlich eine Typbeziehung?
- Würde Komposition die Beziehung präziser ausdrücken?

### Abstraktion
- Welches konkrete Problem löst jede neue Abstraktion?
- Existiert der Variations- oder Austauschbedarf tatsächlich?

### Zustand und Lifecycle
- Kann ein ungültiger Zustand entstehen?
- Funktioniert Cleanup auch bei Exceptions?

### API
- Drückt die öffentliche API die Absicht des Clients aus?
- Sind Implementierungsdetails unnötig nach außen gelangt?

### Einfachheit
- Habe ich mehr Architektur erzeugt, als die Änderung benötigt?
- Kann eine neue Klasse, Schicht oder Abstraktion wieder entfernt werden, ohne eine wichtige Eigenschaft zu verlieren?

---

# 14. Verhalten bei Unsicherheit

Wenn mehrere Entwürfe fachlich vertretbar sind und die Entscheidung erhebliche Auswirkungen auf die Architektur hat:

**Nicht stillschweigend entscheiden.**

Stattdessen:

1. relevante Alternativen benennen,
2. Auswirkungen kurz gegenüberstellen,
3. bestehende Teamregeln berücksichtigen,
4. bei fehlender Regel die Entscheidung zur Abstimmung markieren.

Beispiel:

```text
ARCHITEKTURENTSCHEIDUNG OFFEN

Variante A: Protocol
+ expliziter struktureller Vertrag
+ statisch prüfbar
- zusätzliche Abstraktion

Variante B: Duck Typing
+ einfacher
+ für lokale Verwendung ausreichend
- Vertrag weniger explizit

Empfehlung nicht automatisch als Corporate Rule übernehmen.
```

---

# 15. Regeln nicht erfinden

Ein KI-Assistent darf aus diesem Dokument keine zusätzlichen verbindlichen Teamregeln ableiten.

Insbesondere gilt:

- Beispiele sind keine Regeln.
- Eine häufig verwendete Technik ist keine Regel.
- Eine persönliche Präferenz ist keine Regel.
- Eine KI-Empfehlung ist keine Regel.

Neue Regeln müssen vom Team beschlossen und anschließend ausdrücklich in diesen Skill aufgenommen werden.

---

# Kurzfassung für den Arbeitskontext

> Schreibe idiomatisches Python. Gib Klassen klare Verantwortlichkeiten. Schütze Invarianten. Verwende Vererbung nur für echte Typbeziehungen und Komposition für Zusammenarbeit. Abstrahiere nur bei konkretem Bedarf und wähle den kleinsten ausreichenden Vertrag. Mache wesentliche Abhängigkeiten sichtbar. Behandle Zustand, Lifecycle, Exceptions und Cleanup als Teil des Designs. Halte öffentliche APIs klein und absichtsorientiert. Nutze deterministische Werkzeuge für deterministisch prüfbare Regeln. Erzeuge keine zusätzliche Architektur ohne konkreten Nutzen. Bei wesentlichen offenen Architekturentscheidungen nicht raten, sondern Alternativen sichtbar machen.

---

## Workshop-Aufgabe

Dieses Proposal wird während Tag 1 überprüft.

Für jede Regel entscheidet das Team:

- **übernehmen**
- **ändern**
- **streichen**
- **Verbindlichkeit ändern**
- **ergänzen**

Das Ergebnis bildet die erste Version des **Python Coding & Engineering Skills** und dient an Tag 3 als maschinenlesbarer Arbeitskontext für Claude Code bzw. andere KI-Coding-Assistenten.
