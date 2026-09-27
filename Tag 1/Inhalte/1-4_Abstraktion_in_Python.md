# 1-4 · Abstraktion in Python

Abstraktion trennt die Frage **„Was benötige ich?“** von **„Wie wird es konkret umgesetzt?“**. Python bietet dafür mehrere Mechanismen mit unterschiedlichem Formalisierungsgrad.

- **Duck Typing** – Ein Client verwendet ein Objekt aufgrund seines Verhaltens. Eine gemeinsame deklarierte Oberklasse ist nicht erforderlich.
- **Abstract Base Class (ABC)** – Eine ABC definiert einen expliziten nominalen Vertrag und kann gemeinsame Implementierung bereitstellen. Sie eignet sich, wenn eine bewusst modellierte Typfamilie existiert.
- **Protocol** – `typing.Protocol` beschreibt strukturell, welches Verhalten benötigt wird. Eine Klasse muss das Protocol nicht explizit erben, um typkompatibel zu sein.
- **Nominale Typisierung** – Zugehörigkeit entsteht durch explizite Typbeziehung, beispielsweise Vererbung oder Registrierung.
- **Strukturelle Typisierung** – Entscheidend ist die vorhandene Struktur bzw. das angebotene Verhalten.
- **Type Hints** – Typannotationen dokumentieren Erwartungen und unterstützen IDEs, statische Analyse und Refactoring, ohne Python in eine statisch typisierte Sprache zu verwandeln.
- **Kleine Verträge** – Je kleiner die benötigte Schnittstelle, desto geringer die Kopplung. Ein Client sollte nicht von Operationen abhängig sein, die er nicht verwendet.
- **Abstraktion hat Kosten** – Zusätzliche Interfaces, ABCs oder Protocols erhöhen die Zahl der Konzepte. Eine Abstraktion ist dann wertvoll, wenn sie reale Varianten, Austauschbarkeit oder eine wichtige Grenze ausdrückt.

## Drei mögliche Antworten auf dasselbe Problem

Ein Objekt benötigt beispielsweise lediglich eine Operation `send(message)`. Dafür kann der Code:

1. einfach Duck Typing verwenden,
2. eine gemeinsame ABC verlangen,
3. ein kleines Protocol beschreiben.

Keine Variante ist grundsätzlich „die richtige“. Entscheidend sind gewünschte Explizitheit, Tool-Unterstützung, Erweiterbarkeit und Kontext.

> **Merksatz:** Abstrahiert wird benötigtes Verhalten – nicht vorsorglich jede Implementierung.
